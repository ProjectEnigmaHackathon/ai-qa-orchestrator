"""
CrewAI Agent Factory - Creates specialized AI agents for comprehensive testing
"""

from crewai import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
from langchain.tools import Tool
from typing import List, Dict, Any
import os
import sys
sys.path.append('..')
from config import config

from tools.analysis_tools import AnalysisTools
from tools.test_generation_tools import TestGenerationTools
from tools.quality_tools import QualityTools
from tools.test_execution_tools import TestExecutionTools
from tools.ai_validation_metrics import AIValidationMetrics
from agents.application_discovery_agent import ApplicationDiscoveryAgent


class CrewFactory:
    """Factory for creating specialized CrewAI agents and crews"""
    
    def __init__(self, llm_model: str = "claude-3-5-sonnet-20241022"):
        # Use API key from config (loads from .env file)
        self.llm = ChatAnthropic(
            model=llm_model,
            temperature=0.2,
            anthropic_api_key=config.get_anthropic_key()
        )
        self.analysis_tools = AnalysisTools()
        self.test_gen_tools = TestGenerationTools()
        self.quality_tools = QualityTools()
        self.execution_tools = TestExecutionTools()
        self.ai_validation_metrics = AIValidationMetrics()
        self.discovery_agent = ApplicationDiscoveryAgent(llm_model)
        
    def create_qa_orchestrator_agent(self) -> Agent:
        """Create the main QA orchestrator agent"""
        return Agent(
            role='QA Orchestrator & Architect',
            goal='Coordinate comprehensive test generation across all quality domains and ensure strategic alignment',
            backstory="""You are a Senior QA Architect with 15+ years of experience in quality engineering,
            test automation, and SDLC optimization. You have deep expertise in risk assessment, test strategy,
            and coordinating complex testing initiatives. Your role is to orchestrate the entire testing process,
            ensuring comprehensive coverage across all quality domains while maintaining high standards and efficiency.""",
            tools=[
                self.analysis_tools.story_analyzer,
                self.analysis_tools.priority_manager,
                self.quality_tools.orchestration_coordinator
            ],
            llm=self.llm,
            max_execution_time=300,
            verbose=True
        )
    
    def create_story_analyst_agent(self) -> Agent:
        """Create the story analysis specialist agent"""
        return Agent(
            role='Requirements & Story Analysis Specialist',
            goal='Parse user stories, extract testable requirements, and identify business context and acceptance criteria',
            backstory="""You are a Business Analyst and Requirements Engineer with expertise in story mapping,
            acceptance criteria definition, and requirement traceability. You excel at breaking down complex user stories
            into testable components and identifying the underlying business rules and data flows. Your analysis forms
            the foundation for comprehensive test generation.""",
            tools=[
                self.analysis_tools.nlp_parser,
                self.analysis_tools.requirement_extractor,
                self.analysis_tools.business_rule_analyzer
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_application_discovery_agent(self) -> Agent:
        """Create the application discovery specialist agent"""
        return self.discovery_agent.create_agent()
    
    def create_risk_assessor_agent(self) -> Agent:
        """Create the risk assessment specialist agent"""
        return Agent(
            role='Risk Analysis & Security Assessment Specialist',
            goal='Identify technical, security, performance, and business risks requiring specialized testing approaches',
            backstory="""You are a Risk Management Expert with deep knowledge of cybersecurity, system architecture,
            and business continuity. You have experience in threat modeling, vulnerability assessment, and risk-based
            testing strategies. Your expertise helps prioritize testing efforts based on potential impact and likelihood
            of various risk scenarios.""",
            tools=[
                self.analysis_tools.risk_matrix_calculator,
                self.analysis_tools.vulnerability_scanner,
                self.analysis_tools.complexity_analyzer
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_unit_test_agent(self) -> Agent:
        """Create the unit test generation specialist agent"""
        return Agent(
            role='Unit Test Engineering Specialist',
            goal='Generate comprehensive unit tests with maximum code coverage, including edge cases and boundary conditions',
            backstory="""You are a Test-Driven Development (TDD) expert with mastery in multiple programming languages
            and testing frameworks. You have deep understanding of code structure, design patterns, and testing best practices.
            Your unit tests are known for their completeness, maintainability, and ability to catch regression issues early
            in the development cycle.""",
            tools=[
                self.test_gen_tools.code_analyzer,
                self.test_gen_tools.unit_test_generator,
                self.test_gen_tools.coverage_calculator
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_integration_test_agent(self) -> Agent:
        """Create the integration test specialist agent"""
        return Agent(
            role='Integration Test Architecture Specialist',
            goal='Design and generate end-to-end integration tests for complex system interactions and workflows',
            backstory="""You are a Systems Integration Architect with expertise in API testing, service mesh architecture,
            and distributed systems. You understand the complexities of modern microservices architectures and excel at
            creating integration tests that validate system behavior across service boundaries, databases, and external APIs.""",
            tools=[
                self.test_gen_tools.api_analyzer,
                self.test_gen_tools.workflow_mapper,
                self.test_gen_tools.integration_test_generator
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_security_test_agent(self) -> Agent:
        """Create the security testing specialist agent"""
        return Agent(
            role='Security Test Engineering Specialist',
            goal='Generate comprehensive security tests covering OWASP Top 10, penetration testing scenarios, and vulnerability assessments',
            backstory="""You are a Cybersecurity Engineer and Ethical Hacker with expertise in application security testing,
            penetration testing, and secure code review. You are well-versed in OWASP guidelines, common attack vectors,
            and security testing methodologies. Your security tests help prevent vulnerabilities from reaching production.""",
            tools=[
                self.test_gen_tools.owasp_analyzer,
                self.test_gen_tools.vulnerability_test_generator,
                self.test_gen_tools.security_scanner
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_performance_test_agent(self) -> Agent:
        """Create the performance testing specialist agent"""
        return Agent(
            role='Performance Test Engineering Specialist',
            goal='Create comprehensive performance tests including load testing, stress testing, and performance benchmarks',
            backstory="""You are a Performance Engineer with expertise in scalability testing, performance optimization,
            and system capacity planning. You understand performance bottlenecks, resource utilization patterns, and
            user experience metrics. Your performance tests ensure applications can handle expected and peak loads
            while maintaining acceptable response times.""",
            tools=[
                self.test_gen_tools.load_test_generator,
                self.test_gen_tools.benchmark_creator,
                self.test_gen_tools.performance_analyzer
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_ai_validation_agent(self) -> Agent:
        """Create the AI model validation specialist agent with comprehensive metrics"""
        return Agent(
            role='AI Model Test & Validation Specialist',
            goal='Generate comprehensive AI model validation tests using industry-standard metrics including faithfulness, groundedness, accuracy, response time, bias detection, and advanced evaluation frameworks',
            backstory="""You are an ML Engineer and AI Ethics Specialist with deep expertise in AI model validation using 
            frameworks like RAGAS, DeepEval, and industry best practices. You specialize in:
            - Faithfulness and groundedness evaluation for RAG systems
            - Hallucination detection and factual accuracy verification  
            - Bias detection across demographic, cultural, and linguistic dimensions
            - Performance benchmarking including latency, throughput, and efficiency metrics
            - Robustness testing against adversarial inputs and edge cases
            - Multi-modal evaluation for text, code, and conversational AI systems
            Your comprehensive test suites ensure AI systems are reliable, ethical, and production-ready.""",
            tools=[
                # Core RAGAS-inspired metrics
                self.ai_validation_metrics.faithfulness_evaluator,
                self.ai_validation_metrics.answer_relevancy_evaluator,
                self.ai_validation_metrics.groundedness_checker,
                self.ai_validation_metrics.context_precision_evaluator,
                self.ai_validation_metrics.context_recall_evaluator,
                
                # Advanced evaluation metrics
                self.ai_validation_metrics.hallucination_detector,
                self.ai_validation_metrics.answer_correctness_evaluator,
                self.ai_validation_metrics.g_eval_scorer,
                
                # Performance & efficiency
                self.ai_validation_metrics.response_time_analyzer,
                self.ai_validation_metrics.token_efficiency_analyzer,
                self.ai_validation_metrics.memory_usage_profiler,
                
                # Quality & consistency
                self.ai_validation_metrics.consistency_evaluator,
                self.ai_validation_metrics.robustness_tester,
                self.ai_validation_metrics.coherence_analyzer,
                
                # Safety & bias detection
                self.ai_validation_metrics.bias_detector,
                self.ai_validation_metrics.toxicity_classifier,
                self.ai_validation_metrics.fairness_evaluator,
                
                # Advanced testing capabilities
                self.ai_validation_metrics.adversarial_attack_simulator,
                self.ai_validation_metrics.model_drift_detector,
                self.ai_validation_metrics.uncertainty_quantifier
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_edge_case_agent(self) -> Agent:
        """Create the edge case and boundary testing specialist agent"""
        return Agent(
            role='Edge Case & Boundary Test Specialist',
            goal='Identify and generate tests for edge cases, boundary conditions, and unusual system states',
            backstory="""You are an Exploratory Testing Expert with a talent for finding unusual scenarios and edge cases
            that others miss. You have deep understanding of system boundaries, error conditions, and chaos engineering
            principles. Your edge case tests often uncover critical issues that would otherwise be discovered in production.""",
            tools=[
                self.test_gen_tools.boundary_analyzer,
                self.test_gen_tools.edge_case_generator,
                self.test_gen_tools.chaos_test_creator
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_quality_reviewer_agent(self) -> Agent:
        """Create the quality review and validation specialist agent"""
        return Agent(
            role='Quality Assurance Reviewer & Validator',
            goal='Review, score, and validate all generated tests for completeness, effectiveness, and production readiness',
            backstory="""You are a QA Architect and Quality Engineering Leader with expertise in test quality metrics,
            continuous improvement, and quality gate implementation. You have a keen eye for test completeness,
            maintainability, and effectiveness. Your reviews ensure that generated tests meet the highest standards
            before deployment to production environments.""",
            tools=[
                self.quality_tools.test_quality_scorer,
                self.quality_tools.coverage_analyzer,
                self.quality_tools.improvement_recommender
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_test_code_generator_agent(self) -> Agent:
        """Create the Test Code Generator agent"""
        return Agent(
            role="Test Code Generator & Automation Script Creator",
            goal="Generate executable, production-ready test automation scripts in various frameworks (pytest, selenium, etc.)",
            backstory="""You are an expert test automation engineer who specializes in generating 
            production-ready test scripts. You create well-structured, maintainable test code 
            using industry best practices including pytest, selenium, API testing libraries, 
            and performance testing tools. You ensure tests are executable, properly documented, 
            follow coding standards, and include proper setup/teardown procedures.""",
            tools=[],
            llm=self.llm,
            verbose=True
        )
    
    def create_test_executor_agent(self) -> Agent:
        """Create the test execution specialist agent"""
        return Agent(
            role='Test Execution Specialist & Results Analyzer',
            goal='Execute generated tests across all domains and provide comprehensive execution analysis with actionable insights',
            backstory="""You are a Test Execution Expert and Results Analysis Specialist with expertise in test automation,
            CI/CD integration, and execution analytics. You excel at running comprehensive test suites efficiently,
            analyzing execution results, identifying patterns in test failures, and providing actionable recommendations
            for improving test reliability and system quality. Your execution reports are trusted by development teams
            and stakeholders for making critical deployment decisions.""",
            tools=[
                self.execution_tools.test_executor_engine,
                self.execution_tools.result_analyzer,
                self.execution_tools.execution_reporter,
                self.execution_tools.performance_monitor,
                self.execution_tools.failure_analyzer,
                self.execution_tools.parallel_executor
            ],
            llm=self.llm,
            verbose=True
        )
    
    def create_demo_crew(self) -> Crew:
        """Create the demo crew with Story Analyst for user story-based testing"""
        
        # Create all agents for demo/story-based testing
        agents = [
            self.create_qa_orchestrator_agent(),
            self.create_story_analyst_agent(),
            self.create_risk_assessor_agent(),
            self.create_unit_test_agent(),
            self.create_integration_test_agent(),
            self.create_security_test_agent(),
            self.create_performance_test_agent(),
            self.create_ai_validation_agent(),
            self.create_edge_case_agent(),
            self.create_test_code_generator_agent(),
            self.create_test_executor_agent(),
            self.create_quality_reviewer_agent()
        ]
        
        # Define demo tasks
        tasks = self._create_demo_tasks(agents)
        
        return Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,  # Sequential with parallel sub-tasks
            verbose=True,
            memory=True
        )
    
    def create_analysis_crew(self) -> Crew:
        """Create a focused crew for story analysis and risk assessment"""
        
        agents = [
            self.create_qa_orchestrator_agent(),
            self.create_story_analyst_agent(),
            self.create_risk_assessor_agent()
        ]
        
        tasks = [
            Task(
                description="Analyze the user story and extract comprehensive requirements",
                agent=agents[1],  # Story analyst
                expected_output="Structured story analysis with actors, actions, acceptance criteria, and business rules"
            ),
            Task(
                description="Perform comprehensive risk analysis across security, performance, and business domains",
                agent=agents[2],  # Risk assessor
                expected_output="Multi-dimensional risk matrix with prioritized risk categories and mitigation strategies"
            ),
            Task(
                description="Coordinate analysis results and create comprehensive test strategy",
                agent=agents[0],  # QA orchestrator
                expected_output="Integrated analysis results with test generation priorities and strategy recommendations"
            )
        ]
        
        return Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )
    
    def create_comprehensive_crew(self) -> Crew:
        """Backward compatibility: Create demo crew (Story Analyst mode)"""
        return self.create_demo_crew()
    
    def create_real_application_crew(self, application_config: Dict[str, Any]) -> Crew:
        """Create a crew specifically for real application testing with all 11 agents"""
        
        # Create all agents for comprehensive real application testing
        agents = [
            self.create_qa_orchestrator_agent(),
            self.create_application_discovery_agent(),
            self.create_risk_assessor_agent(),
            self.create_unit_test_agent(),
            self.create_integration_test_agent(),
            self.create_security_test_agent(),
            self.create_performance_test_agent(),
            self.create_ai_validation_agent(),
            self.create_edge_case_agent(),
            self.create_test_code_generator_agent(),
            self.create_test_executor_agent(),
            self.create_quality_reviewer_agent()
        ]
        
        # Create tasks specifically for real application testing
        tasks = self._create_real_application_tasks(agents, application_config)
        
        return Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            max_rpm=10  # Rate limiting for respectful testing
        )
    
    def _create_demo_tasks(self, agents: List[Agent]) -> List[Task]:
        """Create demo task definitions for story-based testing"""
        
        qa_orchestrator, story_analyst, risk_assessor, unit_agent, integration_agent, \
        security_agent, performance_agent, ai_validation_agent, edge_case_agent, test_executor, quality_reviewer = agents
        
        return [
            # Phase 1: Story Analysis and Requirements
            Task(
                description="""Analyze the provided user story and extract comprehensive requirements including:
                - User roles and personas
                - Core functionality and actions
                - Acceptance criteria and business rules
                - Data entities and relationships
                - System integrations and dependencies
                
                Provide a structured analysis that will guide test generation across all domains.""",
                agent=story_analyst,
                expected_output="Structured story analysis with all testable components identified, including actors, actions, acceptance criteria, and business rules"
            ),
            
            Task(
                description="""Perform comprehensive risk analysis to identify:
                - Security vulnerabilities and attack vectors
                - Performance bottlenecks and scalability concerns
                - Business continuity and compliance risks
                - Technical complexity and integration challenges
                Create a prioritized risk matrix to guide test focus areas.""",
                agent=risk_assessor,
                expected_output="Multi-dimensional risk assessment with priority rankings and mitigation strategies"
            ),
            
            # Phase 2: Test Generation
            Task(
                description="""Generate comprehensive unit tests including:
                - Happy path scenarios with valid inputs
                - Input validation and boundary value testing
                - Error handling and exception scenarios
                - State transition and workflow testing
                - Mock and stub implementations for dependencies
                Ensure 95%+ code coverage with meaningful assertions.""",
                agent=unit_agent,
                expected_output="Complete unit test suite with comprehensive coverage and edge cases"
            ),
            
            Task(
                description="""Create end-to-end integration tests covering:
                - API endpoint testing with various payloads
                - Database integration and transaction testing
                - External service integration and fallback scenarios
                - Workflow validation across system boundaries
                - Data consistency and integrity verification""",
                agent=integration_agent,
                expected_output="Integration test suite validating all system interactions"
            ),
            
            Task(
                description="""Generate security tests addressing:
                - OWASP Top 10 vulnerabilities
                - Authentication and authorization testing
                - Input sanitization and injection prevention
                - Data exposure and privacy protection
                - Session management and CSRF protection
                Include both automated tests and manual testing procedures.""",
                agent=security_agent,
                expected_output="Comprehensive security test suite with vulnerability assessments"
            ),
            
            Task(
                description="""Create performance testing scenarios including:
                - Load testing for expected user volumes
                - Stress testing for peak and beyond-peak loads
                - Spike testing for sudden traffic increases
                - Volume testing for large data sets
                - Memory and resource utilization monitoring
                Include performance benchmarks and SLA validation.""",
                agent=performance_agent,
                expected_output="Performance test suite with benchmarks and load scenarios"
            ),
            
            Task(
                description="""Generate comprehensive AI model validation tests using industry-standard metrics and frameworks:
                
                🎯 ACCURACY & FAITHFULNESS METRICS:
                - Faithfulness evaluation using chain-of-verification techniques
                - Groundedness checking to ensure responses are context-based
                - Factual accuracy verification against knowledge bases
                - Answer correctness combining semantic and factual dimensions
                
                📊 RAGAS-INSPIRED METRICS:
                - Answer relevancy evaluation using semantic similarity
                - Context precision measurement for RAG systems
                - Context recall assessment against ground truth
                - Hallucination detection using multiple verification methods
                
                ⚡ PERFORMANCE & EFFICIENCY METRICS:
                - Response time analysis across various input lengths
                - Token efficiency and cost optimization analysis
                - Memory usage profiling during inference
                - Throughput benchmarking under load conditions
                
                🔍 QUALITY & CONSISTENCY METRICS:
                - Output consistency testing across multiple runs
                - Robustness evaluation against input variations
                - Coherence analysis for logical flow
                - Semantic similarity scoring using BERTScore and embeddings
                
                🛡️ SAFETY & BIAS DETECTION:
                - Comprehensive bias detection (demographic, cultural, linguistic)
                - Toxicity classification and harmful content detection
                - Fairness evaluation using statistical parity metrics
                - Adversarial attack simulation and resistance testing
                
                🧪 ADVANCED EVALUATION CAPABILITIES:
                - G-Eval scoring using LLM-based evaluation
                - Model drift detection over time
                - Uncertainty quantification for decision confidence
                - Multi-turn conversation evaluation
                - Instruction following assessment
                
                Include automated testing pipelines, evaluation dashboards, and detailed reporting with actionable insights.""",
                agent=ai_validation_agent,
                expected_output="Comprehensive AI validation test suite with 25+ metrics covering accuracy, faithfulness, groundedness, performance, safety, and advanced evaluation capabilities"
            ),
            
            Task(
                description="""Identify and generate edge case tests for:
                - Boundary value conditions and limits
                - Null, empty, and invalid input scenarios
                - Concurrent access and race conditions
                - System resource exhaustion scenarios
                - Network failures and timeout conditions
                Focus on scenarios that are often missed in standard testing.""",
                agent=edge_case_agent,
                expected_output="Edge case test suite covering boundary conditions and stress scenarios"
            ),
            
            # Phase 3: Test Execution and Results Analysis
            Task(
                description="""Execute the generated comprehensive test suite and provide detailed analysis:
                - Run all generated tests across all domains (unit, integration, security, performance, AI validation, edge cases)
                - Monitor execution performance and resource utilization
                - Analyze test results and identify patterns in failures
                - Generate comprehensive execution reports with metrics
                - Provide root cause analysis for any test failures
                - Calculate coverage metrics and identify gaps
                - Assess execution efficiency and recommend optimizations
                - Validate test environment readiness and configuration
                Create actionable insights for development teams and stakeholders.""",
                agent=test_executor,
                expected_output="Complete test execution results with detailed analysis, metrics, and actionable recommendations"
            ),
            
            # Phase 4: Quality Review and Validation
            Task(
                description="""Review all generated tests and provide:
                - Quality scores for each test domain
                - Coverage analysis and gap identification
                - Test effectiveness and maintainability assessment
                - Production readiness evaluation
                - Improvement recommendations and next steps
                Ensure all tests meet enterprise quality standards.""",
                agent=quality_reviewer,
                expected_output="Comprehensive quality assessment with scores, gaps, and recommendations"
            ),
            
            # Phase 5: Final Orchestration
            Task(
                description="""Coordinate all test generation results and create:
                - Integrated test execution plan
                - CI/CD pipeline integration specifications
                - Quality gate configurations
                - Monitoring and alerting setup
                - Executive summary with key metrics and achievements
                Ensure seamless integration with existing development workflows.""",
                agent=qa_orchestrator,
                expected_output="Complete test ecosystem with integration specifications and executive summary"
            )
        ]
    
    def _create_real_application_tasks(self, agents: List[Agent], app_config: Dict[str, Any]) -> List[Task]:
        """Create tasks specifically designed for real application testing"""
        
        qa_orchestrator, discovery_agent, risk_assessor, unit_agent, integration_agent, \
        security_agent, performance_agent, ai_validation_agent, edge_case_agent, test_executor, quality_reviewer = agents
        
        base_url = app_config.get('urls', {}).get('base_url', 'https://www.google.com')
        app_name = app_config.get('application', {}).get('name', 'Web Application')
        app_type = app_config.get('application', {}).get('type', 'web')
        
        return [
            # Phase 1: Application Discovery
            self.discovery_agent.create_discovery_task(app_config),
            
            # Phase 2: Risk Assessment based on discovered features
            Task(
                description=f"""Analyze the discovered application features and assess risks for {app_name}:
                - Review the application discovery report from the previous phase
                - Identify security vulnerabilities based on discovered elements and workflows
                - Assess performance risks and scalability concerns from actual application structure
                - Evaluate business continuity risks from critical user journeys
                - Create prioritized risk matrix focusing on real discovered features
                
                Focus on risks identified from actual application exploration, not theoretical concerns.""",
                agent=risk_assessor,
                expected_output="Risk assessment report prioritizing real discovered vulnerabilities and performance concerns"
            ),
            
            # Phase 3: Test Generation based on discovered features
            Task(
                description="""Generate comprehensive unit tests based on discovered application components:
                - Use the application discovery report to identify testable components
                - Create unit tests for discovered JavaScript functions, forms, and interactions
                - Generate tests for input validation based on discovered form elements
                - Create mock tests for identified API calls and integrations
                - Focus on components actually discovered in the application exploration
                
                Generate executable test code that can be run against the real application.""",
                agent=unit_agent,
                expected_output="Unit test suite based on discovered application components"
            ),
            
            Task(
                description="""Generate integration tests for discovered application workflows:
                - Create end-to-end tests for discovered user journeys
                - Generate API integration tests for discovered endpoints
                - Create cross-browser compatibility tests for discovered UI elements
                - Build data flow tests for discovered form submissions and interactions
                
                Focus on real discovered workflows and integration points.""",
                agent=integration_agent,
                expected_output="Integration test suite covering discovered workflows and API endpoints"
            ),
            
            Task(
                description=f"""Generate security tests based on discovered application features:
                - Create security tests for discovered form inputs and validation
                - Generate authentication and authorization tests for discovered protected areas
                - Build XSS and injection tests for discovered input fields
                - Create CSRF tests for discovered form submissions
                - Perform passive security scanning of discovered endpoints
                
                Use respectful testing practices appropriate for {app_type} applications.""",
                agent=security_agent,
                expected_output="Security test suite targeting discovered attack surfaces"
            ),
            
            Task(
                description=f"""Generate performance tests for discovered application features:
                - Create load tests for discovered critical user journeys
                - Generate performance benchmarks for discovered page loads
                - Build Core Web Vitals tests for discovered UI interactions
                - Create stress tests for discovered form submissions and searches
                - Monitor resource usage during discovered workflow execution
                
                Focus on performance testing of real discovered features and user paths.""",
                agent=performance_agent,
                expected_output="Performance test suite for discovered application workflows"
            ),
            
            Task(
                description=f"""Generate AI validation tests for discovered intelligent features:
                - Test search intelligence and relevance for discovered search functionality
                - Validate autocomplete and suggestion quality for discovered input fields
                - Assess user experience AI features discovered during exploration
                - Test accessibility AI features discovered in the application
                - Validate any ML-powered features discovered during browsing
                
                Focus on AI-powered features actually discovered in the application.""",
                agent=ai_validation_agent,
                expected_output="AI validation test suite for discovered intelligent features"
            ),
            
            Task(
                description="""Generate edge case tests for discovered application boundaries:
                - Create boundary tests for discovered input fields and limits
                - Generate error handling tests for discovered failure scenarios
                - Build concurrency tests for discovered interactive elements
                - Create data edge case tests for discovered form validations
                - Generate browser compatibility tests for discovered UI components
                
                Focus on edge cases derived from actual discovered application behavior.""",
                agent=edge_case_agent,
                expected_output="Edge case test suite targeting discovered application boundaries"
            ),
            
            Task(
                description=f"""Execute all generated tests against the real application at {base_url}:
                - Run all generated test suites against the actual application
                - Execute browser automation tests in headless mode
                - Perform API testing against discovered endpoints
                - Run security tests using passive scanning techniques
                - Execute performance tests with appropriate load levels
                - Collect comprehensive test results and metrics
                
                Ensure respectful testing practices and rate limiting.""",
                agent=test_executor,
                expected_output="Complete test execution results with detailed metrics and findings"
            ),
            
            Task(
                description="""Review and score all test results for quality and completeness:
                - Analyze test execution results across all domains
                - Score test coverage based on discovered application features
                - Evaluate test effectiveness and reliability
                - Generate comprehensive quality assessment
                - Provide recommendations for test improvement and additional coverage
                - Create executive summary with actionable insights
                
                Focus quality assessment on real discovered features and actual test results.""",
                agent=quality_reviewer,
                expected_output="Comprehensive quality report with scores, analysis, and actionable recommendations for the real application"
            )
        ]