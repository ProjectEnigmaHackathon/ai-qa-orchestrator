"""Workflow management endpoints for human approval and workflow control."""

import asyncio
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from app.workflows.workflow_manager import get_workflow_manager

router = APIRouter()


class ApprovalRequest(BaseModel):
    """Request model for approval decisions."""

    workflow_id: str
    approved: bool
    notes: Optional[str] = ""
    user_id: Optional[str] = "user"


class ApprovalResponse(BaseModel):
    """Response model for approval decisions."""

    approval_id: str
    workflow_id: str
    status: str  # "approved", "denied", "timeout"
    message: str
    timestamp: datetime


class WorkflowAction(BaseModel):
    """Request model for workflow actions."""

    workflow_id: str
    action: str  # "pause", "resume", "cancel"


# Global store for pending approvals (in production, use Redis)
pending_approvals: Dict[str, Dict[str, Any]] = {}
approval_timeouts: Dict[str, datetime] = {}


@router.post("/approval")
async def handle_approval_decision(request: ApprovalRequest) -> ApprovalResponse:
    """
    Handle human approval decisions for workflow checkpoints.
    """
    try:
        workflow_manager = get_workflow_manager()

        # Check if approval is pending
        if request.workflow_id not in pending_approvals:
            raise HTTPException(
                status_code=404,
                detail=f"No pending approval found for workflow {request.workflow_id}",
            )

        approval_data = pending_approvals[request.workflow_id]
        approval_id = approval_data["approval_id"]

        # Create approval response
        response = ApprovalResponse(
            approval_id=approval_id,
            workflow_id=request.workflow_id,
            status="approved" if request.approved else "denied",
            message=f"Approval {'granted' if request.approved else 'denied'} by {request.user_id}",
            timestamp=datetime.now(),
        )

        # Update workflow state with approval decision
        current_state = workflow_manager.state_store.get_state(request.workflow_id)
        if current_state:
            current_state["approval_decision"] = {
                "approved": request.approved,
                "notes": request.notes,
                "user_id": request.user_id,
                "timestamp": datetime.now().isoformat(),
                "approval_id": approval_id,
            }
            current_state["approval_required"] = False

            # Get and update metadata
            metadata = workflow_manager.state_store.get_metadata(request.workflow_id)
            if metadata:
                metadata.status = "running" if request.approved else "cancelled"
                metadata.current_step = (
                    "sprint_merging" if request.approved else "complete"
                )
                workflow_manager.state_store.store_state(
                    request.workflow_id, current_state, metadata
                )

                # Resume workflow if approved
                if request.approved:
                    await workflow_manager.resume_workflow(request.workflow_id)
                else:
                    # Cancel workflow if denied
                    await workflow_manager.cancel_workflow(request.workflow_id)

        # Clean up pending approval
        pending_approvals.pop(request.workflow_id, None)
        approval_timeouts.pop(request.workflow_id, None)

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing approval: {str(e)}"
        )


@router.get("/approval/{workflow_id}")
async def get_pending_approval(workflow_id: str):
    """
    Get pending approval details for a workflow.
    """
    if workflow_id not in pending_approvals:
        raise HTTPException(
            status_code=404,
            detail=f"No pending approval found for workflow {workflow_id}",
        )

    approval_data = pending_approvals[workflow_id]
    timeout = approval_timeouts.get(workflow_id)

    return {
        "approval_id": approval_data["approval_id"],
        "workflow_id": workflow_id,
        "message": approval_data["message"],
        "created_at": approval_data["created_at"],
        "timeout_at": timeout.isoformat() if timeout else None,
        "is_expired": timeout and datetime.now() > timeout if timeout else False,
    }


@router.get("/approval")
async def list_pending_approvals():
    """
    List all pending approvals.
    """
    current_time = datetime.now()
    approvals = []

    for workflow_id, approval_data in pending_approvals.items():
        timeout = approval_timeouts.get(workflow_id)
        is_expired = timeout and current_time > timeout if timeout else False

        approvals.append(
            {
                "approval_id": approval_data["approval_id"],
                "workflow_id": workflow_id,
                "message": approval_data["message"],
                "created_at": approval_data["created_at"],
                "timeout_at": timeout.isoformat() if timeout else None,
                "is_expired": is_expired,
            }
        )

    return {"pending_approvals": approvals}


