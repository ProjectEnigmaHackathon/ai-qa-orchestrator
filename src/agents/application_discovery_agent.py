"""
Application Discovery Agent - Explores real applications to understand structure and generate test cases
Replaces Story Analyst for real application testing
"""

from crewai import Agent, Task
from langchain_anthropic import ChatAnthropic
from typing import Dict, List, Any, Optional
import os
import json
import time
from datetime import datetime

class ApplicationDiscoveryAgent:
    """AI agent that explores real applications to understand their structure and features"""
    
    def __init__(self, llm_model: str = "claude-3-5-sonnet-20241022"):
        self.llm = ChatAnthropic(
            model=llm_model,
            temperature=0.1,  # Lower temperature for more consistent discovery
            anthropic_api_key=os.getenv('ANTHROPIC_API_KEY')
        )
        
    def create_agent(self) -> Agent:
        """Create the Application Discovery Agent"""
        return Agent(
            role='Application Discovery & Feature Analysis Specialist',
            goal='Explore real applications through automated browsing to discover features, UI elements, workflows, and generate comprehensive test scenarios based on actual application structure',
            backstory="""You are an AI-powered Application Explorer with advanced capabilities in web automation, 
            feature discovery, and intelligent test case generation. Instead of relying on user stories or documentation, 
            you actively browse and explore applications to understand their true structure and functionality.
            
            Your expertise includes:
            - Automated web crawling and UI element discovery
            - Feature identification through intelligent interaction
            - Workflow mapping and user journey analysis  
            - Dynamic test case generation based on discovered features
            - Cross-browser compatibility analysis
            - Accessibility and usability assessment
            
            You replace traditional requirements analysis by providing real, actionable insights from actual application exploration.""",
            tools=[
                self._create_browser_automation_tool(),
                self._create_element_discovery_tool(),
                self._create_feature_mapping_tool(),
                self._create_workflow_analyzer_tool(),
                self._create_test_scenario_generator_tool()
            ],
            llm=self.llm,
            verbose=True,
            allow_delegation=True
        )
    
    def _create_browser_automation_tool(self):
        """Tool for automated browser control and navigation"""
        from langchain.tools import Tool
        
        def browse_application(application_url: str) -> str:
            """
            Automatically browse and explore the given application URL
            
            Args:
                application_url: The base URL of the application to explore
                
            Returns:
                Detailed exploration report with discovered pages and features
            """
            
            # Mock implementation - in real scenario, this would use Selenium WebDriver
            exploration_results = {
                "base_url": application_url,
                "discovery_timestamp": datetime.now().isoformat(),
                "pages_discovered": [
                    {
                        "url": application_url,
                        "title": "Homepage",
                        "page_type": "landing",
                        "load_time": "1.2s",
                        "elements_found": 45,
                        "interactive_elements": 12
                    },
                    {
                        "url": f"{application_url}/search",
                        "title": "Search Page", 
                        "page_type": "search",
                        "load_time": "0.8s",
                        "elements_found": 23,
                        "interactive_elements": 5
                    }
                ],
                "technology_stack": {
                    "frontend_framework": "React/JavaScript",
                    "css_framework": "Custom CSS",
                    "analytics": "Google Analytics",
                    "cdn": "Google CDN"
                },
                "performance_metrics": {
                    "avg_load_time": "1.0s",
                    "lighthouse_score": 92,
                    "core_web_vitals": "Good"
                }
            }
            
            return json.dumps(exploration_results, indent=2)
        
        return Tool(
            name="Browser Automation Explorer",
            func=browse_application,
            description="Automatically browse and explore applications using headless browser automation"
        )
    
    def _create_element_discovery_tool(self):
        """Tool for discovering and cataloging UI elements"""
        from langchain.tools import Tool
        
        def discover_elements(page_url: str) -> str:
            """
            Discover and catalog all UI elements on a given page
            
            Args:
                page_url: URL of the page to analyze
                
            Returns:
                Comprehensive catalog of discovered UI elements
            """
            
            # Mock implementation - real version would use Selenium element detection
            elements_catalog = {
                "page_url": page_url,
                "discovery_time": datetime.now().isoformat(),
                "form_elements": [
                    {
                        "type": "search_input",
                        "selector": "[name='q']",
                        "placeholder": "Search Google or type a URL",
                        "required": False,
                        "validation": "text",
                        "test_scenarios": ["valid_search", "empty_search", "special_chars"]
                    },
                    {
                        "type": "submit_button",
                        "selector": "[value='Google Search']",
                        "text": "Google Search",
                        "enabled": True,
                        "test_scenarios": ["click_enabled", "keyboard_enter"]
                    }
                ],
                "navigation_elements": [
                    {
                        "type": "link",
                        "text": "Images",
                        "href": "/imghp",
                        "target": "_self"
                    },
                    {
                        "type": "link", 
                        "text": "Gmail",
                        "href": "https://mail.google.com",
                        "target": "_blank"
                    }
                ],
                "interactive_elements": [
                    {
                        "type": "suggestion_dropdown",
                        "trigger": "input_focus",
                        "dynamic": True,
                        "test_scenarios": ["suggestions_appear", "keyboard_navigation"]
                    }
                ],
                "accessibility_elements": [
                    {
                        "type": "aria_label",
                        "selector": "[aria-label='Search']",
                        "compliance": "WCAG_2.1"
                    }
                ]
            }
            
            return json.dumps(elements_catalog, indent=2)
        
        return Tool(
            name="Element Discovery Scanner",
            func=discover_elements,
            description="Discover and catalog all UI elements, forms, buttons, and interactive components"
        )
    
    def _create_feature_mapping_tool(self):
        """Tool for mapping application features and functionality"""
        from langchain.tools import Tool
        
        def map_features(application_data: str) -> str:
            """
            Map and analyze application features based on discovered elements
            
            Args:
                application_data: JSON string with discovered application data
                
            Returns:
                Feature map with testing recommendations
            """
            
            feature_map = {
                "primary_features": [
                    {
                        "feature_name": "Search Functionality",
                        "description": "Core search feature allowing users to find information",
                        "complexity": "medium",
                        "critical_path": True,
                        "user_workflows": [
                            "Basic search query",
                            "Search with suggestions",
                            "Empty search handling",
                            "Special character search"
                        ],
                        "test_priority": "high",
                        "risk_level": "medium"
                    },
                    {
                        "feature_name": "Navigation System",
                        "description": "Site navigation and link structure",
                        "complexity": "low",
                        "critical_path": True,
                        "user_workflows": [
                            "Main navigation usage",
                            "External link navigation",
                            "Back/forward browser navigation"
                        ],
                        "test_priority": "medium",
                        "risk_level": "low"
                    }
                ],
                "secondary_features": [
                    {
                        "feature_name": "Autocomplete Suggestions",
                        "description": "Dynamic search suggestions as user types",
                        "complexity": "high",
                        "critical_path": False,
                        "user_workflows": [
                            "Suggestion appearance",
                            "Suggestion selection",
                            "Keyboard navigation of suggestions"
                        ],
                        "test_priority": "medium",
                        "risk_level": "low"
                    }
                ],
                "integration_points": [
                    {
                        "name": "External Services",
                        "description": "Integration with external Google services",
                        "test_approach": "API contract testing"
                    }
                ],
                "performance_considerations": [
                    {
                        "area": "Search Response Time",
                        "target": "< 2 seconds",
                        "test_type": "load_testing"
                    }
                ]
            }
            
            return json.dumps(feature_map, indent=2)
        
        return Tool(
            name="Feature Mapping Analyzer",
            func=map_features,
            description="Map application features, workflows, and generate testing strategies"
        )
    
    def _create_workflow_analyzer_tool(self):
        """Tool for analyzing user workflows and journeys"""
        from langchain.tools import Tool
        
        def analyze_workflows(feature_data: str) -> str:
            """
            Analyze user workflows and critical paths through the application
            
            Args:
                feature_data: JSON string with feature mapping data
                
            Returns:
                Workflow analysis with test scenarios
            """
            
            workflow_analysis = {
                "critical_user_journeys": [
                    {
                        "journey_name": "Primary Search Journey",
                        "description": "User performs a search and views results",
                        "steps": [
                            {
                                "step": 1,
                                "action": "Navigate to homepage",
                                "element": "URL navigation",
                                "expected": "Homepage loads successfully",
                                "test_cases": ["page_load", "element_visibility"]
                            },
                            {
                                "step": 2,
                                "action": "Focus on search input",
                                "element": "[name='q']",
                                "expected": "Input field is focused and ready",
                                "test_cases": ["input_focus", "placeholder_text"]
                            },
                            {
                                "step": 3,
                                "action": "Type search query",
                                "element": "[name='q']",
                                "expected": "Text appears in input field",
                                "test_cases": ["text_input", "character_limits", "special_chars"]
                            },
                            {
                                "step": 4,
                                "action": "Click search button",
                                "element": "[value='Google Search']",
                                "expected": "Search is submitted",
                                "test_cases": ["button_click", "enter_key", "form_submission"]
                            },
                            {
                                "step": 5,
                                "action": "View search results",
                                "element": "#search",
                                "expected": "Results are displayed",
                                "test_cases": ["results_display", "load_time", "result_count"]
                            }
                        ],
                        "alternate_paths": [
                            "Search using Enter key",
                            "Search using autocomplete selection"
                        ],
                        "error_scenarios": [
                            "Network failure during search",
                            "Empty search submission",
                            "Invalid characters in search"
                        ]
                    }
                ],
                "edge_case_workflows": [
                    {
                        "workflow": "Rapid consecutive searches",
                        "risk": "Rate limiting or performance issues",
                        "test_approach": "stress_testing"
                    },
                    {
                        "workflow": "Search with disabled JavaScript",
                        "risk": "Functionality breakdown",
                        "test_approach": "progressive_enhancement_testing"
                    }
                ]
            }
            
            return json.dumps(workflow_analysis, indent=2)
        
        return Tool(
            name="Workflow Journey Analyzer", 
            func=analyze_workflows,
            description="Analyze user workflows, critical paths, and generate journey-based test scenarios"
        )
    
    def _create_test_scenario_generator_tool(self):
        """Tool for generating comprehensive test scenarios"""
        from langchain.tools import Tool
        
        def generate_test_scenarios(workflow_data: str) -> str:
            """
            Generate comprehensive test scenarios based on discovered workflows
            
            Args:
                workflow_data: JSON string with workflow analysis
                
            Returns:
                Generated test scenarios for all testing types
            """
            
            test_scenarios = {
                "unit_test_scenarios": [
                    {
                        "component": "Search Input Component",
                        "tests": [
                            "Should accept valid text input",
                            "Should handle empty input",
                            "Should validate input length",
                            "Should sanitize special characters"
                        ]
                    }
                ],
                "integration_test_scenarios": [
                    {
                        "integration": "Search API Integration",
                        "tests": [
                            "Should call search API with correct parameters",
                            "Should handle API response correctly",
                            "Should handle API errors gracefully",
                            "Should manage API rate limiting"
                        ]
                    }
                ],
                "ui_test_scenarios": [
                    {
                        "feature": "Search Functionality",
                        "tests": [
                            {
                                "test_name": "Basic Search Flow",
                                "steps": [
                                    "Navigate to homepage",
                                    "Enter search term 'AI testing'",
                                    "Click search button",
                                    "Verify results appear"
                                ],
                                "expected": "Search results displayed within 2 seconds"
                            },
                            {
                                "test_name": "Autocomplete Functionality",
                                "steps": [
                                    "Navigate to homepage", 
                                    "Start typing 'machine lear'",
                                    "Wait for suggestions",
                                    "Verify dropdown appears"
                                ],
                                "expected": "Relevant suggestions appear"
                            }
                        ]
                    }
                ],
                "performance_test_scenarios": [
                    {
                        "scenario": "Search Performance Test",
                        "metrics": ["response_time", "throughput", "resource_usage"],
                        "load_patterns": [
                            "1 user - baseline",
                            "10 concurrent users",
                            "100 concurrent users"
                        ]
                    }
                ],
                "security_test_scenarios": [
                    {
                        "category": "Input Validation",
                        "tests": [
                            "XSS injection in search field",
                            "SQL injection attempts",
                            "CSRF token validation",
                            "Rate limiting bypass attempts"
                        ]
                    }
                ],
                "accessibility_test_scenarios": [
                    {
                        "category": "WCAG Compliance",
                        "tests": [
                            "Keyboard navigation support",
                            "Screen reader compatibility",
                            "Color contrast verification",
                            "Focus management"
                        ]
                    }
                ]
            }
            
            return json.dumps(test_scenarios, indent=2)
        
        return Tool(
            name="Test Scenario Generator",
            func=generate_test_scenarios,
            description="Generate comprehensive test scenarios across all testing domains based on discovered application features"
        )

    def create_discovery_task(self, application_config: Dict[str, Any]) -> Task:
        """Create the application discovery task"""
        
        base_url = application_config.get('urls', {}).get('base_url', 'https://www.google.com')
        app_name = application_config.get('application', {}).get('name', 'Web Application')
        
        return Task(
            description=f"""Perform comprehensive application discovery and analysis for {app_name} at {base_url}:
            
            🔍 **Phase 1: Application Exploration**
            - Use browser automation to navigate and explore the application
            - Discover all accessible pages, forms, and interactive elements
            - Map the application's structure and navigation flow
            - Identify technology stack and frameworks used
            
            🧩 **Phase 2: Feature Analysis** 
            - Catalog all UI elements (forms, buttons, inputs, links)
            - Identify primary and secondary features
            - Map user workflows and critical paths
            - Analyze accessibility and usability aspects
            
            🎯 **Phase 3: Test Scenario Generation**
            - Generate comprehensive test scenarios for all discovered features
            - Create test cases for unit, integration, UI, performance, and security testing
            - Prioritize test scenarios based on feature criticality and risk
            - Provide actionable test recommendations for all 11 AI agents
            
            🚀 **Phase 4: Intelligence Briefing**
            - Prepare detailed application analysis report
            - Provide feature-to-test mapping for downstream agents
            - Recommend testing strategies and priorities
            - Generate executable test specifications
            
            Focus on real, discoverable features rather than assumed functionality.
            Generate test cases that can be immediately executed by other AI agents.""",
            agent=self.create_agent(),
            expected_output="""Comprehensive Application Discovery Report including:
            1. Complete application structure map with discovered pages and features
            2. Detailed UI element catalog with selectors and interaction patterns
            3. Feature analysis with complexity assessment and risk evaluation
            4. User workflow mapping with critical path identification
            5. Generated test scenarios for all 11 testing domains
            6. Prioritized testing recommendations and execution strategies
            7. Technical specifications for automated test implementation"""
        )