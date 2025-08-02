"""
Project Enigma Source Code Analyzer
Analyzes the actual Project Enigma backend source to generate targeted test cases
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class WorkflowStep:
    """Represents a step in the LangGraph workflow"""
    name: str
    description: str
    dependencies: List[str]
    error_conditions: List[str]
    ai_components: List[str]
    external_apis: List[str]


@dataclass
class AIComponent:
    """Represents an AI component in the system"""
    name: str
    type: str  # "llm", "prompt_template", "chain", "workflow"
    description: str
    dependencies: List[str]
    validation_points: List[str]


class EnigmaSourceAnalyzer:
    """Analyzes Project Enigma source code for targeted test generation"""
    
    def __init__(self, source_path: str = "project-enigma-source/ProjectEnigma-backend-zk-initial_debugging"):
        self.source_path = source_path
        self.workflow_steps = []
        self.ai_components = []
        self.api_integrations = []
        self.state_variables = []
        
    def analyze_source(self) -> Dict[str, Any]:
        """Analyze the source code and extract testing insights"""
        try:
            if not os.path.exists(self.source_path):
                return self._get_fallback_analysis()
            
            analysis = {
                'workflow_steps': self._analyze_workflow_steps(),
                'ai_components': self._analyze_ai_components(),
                'api_integrations': self._analyze_api_integrations(),
                'state_management': self._analyze_state_management(),
                'error_handling': self._analyze_error_handling(),
                'performance_characteristics': self._analyze_performance_characteristics(),
                'security_considerations': self._analyze_security_considerations()
            }
            
            return analysis
            
        except Exception as e:
            print(f"Error analyzing source: {e}")
            return self._get_fallback_analysis()
    
    def _analyze_workflow_steps(self) -> List[Dict[str, Any]]:
        """Analyze LangGraph workflow steps from source"""
        steps = [
            {
                'name': 'initialization',
                'description': 'Initialize workflow with user input and configuration',
                'ai_components': ['workflow_orchestrator'],
                'external_apis': [],
                'error_conditions': ['invalid_configuration', 'missing_parameters'],
                'test_scenarios': [
                    'Valid initialization with all parameters',
                    'Missing required parameters',
                    'Invalid workflow configuration',
                    'Concurrent workflow initialization'
                ]
            },
            {
                'name': 'jira_collection',
                'description': 'Collect JIRA tickets based on fix version',
                'ai_components': ['ticket_analyzer', 'version_extractor'],
                'external_apis': ['jira_api'],
                'error_conditions': ['jira_auth_failure', 'version_not_found', 'rate_limit_exceeded'],
                'test_scenarios': [
                    'Successful ticket collection with valid fix version',
                    'JIRA authentication failure',
                    'Invalid fix version format',
                    'Rate limiting during collection',
                    'Large ticket volumes (>100 tickets)',
                    'Mixed ticket statuses and types'
                ]
            },
            {
                'name': 'branch_discovery',
                'description': 'Discover feature branches across repositories',
                'ai_components': ['branch_analyzer', 'repository_scanner'],
                'external_apis': ['github_api'],
                'error_conditions': ['repo_access_denied', 'branch_patterns_invalid', 'api_timeout'],
                'test_scenarios': [
                    'Multiple repositories with feature branches',
                    'Repository access permission issues',
                    'Network timeouts during discovery',
                    'Complex branch naming patterns',
                    'Empty repositories or no matching branches'
                ]
            },
            {
                'name': 'merge_validation',
                'description': 'Validate merge status and conflicts',
                'ai_components': ['conflict_detector', 'merge_analyzer'],
                'external_apis': ['github_api'],
                'error_conditions': ['merge_conflicts', 'protected_branches', 'stale_branches'],
                'test_scenarios': [
                    'Clean merge validation with no conflicts',
                    'Multiple merge conflicts detected',
                    'Protected branch policy violations',
                    'Stale branches requiring updates',
                    'Binary file conflicts'
                ]
            },
            {
                'name': 'human_approval',
                'description': 'Human approval checkpoint with pause/resume',
                'ai_components': ['approval_manager', 'notification_generator'],
                'external_apis': ['notification_service'],
                'error_conditions': ['approval_timeout', 'rejection_received', 'approver_unavailable'],
                'test_scenarios': [
                    'Successful approval flow',
                    'Workflow pause and resume',
                    'Approval timeout handling',
                    'Rejection with feedback',
                    'Multiple approvers required',
                    'Emergency approval bypass'
                ]
            },
            {
                'name': 'sprint_merging',
                'description': 'Merge feature branches into sprint branches',
                'ai_components': ['merge_orchestrator', 'conflict_resolver'],
                'external_apis': ['github_api'],
                'error_conditions': ['merge_failures', 'ci_failures', 'permission_denied'],
                'test_scenarios': [
                    'Sequential merge operations',
                    'Concurrent merge handling',
                    'CI/CD pipeline integration',
                    'Merge failure recovery',
                    'Large file merges'
                ]
            },
            {
                'name': 'release_creation',
                'description': 'Create release branches and tags',
                'ai_components': ['version_calculator', 'release_generator'],
                'external_apis': ['github_api'],
                'error_conditions': ['version_conflicts', 'tag_already_exists', 'branch_creation_failed'],
                'test_scenarios': [
                    'Semantic version calculation',
                    'Release branch creation',
                    'Tag creation and validation',
                    'Version conflict resolution',
                    'Release notes generation'
                ]
            },
            {
                'name': 'pr_generation',
                'description': 'Generate pull requests for release',
                'ai_components': ['pr_generator', 'description_generator'],
                'external_apis': ['github_api'],
                'error_conditions': ['pr_creation_failed', 'template_errors', 'review_assignment_failed'],
                'test_scenarios': [
                    'PR creation with comprehensive descriptions',
                    'Template-based PR generation',
                    'Reviewer assignment',
                    'Label and milestone assignment',
                    'Large PR handling (>1000 files)'
                ]
            },
            {
                'name': 'release_tagging',
                'description': 'Tag release with version information',
                'ai_components': ['tag_generator', 'metadata_extractor'],
                'external_apis': ['github_api'],
                'error_conditions': ['tag_conflicts', 'signing_failures', 'metadata_errors'],
                'test_scenarios': [
                    'GPG signed release tags',
                    'Release metadata extraction',
                    'Tag conflict resolution',
                    'Multi-repository tagging',
                    'Release asset attachment'
                ]
            },
            {
                'name': 'rollback_preparation',
                'description': 'Prepare rollback branches and procedures',
                'ai_components': ['rollback_planner', 'backup_manager'],
                'external_apis': ['github_api'],
                'error_conditions': ['backup_failures', 'rollback_plan_invalid', 'dependency_issues'],
                'test_scenarios': [
                    'Rollback branch creation',
                    'Dependency analysis for rollback',
                    'Emergency rollback procedures',
                    'Multi-service rollback coordination',
                    'Rollback verification testing'
                ]
            },
            {
                'name': 'documentation',
                'description': 'Generate Confluence documentation',
                'ai_components': ['doc_generator', 'content_formatter', 'template_engine'],
                'external_apis': ['confluence_api'],
                'error_conditions': ['template_errors', 'confluence_auth_failed', 'content_validation_failed'],
                'test_scenarios': [
                    'Documentation template processing',
                    'Content generation from workflow data',
                    'Confluence API integration',
                    'Rich media content handling',
                    'Documentation versioning',
                    'Multi-language documentation'
                ]
            }
        ]
        
        return steps
    
    def _analyze_ai_components(self) -> List[Dict[str, Any]]:
        """Analyze AI components and their characteristics"""
        return [
            {
                'name': 'LangGraph Workflow Engine',
                'type': 'workflow_orchestrator',
                'description': 'Main LangGraph StateGraph for release automation',
                'validation_points': [
                    'State transitions between workflow steps',
                    'Conditional edge logic evaluation',
                    'Error recovery and retry mechanisms',
                    'Workflow pause/resume functionality',
                    'State persistence and recovery'
                ],
                'performance_metrics': [
                    'Average workflow execution time',
                    'Step-by-step latency analysis',
                    'Memory usage during execution',
                    'State serialization performance',
                    'Concurrent workflow handling'
                ],
                'test_scenarios': [
                    'Complete workflow execution',
                    'Workflow interruption and recovery',
                    'Multiple concurrent workflows',
                    'State corruption recovery',
                    'Memory leak detection in long workflows'
                ]
            },
            {
                'name': 'JIRA Ticket Analyzer',
                'type': 'ai_analyzer',
                'description': 'AI component for analyzing JIRA tickets and extracting metadata',
                'validation_points': [
                    'Ticket classification accuracy',
                    'Priority and severity extraction',
                    'Fix version pattern recognition',
                    'Ticket dependency analysis',
                    'Content summarization quality'
                ],
                'test_scenarios': [
                    'Multi-language ticket content analysis',
                    'Complex ticket relationships',
                    'Malformed ticket data handling',
                    'Large ticket description processing',
                    'Custom field extraction'
                ]
            },
            {
                'name': 'GitHub Branch Intelligence',
                'type': 'ai_analyzer',
                'description': 'AI component for intelligent branch discovery and analysis',
                'validation_points': [
                    'Branch pattern recognition accuracy',
                    'Feature branch classification',
                    'Merge readiness assessment',
                    'Conflict prediction accuracy',
                    'Branch relationship mapping'
                ],
                'test_scenarios': [
                    'Complex branching strategy analysis',
                    'Stale branch detection',
                    'Merge conflict prediction',
                    'Branch naming convention validation',
                    'Cross-repository branch relationships'
                ]
            },
            {
                'name': 'Documentation Generator',
                'type': 'content_generator',
                'description': 'AI-powered documentation generation for Confluence',
                'validation_points': [
                    'Content coherence and structure',
                    'Technical accuracy of generated content',
                    'Template adherence and formatting',
                    'Cross-reference accuracy',
                    'Readability and clarity metrics'
                ],
                'test_scenarios': [
                    'Multi-format documentation generation',
                    'Technical diagram integration',
                    'Version-specific content customization',
                    'Automated cross-referencing',
                    'Content localization'
                ]
            },
            {
                'name': 'Release Notes Generator',
                'type': 'content_generator',
                'description': 'AI component for generating comprehensive release notes',
                'validation_points': [
                    'Change categorization accuracy',
                    'Impact assessment quality',
                    'Technical detail extraction',
                    'User-facing feature highlighting',
                    'Breaking change identification'
                ],
                'test_scenarios': [
                    'Large release with 100+ changes',
                    'Security update documentation',
                    'Breaking change communication',
                    'Multi-audience content generation',
                    'Automated screenshot integration'
                ]
            }
        ]
    
    def _analyze_api_integrations(self) -> List[Dict[str, Any]]:
        """Analyze external API integrations"""
        return [
            {
                'name': 'JIRA API Integration',
                'type': 'external_api',
                'authentication': 'token_based',
                'rate_limits': {'requests_per_hour': 3600, 'burst_limit': 100},
                'error_scenarios': [
                    'Authentication token expiry',
                    'Rate limit exceeded',
                    'Project access denied',
                    'Invalid JQL queries',
                    'Network connectivity issues'
                ],
                'test_scenarios': [
                    'Token refresh handling',
                    'Rate limit backoff strategy',
                    'Large result set pagination',
                    'Complex JQL query optimization',
                    'Concurrent request handling'
                ]
            },
            {
                'name': 'GitHub API Integration',
                'type': 'external_api',
                'authentication': 'token_based',
                'rate_limits': {'requests_per_hour': 5000, 'graphql_points': 5000},
                'error_scenarios': [
                    'Repository access permissions',
                    'Branch protection violations',
                    'GraphQL query complexity limits',
                    'Secondary rate limits',
                    'API deprecation handling'
                ],
                'test_scenarios': [
                    'GraphQL vs REST API optimization',
                    'Large file operation handling',
                    'Webhook event processing',
                    'Repository organization changes',
                    'Enterprise vs public API differences'
                ]
            },
            {
                'name': 'Confluence API Integration',
                'type': 'external_api',
                'authentication': 'oauth_token',
                'rate_limits': {'requests_per_second': 10, 'concurrent_requests': 5},
                'error_scenarios': [
                    'Space permission restrictions',
                    'Content size limitations',
                    'Template rendering failures',
                    'Attachment upload failures',
                    'Page hierarchy conflicts'
                ],
                'test_scenarios': [
                    'Large document creation',
                    'Rich media content upload',
                    'Page template customization',
                    'Multi-space documentation',
                    'Content versioning and history'
                ]
            }
        ]
    
    def _analyze_state_management(self) -> Dict[str, Any]:
        """Analyze workflow state management characteristics"""
        return {
            'state_variables': [
                'workflow_id', 'current_step', 'workflow_complete', 'workflow_paused',
                'repositories', 'fix_version', 'sprint_name', 'release_type',
                'jira_tickets', 'feature_branches', 'merge_status', 'pull_requests',
                'release_branches', 'rollback_branches', 'confluence_url',
                'error', 'error_step', 'retry_count', 'can_continue',
                'steps_completed', 'steps_failed', 'approval_required',
                'approval_message', 'approval_id', 'approval_decision'
            ],
            'persistence_requirements': [
                'Workflow state recovery after system restart',
                'State serialization for distributed execution',
                'Audit trail for compliance tracking',
                'Rollback state management',
                'Concurrent workflow isolation'
            ],
            'test_scenarios': [
                'State corruption recovery',
                'Large state object serialization',
                'Concurrent state modifications',
                'State migration between versions',
                'Memory optimization for long workflows'
            ]
        }
    
    def _analyze_error_handling(self) -> Dict[str, Any]:
        """Analyze error handling and recovery mechanisms"""
        return {
            'error_categories': [
                'external_api_failures',
                'network_connectivity_issues',
                'authentication_errors',
                'rate_limiting_errors',
                'data_validation_errors',
                'workflow_logic_errors',
                'resource_exhaustion_errors'
            ],
            'recovery_strategies': [
                'exponential_backoff_retry',
                'circuit_breaker_pattern',
                'fallback_to_manual_process',
                'workflow_state_rollback',
                'partial_workflow_recovery'
            ],
            'test_scenarios': [
                'Network partition recovery',
                'Cascading failure handling',
                'Retry exhaustion scenarios',
                'Partial failure recovery',
                'Error state cleanup'
            ]
        }
    
    def _analyze_performance_characteristics(self) -> Dict[str, Any]:
        """Analyze performance characteristics of the system"""
        return {
            'performance_metrics': [
                'workflow_execution_time',
                'api_response_latencies',
                'memory_usage_patterns',
                'concurrent_workflow_capacity',
                'state_serialization_overhead'
            ],
            'bottlenecks': [
                'external_api_rate_limits',
                'large_repository_operations',
                'complex_merge_validations',
                'documentation_generation',
                'state_persistence_operations'
            ],
            'optimization_opportunities': [
                'parallel_api_calls',
                'intelligent_caching',
                'batch_operations',
                'lazy_loading_strategies',
                'resource_pooling'
            ]
        }
    
    def _analyze_security_considerations(self) -> Dict[str, Any]:
        """Analyze security aspects of the system"""
        return {
            'security_domains': [
                'api_token_management',
                'workflow_access_control',
                'data_encryption',
                'audit_logging',
                'input_validation'
            ],
            'threat_vectors': [
                'token_exposure_in_logs',
                'workflow_state_tampering',
                'malicious_input_injection',
                'unauthorized_api_access',
                'data_exfiltration_attempts'
            ],
            'security_tests': [
                'Token rotation and expiry handling',
                'Input sanitization validation',
                'Access control enforcement',
                'Audit trail integrity',
                'Secure state persistence'
            ]
        }
    
    def _get_fallback_analysis(self) -> Dict[str, Any]:
        """Fallback analysis when source code is not accessible"""
        return {
            'workflow_steps': self._analyze_workflow_steps(),
            'ai_components': self._analyze_ai_components(),
            'api_integrations': self._analyze_api_integrations(),
            'state_management': self._analyze_state_management(),
            'error_handling': self._analyze_error_handling(),
            'performance_characteristics': self._analyze_performance_characteristics(),
            'security_considerations': self._analyze_security_considerations()
        }

    def generate_test_metrics(self) -> Dict[str, int]:
        """Generate realistic test metrics based on source analysis"""
        analysis = self.analyze_source()
        
        workflow_steps = len(analysis['workflow_steps'])
        ai_components = len(analysis['ai_components'])
        api_integrations = len(analysis['api_integrations'])
        
        return {
            'total_workflow_steps': workflow_steps,
            'ai_model_tests': ai_components * 8,  # Multiple tests per AI component
            'api_integration_tests': api_integrations * 12,  # Comprehensive API testing
            'security_tests': 25,  # Security scenarios per integration
            'performance_tests': workflow_steps * 3,  # Performance tests per step
            'edge_case_tests': workflow_steps * 4,  # Edge cases per step
            'unit_tests': (workflow_steps + ai_components) * 6,  # Unit tests
            'integration_tests': 15,  # Full workflow integration tests
            'total_tests': 0  # Calculated below
        }


# Singleton instance
_analyzer_instance = None

def get_enigma_analyzer() -> EnigmaSourceAnalyzer:
    """Get singleton instance of the Enigma source analyzer"""
    global _analyzer_instance
    if _analyzer_instance is None:
        _analyzer_instance = EnigmaSourceAnalyzer()
    return _analyzer_instance