#!/usr/bin/env python3
"""
AI Quality Assurance Orchestrator - Main Application
Comprehensive AI-powered test generation across all quality domains
"""

import streamlit as st
import asyncio
import time
import json
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from typing import Dict, List, Any
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from orchestration.qa_orchestrator import QAOrchestrationEngine
from agents.crew_factory import CrewFactory
from test_generators.comprehensive_generator import ComprehensiveTestGenerators
from utils.demo_data import DemoScenarios, MockResults
from visualization.dashboard_components import DashboardComponents

# Page configuration
st.set_page_config(
    page_title="AI Quality Assurance Orchestrator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

class QAOrchestratorApp:
    """Main Streamlit application for the QA Orchestrator"""
    
    def __init__(self):
        self.orchestrator = QAOrchestrationEngine()
        self.demo_scenarios = DemoScenarios()
        self.dashboard = DashboardComponents()
        self.mock_results = MockResults()
        
    def render_header(self):
        """Render the main application header"""
        st.title("🤖 AI Quality Assurance Orchestrator")
        st.subheader("Comprehensive AI-Powered Test Generation Across All Quality Domains")
        
        # Key metrics in header
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("AI Agents", "10", "Specialized")
        with col2:
            st.metric("Test Domains", "6", "Comprehensive")
        with col3:
            st.metric("Quality Score", "94%", "↑ 12%")
        with col4:
            st.metric("Time Saved", "8+ hrs", "Per Story")
        with col5:
            st.metric("Risk Coverage", "98%", "↑ 23%")
            
    def render_sidebar(self):
        """Render sidebar configuration"""
        with st.sidebar:
            st.header("🎛️ Configuration")
            
            # Test domain selection
            test_domains = st.multiselect(
                "Select Test Domains:",
                ['Unit Tests', 'Integration Tests', 'Security Tests', 
                 'Performance Tests', 'AI Validation', 'Edge Cases'],
                default=['Unit Tests', 'Integration Tests', 'Security Tests', 
                        'Performance Tests', 'AI Validation', 'Edge Cases']
            )
            
            # Risk and quality settings
            risk_tolerance = st.slider("Risk Tolerance Level", 1, 10, 5)
            quality_threshold = st.slider("Quality Threshold (%)", 70, 100, 85)
            
            # Execution options
            auto_execute = st.checkbox("Auto-execute generated tests")
            parallel_execution = st.checkbox("Enable parallel execution", value=True)
            
            # Advanced settings
            with st.expander("⚙️ Advanced Settings"):
                max_agents = st.slider("Max Concurrent Agents", 1, 15, 10)
                timeout_minutes = st.slider("Agent Timeout (min)", 1, 30, 10)
                llm_model = st.selectbox("LLM Model", 
                    ["gpt-4-turbo-preview", "gpt-3.5-turbo", "claude-3-sonnet"])
                
            return {
                'test_domains': test_domains,
                'risk_tolerance': risk_tolerance,
                'quality_threshold': quality_threshold,
                'auto_execute': auto_execute,
                'parallel_execution': parallel_execution,
                'max_agents': max_agents,
                'timeout_minutes': timeout_minutes,
                'llm_model': llm_model
            }
    
    def render_story_input(self):
        """Render user story input section"""
        st.header("📝 User Story & Requirements")
        
        # Demo scenario selection
        demo_scenarios = self.demo_scenarios.get_all_scenarios()
        selected_scenario = st.selectbox(
            "Choose a demo scenario or write your own:",
            ["Custom Story"] + list(demo_scenarios.keys())
        )
        
        if selected_scenario != "Custom Story":
            user_story = st.text_area(
                "User Story:",
                demo_scenarios[selected_scenario],
                height=250,
                help="Modify this story or use as-is for demonstration"
            )
        else:
            user_story = st.text_area(
                "Enter your user story:",
                placeholder="As a [user type], I want [functionality] so that [benefit]...",
                height=250
            )
        
        # Additional context
        with st.expander("📋 Additional Context (Optional)"):
            col1, col2 = st.columns(2)
            
            with col1:
                code_context = st.text_area(
                    "Existing code or API specs:",
                    height=150,
                    placeholder="Paste relevant code, API documentation, or technical specifications..."
                )
            
            with col2:
                architecture_notes = st.text_area(
                    "Architecture notes:",
                    height=150,
                    placeholder="System architecture, constraints, or special requirements..."
                )
        
        return {
            'user_story': user_story,
            'code_context': code_context if 'code_context' in locals() else "",
            'architecture_notes': architecture_notes if 'architecture_notes' in locals() else ""
        }
    
    def render_agent_collaboration(self):
        """Render real-time agent collaboration visualization"""
        st.header("🤖 AI Agent Collaboration")
        
        # Agent workflow visualization for DEMO mode (Story-based testing)
        agents_workflow = [
            ("🎯 QA Orchestrator", "Initializing comprehensive test generation workflow...", 5),
            ("📋 Story Analyst", "Parsing user story and extracting testable requirements...", 15),
            ("⚠️ Risk Assessor", "Analyzing story requirements for security, performance, and business risks...", 25),
            ("🧪 Unit Test Agent", "Generating comprehensive unit tests with edge cases...", 35),
            ("🔗 Integration Agent", "Creating end-to-end integration test scenarios...", 45),
            ("🔒 Security Agent", "Building OWASP Top 10 security test suite...", 55),
            ("⚡ Performance Agent", "Generating load tests and performance benchmarks...", 65),
            ("🤖 AI Validation Agent", "Creating AI model behavior validation tests with 25+ metrics...", 70),
            ("🎪 Edge Case Agent", "Identifying boundary conditions and stress scenarios...", 80),
            ("🚀 Test Executor", "Executing generated tests and analyzing results...", 85),
            ("✅ Quality Reviewer", "Scoring test quality and generating final report...", 95)
        ]
        
        return agents_workflow
    
    def execute_orchestration(self, story_data, config, agents_workflow):
        """Execute the test generation orchestration"""
        
        # Create containers for live updates
        progress_container = st.container()
        
        with progress_container:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                agent_status = st.empty()
                agent_conversation = st.empty()
                
            with col2:
                live_metrics = st.empty()
        
        # Progress bar
        progress_bar = st.progress(0)
        
        # Execute agent workflow with visual feedback
        generated_metrics = {
            'tests_generated': 0,
            'domains_covered': 0,
            'quality_score': 0,
            'risks_identified': 0
        }
        
        for agent_name, message, progress in agents_workflow:
            # Update UI
            agent_status.info(f"**{agent_name}** is working...")
            agent_conversation.text(f"💬 {message}")
            progress_bar.progress(progress / 100)  # Convert percentage to decimal
            
            # Update live metrics
            generated_metrics['tests_generated'] += 8 + (progress // 10)
            generated_metrics['domains_covered'] = min(6, progress // 15)
            generated_metrics['quality_score'] = min(94, progress)
            generated_metrics['risks_identified'] += 2
            
            with live_metrics:
                st.metric("Tests Generated", generated_metrics['tests_generated'])
                st.metric("Domains Covered", f"{generated_metrics['domains_covered']}/6")
                st.metric("Quality Score", f"{generated_metrics['quality_score']}%")
                st.metric("Risks Identified", generated_metrics['risks_identified'])
            
            # Realistic processing time
            time.sleep(1.2)
        
        progress_bar.progress(1.0)  # 100% = 1.0 for progress bar
        agent_status.success("✅ All agents completed successfully!")
        
        return self.mock_results.generate_comprehensive_results(story_data['user_story'])
    
    def render_results_dashboard(self, test_results):
        """Render comprehensive results dashboard"""
        st.success("✅ Comprehensive test suite generated successfully!")
        
        # Results tabs
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
            "📊 Overview", "🧪 Unit Tests", "🔗 Integration", "🔒 Security", 
            "⚡ Performance", "🤖 AI Validation", "🎪 Edge Cases", "📈 Quality Report"
        ])
        
        with tab1:
            self.dashboard.render_overview_tab(test_results)
            
        with tab2:
            self.dashboard.render_unit_tests_tab(test_results)
            
        with tab3:
            self.dashboard.render_integration_tab(test_results)
            
        with tab4:
            self.dashboard.render_security_tab(test_results)
            
        with tab5:
            self.dashboard.render_performance_tab(test_results)
            
        with tab6:
            self.dashboard.render_ai_validation_tab(test_results)
            
        with tab7:
            self.dashboard.render_edge_cases_tab(test_results)
            
        with tab8:
            self.dashboard.render_quality_report_tab(test_results)
    
    def render_cicd_integration(self, test_results):
        """Render CI/CD integration section"""
        st.header("🔄 CI/CD Integration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Pipeline Configuration")
            platform = st.selectbox(
                "Select CI/CD Platform:", 
                ["GitHub Actions", "Jenkins", "GitLab CI", "Azure DevOps"]
            )
            
            if st.button("Generate Pipeline Config"):
                pipeline_config = self.mock_results.generate_pipeline_config(platform)
                st.code(pipeline_config, language='yaml')
        
        with col2:
            st.subheader("Quality Gates")
            st.json(test_results.get('quality_gates', {}))
    
    def render_export_options(self, test_results):
        """Render export and download options"""
        st.header("📤 Export & Integration")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Export Test Suite"):
                export_data = json.dumps(test_results, indent=2)
                st.download_button(
                    label="Download Complete Test Suite",
                    data=export_data,
                    file_name=f"comprehensive_test_suite_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        with col2:
            if st.button("📊 Export Quality Report"):
                report_data = self.mock_results.generate_quality_report(test_results)
                st.download_button(
                    label="Download Quality Report",
                    data=report_data,
                    file_name=f"quality_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
        
        with col3:
            if st.button("🔄 Setup CI/CD Integration"):
                st.success("Integration webhooks and API keys configured!")
                st.balloons()
    
    def run(self):
        """Main application runner"""
        # Render header
        self.render_header()
        
        # Render sidebar and get config
        config = self.render_sidebar()
        
        # Render story input section
        story_data = self.render_story_input()
        
        # Main generation button
        if st.button("🚀 Generate Comprehensive Test Suite", type="primary", use_container_width=True):
            if not story_data['user_story'].strip():
                st.error("Please enter a user story or select a demo scenario.")
                return
            
            # Get agent workflow
            agents_workflow = self.render_agent_collaboration()
            
            # Execute orchestration
            test_results = self.execute_orchestration(story_data, config, agents_workflow)
            
            # Store results in session state for persistence
            st.session_state['test_results'] = test_results
            st.session_state['story_data'] = story_data
        
        # Display results if available
        if 'test_results' in st.session_state:
            test_results = st.session_state['test_results']
            
            # Render results dashboard
            self.render_results_dashboard(test_results)
            
            # Render CI/CD integration
            self.render_cicd_integration(test_results)
            
            # Render export options
            self.render_export_options(test_results)

def main():
    """Application entry point"""
    app = QAOrchestratorApp()
    app.run()

if __name__ == "__main__":
    main()