@router.post("/workflow/action")
async def workflow_action(request: WorkflowAction):
    """
    Perform actions on workflows (pause, resume, cancel).
    """
    try:
        workflow_manager = get_workflow_manager()

        if request.action == "pause":
            success = await workflow_manager.pause_workflow(request.workflow_id)
            return {
                "workflow_id": request.workflow_id,
                "action": "pause",
                "success": success,
                "message": (
                    "Workflow paused successfully"
                    if success
                    else "Failed to pause workflow"
                ),
            }

        elif request.action == "resume":
            success = await workflow_manager.resume_workflow(request.workflow_id)
            return {
                "workflow_id": request.workflow_id,
                "action": "resume",
                "success": success,
                "message": (
                    "Workflow resumed successfully"
                    if success
                    else "Failed to resume workflow"
                ),
            }

        elif request.action == "cancel":
            success = await workflow_manager.cancel_workflow(request.workflow_id)
            return {
                "workflow_id": request.workflow_id,
                "action": "cancel",
                "success": success,
                "message": (
                    "Workflow cancelled successfully"
                    if success
                    else "Failed to cancel workflow"
                ),
            }

        else:
            raise HTTPException(
                status_code=400, detail=f"Unknown action: {request.action}"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error performing workflow action: {str(e)}"
        )


@router.get("/workflow/{workflow_id}/status")
async def get_workflow_status(workflow_id: str):
    """
    Get current workflow status and progress.
    """
    try:
        workflow_manager = get_workflow_manager()
        status = workflow_manager.get_workflow_status(workflow_id)

        if not status:
            raise HTTPException(
                status_code=404, detail=f"Workflow {workflow_id} not found"
            )

        # Add approval information if pending
        if workflow_id in pending_approvals:
            status["pending_approval"] = pending_approvals[workflow_id]
            timeout = approval_timeouts.get(workflow_id)
            status["approval_timeout"] = timeout.isoformat() if timeout else None

        return status

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error getting workflow status: {str(e)}"
        )


@router.get("/workflows")
async def list_workflows():
    """
    List all workflows with their current status.
    """
    try:
        workflow_manager = get_workflow_manager()
        workflows = workflow_manager.list_workflows()

        # Add approval information for workflows with pending approvals
        for workflow in workflows:
            workflow_id = workflow["workflow_id"]
            if workflow_id in pending_approvals:
                workflow["pending_approval"] = pending_approvals[workflow_id]
                timeout = approval_timeouts.get(workflow_id)
                workflow["approval_timeout"] = timeout.isoformat() if timeout else None

        return {"workflows": workflows}

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error listing workflows: {str(e)}"
        )


def create_approval_checkpoint(
    workflow_id: str, message: str, timeout_minutes: int = 30
) -> str:
    """
    Create a new approval checkpoint for a workflow.

    Args:
        workflow_id: The workflow ID requiring approval
        message: The approval message/description
        timeout_minutes: Approval timeout in minutes

    Returns:
        approval_id: Unique approval identifier
    """
    approval_id = str(uuid.uuid4())

    approval_data = {
        "approval_id": approval_id,
        "workflow_id": workflow_id,
        "message": message,
        "created_at": datetime.now().isoformat(),
        "status": "pending",
    }

    pending_approvals[workflow_id] = approval_data
    approval_timeouts[workflow_id] = datetime.now() + timedelta(minutes=timeout_minutes)

    return approval_id


async def cleanup_expired_approvals():
    """
    Background task to clean up expired approvals.
    """
    while True:
        try:
            current_time = datetime.now()
            expired_workflows = []

            for workflow_id, timeout in approval_timeouts.items():
                if current_time > timeout:
                    expired_workflows.append(workflow_id)

            # Handle expired approvals
            for workflow_id in expired_workflows:
                workflow_manager = get_workflow_manager()

                # Update workflow state to indicate timeout
                current_state = workflow_manager.state_store.get_state(workflow_id)
                if current_state:
                    current_state["approval_decision"] = {
                        "approved": False,
                        "notes": "Approval timeout - automatically denied",
                        "user_id": "system",
                        "timestamp": current_time.isoformat(),
                        "approval_id": pending_approvals[workflow_id]["approval_id"],
                    }
                    current_state["approval_required"] = False

                    # Update metadata
                    metadata = workflow_manager.state_store.get_metadata(workflow_id)
                    if metadata:
                        metadata.status = "cancelled"
                        metadata.current_step = "complete"
                        metadata.last_error = "Approval timeout"
                        workflow_manager.state_store.store_state(
                            workflow_id, current_state, metadata
                        )

                        # Cancel the workflow
                        await workflow_manager.cancel_workflow(workflow_id)

                # Clean up
                pending_approvals.pop(workflow_id, None)
                approval_timeouts.pop(workflow_id, None)

            await asyncio.sleep(60)  # Check every minute

        except Exception as e:
            print(f"Error in approval cleanup task: {e}")
            await asyncio.sleep(60)


# Start the cleanup task when the module is imported
import threading

cleanup_thread = threading.Thread(
    target=lambda: asyncio.run(cleanup_expired_approvals()), daemon=True
)
cleanup_thread.start()
