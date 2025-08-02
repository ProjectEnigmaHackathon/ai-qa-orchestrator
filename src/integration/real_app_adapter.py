"""
Real Application Adapter
Integrates the AI QA Orchestrator with real applications using configuration
"""

import yaml
import asyncio
from typing import Dict, List, Any, Optional
import os
from pathlib import Path

from integration.real_app_testing import RealApplicationTester
from orchestration.qa_orchestrator import QAOrchestrationEngine
from utils.demo_data import MockResults


class RealAppAdapter:
    """Adapter to connect AI QA Orchestrator with real applications"""
    
    def __init__(self, config_path: str = "config/app_config.yml"):
        self.config_path = config_path
        self.config = self._load_config()
        self.app_tester = RealApplicationTester(self.config)
        self.orchestrator = QAOrchestrationEngine()
        self.mock_results = MockResults()
    
    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> 'RealAppAdapter':
        """Create adapter from configuration dictionary (no file needed)"""
        instance = cls.__new__(cls)
        instance.config_path = None  # No file path since using dict config
        instance.config = config
        instance.app_tester = RealApplicationTester(instance.config)
        instance.orchestrator = QAOrchestrationEngine()
        instance.mock_results = MockResults()
        return instance
        
    def _load_config(self) -> Dict[str, Any]:
        """Load application configuration from YAML file"""
        
        try:
            with open(self.config_path, 'r') as file:
                config = yaml.safe_load(file)
                return config
        except FileNotFoundError:
            print(f"Config file not found: {self.config_path}")
            print("Using default configuration...")
            return self._get_default_config()
        except yaml.YAMLError as e:
            print(f"Error parsing config file: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration for when config file is missing"""
        
        return {
            'application': {
                'name': 'Default App',
                'type': 'web',
                'language': 'javascript',
                'framework': 'react'
            },
            'urls': {
                'base_url': 'http://localhost:3000',
                'api_base_url': 'http://localhost:3001/api'
            },
            'testing_tools': {
                'unit_testing': {'framework': 'jest'},
                'api_testing': {'tool': 'requests'},
                'security_testing': {'tools': ['manual']},
                'performance_testing': {'tool': 'basic'}
            },
            'quality_gates': {
                'unit_test_coverage': 80,
                'api_test_pass_rate': 100,
                'security_critical_issues': 0
            }
        }
    
    async def setup_real_testing_environment(self) -> Dict[str, Any]:
        """Setup the testing environment for real application testing"""
        
        print("🔧 Setting up real application testing environment...")
        
        # Setup test environment
        env_setup = await self.app_tester.setup_test_environment()
        
        # Validate configuration
        config_validation = self._validate_configuration()
        
        # Check required tools
        tools_check = await self._check_required_tools()
        
        setup_status = {
            'environment_setup': env_setup,
            'configuration_valid': config_validation,
            'required_tools': tools_check,
            'ready_for_testing': all([
                env_setup.get('environment_ready', False),
                config_validation.get('valid', False),
                tools_check.get('all_available', False)
            ])
        }
        
        if setup_status['ready_for_testing']:
            print("✅ Real application testing environment is ready!")
        else:
            print("⚠️  Some setup issues detected. Check the detailed status.")
            
        return setup_status
    
    async def execute_comprehensive_real_testing(self, user_story: str) -> Dict[str, Any]:
        """Execute comprehensive testing on the real application"""
        
        print("🚀 Starting comprehensive real application testing...")
        
        # Phase 1: Generate tests using AI Orchestrator (same as before)
        print("📝 Phase 1: Generating comprehensive test suite...")
        generated_tests = await self.orchestrator.orchestrate_comprehensive_testing(user_story)
        
        # Phase 2: Execute real tests
        print("🔄 Phase 2: Executing tests on real application...")
        real_execution_results = await self._execute_real_tests(generated_tests)
        
        # Phase 3: Combine and analyze results
        print("📊 Phase 3: Analyzing results and generating reports...")
        comprehensive_results = await self._combine_results(generated_tests, real_execution_results)
        
        # Phase 4: Validate against quality gates
        print("🚪 Phase 4: Validating against quality gates...")
        quality_gate_results = await self._validate_quality_gates(comprehensive_results)
        
        final_results = {
            'user_story': user_story,
            'generated_tests': generated_tests,
            'real_execution_results': real_execution_results,
            'comprehensive_analysis': comprehensive_results,
            'quality_gate_validation': quality_gate_results,
            'testing_mode': 'real_application',
            'timestamp': asyncio.get_event_loop().time()
        }
        
        print("✅ Comprehensive real application testing completed!")
        return final_results
    
    async def _execute_real_tests(self, generated_tests: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the generated tests on the real application"""
        
        execution_results = {}
        
        # Execute different types of tests based on configuration
        if self._should_run_unit_tests():
            print("  🧪 Running unit tests...")
            execution_results['unit_tests'] = await self.app_tester.execute_real_unit_tests(
                generated_tests.get('generated_tests', {}).get('unit_tests', '')
            )
        
        if self._should_run_api_tests():
            print("  🔗 Running API tests...")
            execution_results['api_tests'] = await self.app_tester.execute_real_api_tests(
                generated_tests.get('generated_tests', {}).get('integration_tests', '')
            )
        
        if self._should_run_ui_tests():
            print("  🖥️  Running UI tests...")
            execution_results['ui_tests'] = await self.app_tester.execute_real_ui_tests(
                generated_tests.get('generated_tests', {}).get('ui_tests', '')
            )
        
        if self._should_run_security_tests():
            print("  🔒 Running security tests...")
            execution_results['security_tests'] = await self.app_tester.execute_real_security_tests(
                generated_tests.get('generated_tests', {}).get('security_tests', '')
            )
        
        if self._should_run_performance_tests():
            print("  ⚡ Running performance tests...")
            execution_results['performance_tests'] = await self.app_tester.execute_real_performance_tests(
                generated_tests.get('generated_tests', {}).get('performance_tests', '')
            )
        
        # Generate real coverage report
        print("  📊 Generating coverage report...")
        execution_results['coverage_report'] = await self.app_tester.generate_real_coverage_report()
        
        return execution_results
    
    async def _combine_results(self, generated_tests: Dict[str, Any], real_results: Dict[str, Any]) -> Dict[str, Any]:
        """Combine generated test data with real execution results"""
        
        combined_results = {
            'test_generation_summary': {
                'tests_generated': True,
                'domains_covered': len(generated_tests.get('generated_tests', {})),
                'ai_agents_used': 11,
                'generation_time': generated_tests.get('execution_summary', {}).get('execution_time_seconds', 0)
            },
            'real_execution_summary': {
                'tests_executed': len([k for k, v in real_results.items() if v.get('real_execution', False)]),
                'total_test_count': sum([v.get('total_tests', 0) for v in real_results.values() if isinstance(v, dict)]),
                'overall_pass_rate': self._calculate_overall_pass_rate(real_results),
                'execution_time': sum([v.get('execution_time', 0) for v in real_results.values() if isinstance(v, dict)])
            },
            'detailed_results': real_results,
            'quality_metrics': {
                'code_coverage': real_results.get('coverage_report', {}).get('statement_coverage', 0),
                'security_score': real_results.get('security_tests', {}).get('security_score', 100),
                'performance_score': real_results.get('performance_tests', {}).get('performance_score', 85),
                'overall_quality_score': self._calculate_overall_quality_score(real_results)
            },
            'recommendations': self._generate_recommendations(real_results),
            'next_actions': self._suggest_next_actions(real_results)
        }
        
        return combined_results
    
    async def _validate_quality_gates(self, comprehensive_results: Dict[str, Any]) -> Dict[str, Any]:
        """Validate results against configured quality gates"""
        
        quality_gates = self.config.get('quality_gates', {})
        quality_metrics = comprehensive_results.get('quality_metrics', {})
        
        gate_results = {}
        overall_pass = True
        
        # Unit test coverage gate
        coverage_threshold = quality_gates.get('unit_test_coverage', 80)
        actual_coverage = quality_metrics.get('code_coverage', 0)
        coverage_pass = actual_coverage >= coverage_threshold
        gate_results['unit_test_coverage'] = {
            'threshold': coverage_threshold,
            'actual': actual_coverage,
            'pass': coverage_pass
        }
        overall_pass = overall_pass and coverage_pass
        
        # API test pass rate gate
        api_pass_threshold = quality_gates.get('api_test_pass_rate', 100)
        api_results = comprehensive_results.get('detailed_results', {}).get('api_tests', {})
        api_pass_rate = api_results.get('success_rate', 100)
        api_gate_pass = api_pass_rate >= api_pass_threshold
        gate_results['api_test_pass_rate'] = {
            'threshold': api_pass_threshold,
            'actual': api_pass_rate,
            'pass': api_gate_pass
        }
        overall_pass = overall_pass and api_gate_pass
        
        # Security gates
        security_critical_threshold = quality_gates.get('security_critical_issues', 0)
        security_results = comprehensive_results.get('detailed_results', {}).get('security_tests', {})
        critical_issues = security_results.get('critical_issues', 0)
        security_gate_pass = critical_issues <= security_critical_threshold
        gate_results['security_critical_issues'] = {
            'threshold': security_critical_threshold,
            'actual': critical_issues,
            'pass': security_gate_pass
        }
        overall_pass = overall_pass and security_gate_pass
        
        # Performance gate
        performance_threshold = quality_gates.get('performance_p95_response_time', 2000)
        performance_results = comprehensive_results.get('detailed_results', {}).get('performance_tests', {})
        p95_response_time = performance_results.get('response_times', {}).get('p95', '1000ms')
        p95_value = int(p95_response_time.replace('ms', '')) if isinstance(p95_response_time, str) else p95_response_time
        performance_gate_pass = p95_value <= performance_threshold
        gate_results['performance_p95_response_time'] = {
            'threshold': f"{performance_threshold}ms",
            'actual': f"{p95_value}ms",
            'pass': performance_gate_pass
        }
        overall_pass = overall_pass and performance_gate_pass
        
        return {
            'overall_pass': overall_pass,
            'individual_gates': gate_results,
            'deployment_recommendation': 'PROCEED' if overall_pass else 'BLOCK',
            'summary': f"{'✅ All quality gates passed' if overall_pass else '❌ Some quality gates failed'}"
        }
    
    def _validate_configuration(self) -> Dict[str, Any]:
        """Validate the loaded configuration"""
        
        validation_results = {
            'valid': True,
            'issues': [],
            'warnings': []
        }
        
        required_sections = ['application', 'urls', 'testing_tools']
        for section in required_sections:
            if section not in self.config:
                validation_results['valid'] = False
                validation_results['issues'].append(f"Missing required section: {section}")
        
        # Validate URLs
        urls = self.config.get('urls', {})
        if not urls.get('base_url'):
            validation_results['warnings'].append("No base_url specified")
        
        return validation_results
    
    async def _check_required_tools(self) -> Dict[str, Any]:
        """Check if required testing tools are available"""
        
        tools_status = {
            'all_available': True,
            'available_tools': [],
            'missing_tools': []
        }
        
        testing_tools = self.config.get('testing_tools', {})
        
        # Check unit testing framework
        unit_framework = testing_tools.get('unit_testing', {}).get('framework', 'jest')
        if await self._check_tool_availability(unit_framework):
            tools_status['available_tools'].append(unit_framework)
        else:
            tools_status['missing_tools'].append(unit_framework)
            tools_status['all_available'] = False
        
        # Check other tools similarly...
        
        return tools_status
    
    async def _check_tool_availability(self, tool_name: str) -> bool:
        """Check if a specific tool is available"""
        
        try:
            import subprocess
            result = subprocess.run([tool_name, '--help'], 
                                  capture_output=True, timeout=5)
            return result.returncode == 0
        except:
            return False
    
    def _should_run_unit_tests(self) -> bool:
        """Check if unit tests should be run"""
        testing_config = self.config.get('testing_tools', {})
        return 'unit_testing' in testing_config
    
    def _should_run_api_tests(self) -> bool:
        """Check if API tests should be run"""
        return self.config.get('api', {}) and self.config.get('urls', {}).get('api_base_url')
    
    def _should_run_ui_tests(self) -> bool:
        """Check if UI tests should be run"""
        app_type = self.config.get('application', {}).get('type', '')
        return app_type in ['web', 'ui'] and self.config.get('ui', {})
    
    def _should_run_security_tests(self) -> bool:
        """Check if security tests should be run"""
        testing_config = self.config.get('testing_tools', {})
        return 'security_testing' in testing_config
    
    def _should_run_performance_tests(self) -> bool:
        """Check if performance tests should be run"""
        testing_config = self.config.get('testing_tools', {})
        return 'performance_testing' in testing_config
    
    def _calculate_overall_pass_rate(self, results: Dict[str, Any]) -> float:
        """Calculate overall pass rate from all test results"""
        
        total_tests = 0
        passed_tests = 0
        
        for test_type, result in results.items():
            if isinstance(result, dict) and 'total_tests' in result:
                total_tests += result.get('total_tests', 0)
                passed_tests += result.get('passed', 0)
        
        return (passed_tests / total_tests * 100) if total_tests > 0 else 0
    
    def _calculate_overall_quality_score(self, results: Dict[str, Any]) -> float:
        """Calculate overall quality score"""
        
        # Weighted quality calculation
        weights = {
            'coverage': 0.3,
            'security': 0.25,
            'performance': 0.2,
            'functionality': 0.25
        }
        
        coverage_score = results.get('coverage_report', {}).get('statement_coverage', 0)
        security_score = results.get('security_tests', {}).get('security_score', 100)
        performance_score = results.get('performance_tests', {}).get('performance_score', 85)
        functionality_score = self._calculate_overall_pass_rate(results)
        
        overall_score = (
            coverage_score * weights['coverage'] +
            security_score * weights['security'] +
            performance_score * weights['performance'] +
            functionality_score * weights['functionality']
        )
        
        return round(overall_score, 2)
    
    def _generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on test results"""
        
        recommendations = []
        
        # Coverage recommendations
        coverage = results.get('coverage_report', {}).get('statement_coverage', 0)
        if coverage < 80:
            recommendations.append(f"Increase code coverage from {coverage:.1f}% to at least 80%")
        
        # Security recommendations
        security_results = results.get('security_tests', {})
        if security_results.get('vulnerabilities_found', 0) > 0:
            recommendations.append("Address security vulnerabilities found during testing")
        
        # Performance recommendations
        performance_results = results.get('performance_tests', {})
        if performance_results.get('performance_score', 100) < 85:
            recommendations.append("Optimize application performance based on test results")
        
        # API recommendations
        api_results = results.get('api_tests', {})
        if api_results.get('success_rate', 100) < 95:
            recommendations.append("Investigate and fix failing API tests")
        
        return recommendations
    
    def _suggest_next_actions(self, results: Dict[str, Any]) -> List[str]:
        """Suggest next actions based on results"""
        
        actions = []
        
        # Check for critical issues
        security_results = results.get('security_tests', {})
        if security_results.get('critical_issues', 0) > 0:
            actions.append("URGENT: Fix critical security vulnerabilities before deployment")
        
        # Check for test failures
        overall_pass_rate = self._calculate_overall_pass_rate(results)
        if overall_pass_rate < 95:
            actions.append("Review and fix failing tests before proceeding")
        
        # Standard actions
        actions.extend([
            "Review detailed test reports for insights",
            "Update test cases based on findings",
            "Schedule follow-up testing after fixes",
            "Consider deployment to staging environment"
        ])
        
        return actions
    
    def get_configuration_template(self) -> str:
        """Return configuration template for user's application"""
        
        return """
# Quick Configuration Guide for Your Application

1. **Update Application Details:**
   - Set your application type (web, api, mobile, etc.)
   - Specify programming language and framework
   - Configure your application URLs

2. **Configure API Testing:**
   - List your API endpoints
   - Set up authentication details
   - Define test data and expected responses

3. **Set Up UI Testing:**
   - Define critical user flows
   - Configure browser settings
   - Specify elements to test

4. **Configure Quality Gates:**
   - Set minimum coverage thresholds
   - Define acceptable performance metrics
   - Configure security requirements

5. **Choose Testing Tools:**
   - Select unit testing framework
   - Choose API testing tools
   - Configure security scanning tools

See config/app_config.yml for detailed configuration options.
        """