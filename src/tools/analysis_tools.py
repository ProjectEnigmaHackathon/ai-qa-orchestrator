"""
Analysis Tools for CrewAI Agents - Story parsing, risk analysis, and business rule extraction
"""

from langchain.tools import Tool
from typing import Dict, List, Any, Optional
import re
import json
from datetime import datetime


class AnalysisTools:
    """Analysis tools for CrewAI agents"""
    
    def __init__(self):
        self.story_analyzer = Tool(
            name="story_analyzer",
            description="Analyze user stories and extract structured requirements",
            func=self._analyze_story
        )
        
        self.priority_manager = Tool(
            name="priority_manager", 
            description="Manage and prioritize testing requirements based on risk and business value",
            func=self._manage_priorities
        )
        
        self.nlp_parser = Tool(
            name="nlp_parser",
            description="Parse natural language text to extract entities, actions, and conditions",
            func=self._parse_natural_language
        )
        
        self.requirement_extractor = Tool(
            name="requirement_extractor",
            description="Extract testable requirements from user stories and specifications",
            func=self._extract_requirements
        )
        
        self.business_rule_analyzer = Tool(
            name="business_rule_analyzer",
            description="Analyze and extract business rules and constraints",
            func=self._analyze_business_rules
        )
        
        self.risk_matrix_calculator = Tool(
            name="risk_matrix_calculator",
            description="Calculate risk matrix and impact assessment",
            func=self._calculate_risk_matrix
        )
        
        self.vulnerability_scanner = Tool(
            name="vulnerability_scanner",
            description="Scan for potential security vulnerabilities and risks",
            func=self._scan_vulnerabilities
        )
        
        self.complexity_analyzer = Tool(
            name="complexity_analyzer",
            description="Analyze technical complexity and implementation challenges",
            func=self._analyze_complexity
        )
    
    def _analyze_story(self, user_story: str) -> str:
        """Analyze user story and extract structured information"""
        
        analysis = {
            'actors': self._extract_actors(user_story),
            'actions': self._extract_actions(user_story),
            'goals': self._extract_goals(user_story),
            'acceptance_criteria': self._extract_acceptance_criteria(user_story),
            'preconditions': self._extract_preconditions(user_story),
            'postconditions': self._extract_postconditions(user_story),
            'business_value': self._assess_business_value(user_story),
            'complexity_indicators': self._identify_complexity_indicators(user_story),
            'dependencies': self._identify_dependencies(user_story),
            'non_functional_requirements': self._extract_non_functional_requirements(user_story)
        }
        
        return json.dumps(analysis, indent=2)
    
    def _manage_priorities(self, requirements_data: str) -> str:
        """Manage and prioritize testing requirements"""
        
        try:
            requirements = json.loads(requirements_data) if isinstance(requirements_data, str) else requirements_data
        except:
            requirements = {'items': [requirements_data]}
        
        priorities = {
            'critical': [],
            'high': [],
            'medium': [],
            'low': []
        }
        
        # Simple prioritization logic
        for req in requirements.get('items', []):
            if any(keyword in str(req).lower() for keyword in ['security', 'payment', 'critical', 'must']):
                priorities['critical'].append(req)
            elif any(keyword in str(req).lower() for keyword in ['important', 'should', 'user']):
                priorities['high'].append(req)
            elif any(keyword in str(req).lower() for keyword in ['could', 'nice', 'optional']):
                priorities['low'].append(req)
            else:
                priorities['medium'].append(req)
        
        return json.dumps(priorities, indent=2)
    
    def _parse_natural_language(self, text: str) -> str:
        """Parse natural language to extract key components"""
        
        entities = {
            'people': self._extract_people_entities(text),
            'objects': self._extract_object_entities(text),
            'actions': self._extract_action_entities(text),
            'conditions': self._extract_condition_entities(text),
            'quantities': self._extract_quantity_entities(text),
            'time_references': self._extract_time_entities(text)
        }
        
        return json.dumps(entities, indent=2)
    
    def _extract_requirements(self, story_text: str) -> str:
        """Extract testable requirements from story text"""
        
        requirements = {
            'functional': self._extract_functional_requirements(story_text),
            'non_functional': self._extract_non_functional_requirements(story_text),
            'security': self._extract_security_requirements(story_text),
            'performance': self._extract_performance_requirements(story_text),
            'usability': self._extract_usability_requirements(story_text),
            'compatibility': self._extract_compatibility_requirements(story_text)
        }
        
        return json.dumps(requirements, indent=2)
    
    def _analyze_business_rules(self, text: str) -> str:
        """Analyze and extract business rules"""
        
        business_rules = {
            'validation_rules': self._extract_validation_rules(text),
            'business_constraints': self._extract_business_constraints(text),
            'workflow_rules': self._extract_workflow_rules(text),
            'authorization_rules': self._extract_authorization_rules(text),
            'calculation_rules': self._extract_calculation_rules(text),
            'exception_rules': self._extract_exception_rules(text)
        }
        
        return json.dumps(business_rules, indent=2)
    
    def _calculate_risk_matrix(self, context: str) -> str:
        """Calculate risk matrix for the given context"""
        
        risks = {
            'technical_risks': self._assess_technical_risks(context),
            'business_risks': self._assess_business_risks(context),
            'security_risks': self._assess_security_risks(context),
            'operational_risks': self._assess_operational_risks(context),
            'compliance_risks': self._assess_compliance_risks(context)
        }
        
        # Calculate overall risk score
        risk_scores = [risk.get('score', 0) for risk in risks.values()]
        overall_risk = sum(risk_scores) / len(risk_scores) if risk_scores else 0
        
        risk_matrix = {
            'overall_risk_score': overall_risk,
            'risk_level': self._categorize_risk_level(overall_risk),
            'detailed_risks': risks,
            'mitigation_priorities': self._prioritize_mitigations(risks),
            'testing_focus_areas': self._identify_testing_focus(risks)
        }
        
        return json.dumps(risk_matrix, indent=2)
    
    def _scan_vulnerabilities(self, content: str) -> str:
        """Scan for potential security vulnerabilities"""
        
        vulnerabilities = {
            'injection_risks': self._detect_injection_vulnerabilities(content),
            'authentication_risks': self._detect_auth_vulnerabilities(content),
            'authorization_risks': self._detect_authz_vulnerabilities(content),
            'data_exposure_risks': self._detect_data_exposure_vulnerabilities(content),
            'session_risks': self._detect_session_vulnerabilities(content),
            'input_validation_risks': self._detect_input_validation_vulnerabilities(content)
        }
        
        # Calculate vulnerability score
        vuln_scores = [vuln.get('severity', 0) for vuln in vulnerabilities.values()]
        overall_vulnerability = max(vuln_scores) if vuln_scores else 0
        
        vulnerability_report = {
            'overall_vulnerability_score': overall_vulnerability,
            'risk_level': self._categorize_risk_level(overall_vulnerability),
            'detected_vulnerabilities': vulnerabilities,
            'owasp_mapping': self._map_to_owasp(vulnerabilities),
            'recommended_tests': self._recommend_security_tests(vulnerabilities)
        }
        
        return json.dumps(vulnerability_report, indent=2)
    
    def _analyze_complexity(self, content: str) -> str:
        """Analyze technical complexity"""
        
        complexity_analysis = {
            'algorithmic_complexity': self._assess_algorithmic_complexity(content),
            'integration_complexity': self._assess_integration_complexity(content),
            'data_complexity': self._assess_data_complexity(content),
            'ui_complexity': self._assess_ui_complexity(content),
            'workflow_complexity': self._assess_workflow_complexity(content),
            'scalability_complexity': self._assess_scalability_complexity(content)
        }
        
        # Calculate overall complexity score
        complexity_scores = [comp.get('score', 0) for comp in complexity_analysis.values()]
        overall_complexity = sum(complexity_scores) / len(complexity_scores) if complexity_scores else 0
        
        complexity_report = {
            'overall_complexity_score': overall_complexity,
            'complexity_level': self._categorize_complexity_level(overall_complexity),
            'detailed_analysis': complexity_analysis,
            'complexity_drivers': self._identify_complexity_drivers(complexity_analysis),
            'testing_implications': self._derive_testing_implications(complexity_analysis)
        }
        
        return json.dumps(complexity_report, indent=2)
    
    # Helper methods for story analysis
    def _extract_actors(self, story: str) -> List[str]:
        """Extract user roles/actors from story"""
        actor_patterns = [
            r'As\s+an?\s+([^,]+)',
            r'As\s+a\s+([^,]+)',
            r'user',
            r'customer',
            r'admin',
            r'manager',
            r'employee'
        ]
        
        actors = []
        for pattern in actor_patterns:
            matches = re.findall(pattern, story, re.IGNORECASE)
            actors.extend(matches)
        
        return list(set([actor.strip() for actor in actors]))
    
    def _extract_actions(self, story: str) -> List[str]:
        """Extract actions from story"""
        action_patterns = [
            r'I want to\s+([^,\n]+)',
            r'I can\s+([^,\n]+)',
            r'I need to\s+([^,\n]+)',
            r'should be able to\s+([^,\n]+)'
        ]
        
        actions = []
        for pattern in action_patterns:
            matches = re.findall(pattern, story, re.IGNORECASE)
            actions.extend(matches)
        
        # Also look for verb phrases
        verb_pattern = r'\b(create|update|delete|view|manage|process|send|receive|login|logout|register|upload|download)\b'
        verb_matches = re.findall(verb_pattern, story, re.IGNORECASE)
        actions.extend(verb_matches)
        
        return list(set([action.strip() for action in actions]))
    
    def _extract_goals(self, story: str) -> List[str]:
        """Extract goals/benefits from story"""
        goal_patterns = [
            r'so that\s+([^.\n]+)',
            r'in order to\s+([^.\n]+)',
            r'to\s+([^.\n]+)'
        ]
        
        goals = []
        for pattern in goal_patterns:
            matches = re.findall(pattern, story, re.IGNORECASE)
            goals.extend(matches)
        
        return list(set([goal.strip() for goal in goals]))
    
    def _extract_acceptance_criteria(self, story: str) -> List[str]:
        """Extract acceptance criteria"""
        criteria = []
        
        # Look for bullet points or numbered lists
        bullet_patterns = [
            r'[-*•]\s*([^\n]+)',
            r'\d+\.\s*([^\n]+)',
            r'Given\s+([^\n]+)',
            r'When\s+([^\n]+)',
            r'Then\s+([^\n]+)'
        ]
        
        for pattern in bullet_patterns:
            matches = re.findall(pattern, story, re.IGNORECASE)
            criteria.extend(matches)
        
        return [criterion.strip() for criterion in criteria]
    
    def _extract_preconditions(self, story: str) -> List[str]:
        """Extract preconditions"""
        precondition_patterns = [
            r'Given\s+([^\n]+)',
            r'Assuming\s+([^\n]+)',
            r'When\s+([^\n]+)',
            r'If\s+([^\n]+)'
        ]
        
        preconditions = []
        for pattern in precondition_patterns:
            matches = re.findall(pattern, story, re.IGNORECASE)
            preconditions.extend(matches)
        
        return list(set([condition.strip() for condition in preconditions]))
    
    def _extract_postconditions(self, story: str) -> List[str]:
        """Extract postconditions/expected outcomes"""
        postcondition_patterns = [
            r'Then\s+([^\n]+)',
            r'should\s+([^\n]+)',
            r'will\s+([^\n]+)',
            r'result in\s+([^\n]+)'
        ]
        
        postconditions = []
        for pattern in postcondition_patterns:
            matches = re.findall(pattern, story, re.IGNORECASE)
            postconditions.extend(matches)
        
        return list(set([condition.strip() for condition in postconditions]))
    
    def _assess_business_value(self, story: str) -> Dict[str, Any]:
        """Assess potential business value"""
        value_indicators = {
            'user_facing': bool(re.search(r'user|customer|client', story, re.IGNORECASE)),
            'revenue_impact': bool(re.search(r'payment|money|revenue|sale|purchase', story, re.IGNORECASE)),
            'efficiency_gain': bool(re.search(r'automat|efficien|fast|quick|save', story, re.IGNORECASE)),
            'compliance_related': bool(re.search(r'complian|regulat|legal|audit', story, re.IGNORECASE)),
            'competitive_advantage': bool(re.search(r'competit|advantage|unique|differentiat', story, re.IGNORECASE))
        }
        
        value_score = sum(value_indicators.values()) / len(value_indicators)
        
        return {
            'score': value_score,
            'level': 'High' if value_score > 0.6 else 'Medium' if value_score > 0.3 else 'Low',
            'indicators': value_indicators
        }
    
    def _identify_complexity_indicators(self, story: str) -> List[str]:
        """Identify complexity indicators in the story"""
        complexity_keywords = [
            'complex', 'complicated', 'advanced', 'sophisticated',
            'integration', 'multiple', 'various', 'numerous',
            'real-time', 'concurrent', 'parallel', 'synchronous',
            'algorithm', 'calculation', 'processing', 'analysis',
            'workflow', 'orchestration', 'coordination'
        ]
        
        indicators = []
        for keyword in complexity_keywords:
            if re.search(rf'\b{keyword}\b', story, re.IGNORECASE):
                indicators.append(keyword)
        
        return indicators
    
    def _identify_dependencies(self, story: str) -> List[str]:
        """Identify system dependencies"""
        dependency_keywords = [
            'api', 'service', 'database', 'external', 'third-party',
            'integration', 'interface', 'connection', 'communication',
            'email', 'sms', 'notification', 'payment', 'authentication'
        ]
        
        dependencies = []
        for keyword in dependency_keywords:
            if re.search(rf'\b{keyword}\b', story, re.IGNORECASE):
                dependencies.append(keyword)
        
        return list(set(dependencies))
    
    def _extract_non_functional_requirements(self, story: str) -> List[str]:
        """Extract non-functional requirements"""
        nfr_patterns = [
            (r'(\d+)\s*(second|minute|hour)', 'Performance: {} {}'),
            (r'(\d+)\s*(user|concurrent|simultaneous)', 'Scalability: {} {}'),
            (r'(secure|encrypt|protect)', 'Security: {}'),
            (r'(available|uptime|24/7)', 'Availability: {}'),
            (r'(responsive|mobile|desktop)', 'Compatibility: {}')
        ]
        
        requirements = []
        for pattern, template in nfr_patterns:
            matches = re.findall(pattern, story, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    requirements.append(template.format(*match))
                else:
                    requirements.append(template.format(match))
        
        return requirements
    
    # Entity extraction methods
    def _extract_people_entities(self, text: str) -> List[str]:
        """Extract people-related entities"""
        people_patterns = [
            r'\b(user|customer|admin|manager|employee|client|visitor)\b',
            r'\b([A-Z][a-z]+\s+[A-Z][a-z]+)\b'  # Proper names
        ]
        
        people = []
        for pattern in people_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            people.extend([match if isinstance(match, str) else match[0] for match in matches])
        
        return list(set(people))
    
    def _extract_object_entities(self, text: str) -> List[str]:
        """Extract object entities"""
        object_keywords = [
            'account', 'profile', 'document', 'file', 'report', 'form',
            'order', 'product', 'service', 'payment', 'transaction',
            'message', 'notification', 'email', 'data', 'record'
        ]
        
        objects = []
        for keyword in object_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                objects.append(keyword)
        
        return objects
    
    def _extract_action_entities(self, text: str) -> List[str]:
        """Extract action entities"""
        action_verbs = [
            'create', 'read', 'update', 'delete', 'view', 'edit', 'manage',
            'send', 'receive', 'process', 'validate', 'verify', 'confirm',
            'login', 'logout', 'register', 'authenticate', 'authorize',
            'upload', 'download', 'export', 'import', 'search', 'filter'
        ]
        
        actions = []
        for verb in action_verbs:
            if re.search(rf'\b{verb}\b', text, re.IGNORECASE):
                actions.append(verb)
        
        return actions
    
    def _extract_condition_entities(self, text: str) -> List[str]:
        """Extract condition entities"""
        condition_patterns = [
            r'if\s+([^,.\n]+)',
            r'when\s+([^,.\n]+)',
            r'unless\s+([^,.\n]+)',
            r'provided\s+([^,.\n]+)',
            r'given\s+([^,.\n]+)'
        ]
        
        conditions = []
        for pattern in condition_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            conditions.extend(matches)
        
        return [condition.strip() for condition in conditions]
    
    def _extract_quantity_entities(self, text: str) -> List[str]:
        """Extract quantity entities"""
        quantity_patterns = [
            r'(\d+)\s*(items?|records?|users?|times?)',
            r'(all|every|each|any|some|many|few)',
            r'(minimum|maximum|at least|at most|up to|more than|less than)\s*(\d+)'
        ]
        
        quantities = []
        for pattern in quantity_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    quantities.append(' '.join(match))
                else:
                    quantities.append(match)
        
        return quantities
    
    def _extract_time_entities(self, text: str) -> List[str]:
        """Extract time-related entities"""
        time_patterns = [
            r'(\d+)\s*(second|minute|hour|day|week|month|year)s?',
            r'(daily|weekly|monthly|yearly|annually)',
            r'(immediately|instantly|real-time|asynchronously)',
            r'(before|after|during|within)\s+([^,.\n]+)'
        ]
        
        times = []
        for pattern in time_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    times.append(' '.join(match))
                else:
                    times.append(match)
        
        return times
    
    # Requirement extraction methods
    def _extract_functional_requirements(self, text: str) -> List[str]:
        """Extract functional requirements"""
        functional_indicators = [
            'shall', 'must', 'should', 'will', 'can', 'may',
            'function', 'feature', 'capability', 'ability',
            'process', 'handle', 'manage', 'control'
        ]
        
        requirements = []
        sentences = re.split(r'[.!?]+', text)
        
        for sentence in sentences:
            if any(indicator in sentence.lower() for indicator in functional_indicators):
                requirements.append(sentence.strip())
        
        return [req for req in requirements if req]
    
    def _extract_security_requirements(self, text: str) -> List[str]:
        """Extract security requirements"""
        security_keywords = [
            'secure', 'encrypt', 'authenticate', 'authorize', 'protect',
            'privacy', 'confidential', 'access control', 'permission',
            'security', 'safe', 'trusted', 'verified'
        ]
        
        requirements = []
        for keyword in security_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                requirements.append(f"Security requirement: {keyword}")
        
        return requirements
    
    def _extract_performance_requirements(self, text: str) -> List[str]:
        """Extract performance requirements"""
        performance_patterns = [
            r'within\s+(\d+)\s*(second|minute|millisecond)',
            r'respond\s+in\s+(\d+)\s*(second|minute|millisecond)',
            r'(\d+)\s*concurrent\s*users?',
            r'handle\s+(\d+)\s*(request|transaction|operation)s?'
        ]
        
        requirements = []
        for pattern in performance_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    requirements.append(f"Performance: {' '.join(match)}")
                else:
                    requirements.append(f"Performance: {match}")
        
        return requirements
    
    def _extract_usability_requirements(self, text: str) -> List[str]:
        """Extract usability requirements"""
        usability_keywords = [
            'easy', 'simple', 'intuitive', 'user-friendly',
            'accessible', 'responsive', 'mobile', 'desktop'
        ]
        
        requirements = []
        for keyword in usability_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                requirements.append(f"Usability: {keyword}")
        
        return requirements
    
    def _extract_compatibility_requirements(self, text: str) -> List[str]:
        """Extract compatibility requirements"""
        compatibility_patterns = [
            r'(browser|chrome|firefox|safari|edge)',
            r'(mobile|ios|android|tablet)',
            r'(windows|mac|linux)',
            r'compatible\s+with\s+([^,.\n]+)'
        ]
        
        requirements = []
        for pattern in compatibility_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                requirements.append(f"Compatibility: {match}")
        
        return requirements
    
    # Business rule extraction methods
    def _extract_validation_rules(self, text: str) -> List[str]:
        """Extract validation rules"""
        validation_patterns = [
            r'must\s+be\s+([^,.\n]+)',
            r'should\s+contain\s+([^,.\n]+)',
            r'cannot\s+be\s+([^,.\n]+)',
            r'valid\s+([^,.\n]+)',
            r'required\s+([^,.\n]+)'
        ]
        
        rules = []
        for pattern in validation_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            rules.extend([f"Validation: {match.strip()}" for match in matches])
        
        return rules
    
    def _extract_business_constraints(self, text: str) -> List[str]:
        """Extract business constraints"""
        constraint_keywords = [
            'limit', 'maximum', 'minimum', 'restrict', 'prevent',
            'allow only', 'not exceed', 'at least', 'at most'
        ]
        
        constraints = []
        for keyword in constraint_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                # Find the sentence containing the keyword
                sentences = re.split(r'[.!?]+', text)
                for sentence in sentences:
                    if keyword.lower() in sentence.lower():
                        constraints.append(f"Constraint: {sentence.strip()}")
                        break
        
        return constraints
    
    def _extract_workflow_rules(self, text: str) -> List[str]:
        """Extract workflow rules"""
        workflow_keywords = [
            'before', 'after', 'then', 'next', 'first', 'finally',
            'sequence', 'order', 'step', 'workflow', 'process'
        ]
        
        rules = []
        for keyword in workflow_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                sentences = re.split(r'[.!?]+', text)
                for sentence in sentences:
                    if keyword.lower() in sentence.lower():
                        rules.append(f"Workflow: {sentence.strip()}")
                        break
        
        return rules
    
    def _extract_authorization_rules(self, text: str) -> List[str]:
        """Extract authorization rules"""
        auth_keywords = [
            'admin', 'user', 'role', 'permission', 'access',
            'only', 'authorized', 'allowed', 'restricted'
        ]
        
        rules = []
        for keyword in auth_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                sentences = re.split(r'[.!?]+', text)
                for sentence in sentences:
                    if keyword.lower() in sentence.lower():
                        rules.append(f"Authorization: {sentence.strip()}")
                        break
        
        return rules
    
    def _extract_calculation_rules(self, text: str) -> List[str]:
        """Extract calculation rules"""
        calc_keywords = [
            'calculate', 'compute', 'total', 'sum', 'average',
            'percentage', 'rate', 'fee', 'discount', 'tax'
        ]
        
        rules = []
        for keyword in calc_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                sentences = re.split(r'[.!?]+', text)
                for sentence in sentences:
                    if keyword.lower() in sentence.lower():
                        rules.append(f"Calculation: {sentence.strip()}")
                        break
        
        return rules
    
    def _extract_exception_rules(self, text: str) -> List[str]:
        """Extract exception rules"""
        exception_keywords = [
            'except', 'unless', 'but', 'however', 'special case',
            'exception', 'exclude', 'ignore', 'skip'
        ]
        
        rules = []
        for keyword in exception_keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                sentences = re.split(r'[.!?]+', text)
                for sentence in sentences:
                    if keyword.lower() in sentence.lower():
                        rules.append(f"Exception: {sentence.strip()}")
                        break
        
        return rules
    
    # Risk assessment methods
    def _assess_technical_risks(self, context: str) -> Dict[str, Any]:
        """Assess technical risks"""
        risk_indicators = {
            'complexity': len(re.findall(r'complex|complicated|advanced', context, re.IGNORECASE)),
            'integration': len(re.findall(r'integration|api|service|external', context, re.IGNORECASE)),
            'performance': len(re.findall(r'performance|speed|fast|slow|load', context, re.IGNORECASE)),
            'scalability': len(re.findall(r'scale|concurrent|multiple|volume', context, re.IGNORECASE))
        }
        
        score = min(sum(risk_indicators.values()) * 0.1, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_risk_level(score),
            'indicators': risk_indicators
        }
    
    def _assess_business_risks(self, context: str) -> Dict[str, Any]:
        """Assess business risks"""
        risk_indicators = {
            'financial_impact': len(re.findall(r'money|payment|revenue|cost|financial', context, re.IGNORECASE)),
            'regulatory': len(re.findall(r'compliance|regulation|legal|audit', context, re.IGNORECASE)),
            'reputation': len(re.findall(r'public|customer|reputation|brand', context, re.IGNORECASE)),
            'operational': len(re.findall(r'critical|essential|business|operation', context, re.IGNORECASE))
        }
        
        score = min(sum(risk_indicators.values()) * 0.15, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_risk_level(score),
            'indicators': risk_indicators
        }
    
    def _assess_security_risks(self, context: str) -> Dict[str, Any]:
        """Assess security risks"""
        risk_indicators = {
            'authentication': len(re.findall(r'login|password|auth|credential', context, re.IGNORECASE)),
            'data_exposure': len(re.findall(r'data|information|personal|sensitive', context, re.IGNORECASE)),
            'access_control': len(re.findall(r'access|permission|role|admin', context, re.IGNORECASE)),
            'input_handling': len(re.findall(r'input|form|upload|search', context, re.IGNORECASE))
        }
        
        score = min(sum(risk_indicators.values()) * 0.2, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_risk_level(score),
            'indicators': risk_indicators
        }
    
    def _assess_operational_risks(self, context: str) -> Dict[str, Any]:
        """Assess operational risks"""
        risk_indicators = {
            'deployment': len(re.findall(r'deploy|release|production|environment', context, re.IGNORECASE)),
            'monitoring': len(re.findall(r'monitor|track|log|alert', context, re.IGNORECASE)),
            'maintenance': len(re.findall(r'maintain|support|update|patch', context, re.IGNORECASE)),
            'backup': len(re.findall(r'backup|recovery|disaster|failover', context, re.IGNORECASE))
        }
        
        score = min(sum(risk_indicators.values()) * 0.1, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_risk_level(score),
            'indicators': risk_indicators
        }
    
    def _assess_compliance_risks(self, context: str) -> Dict[str, Any]:
        """Assess compliance risks"""
        risk_indicators = {
            'privacy': len(re.findall(r'privacy|gdpr|personal|pii', context, re.IGNORECASE)),
            'security_standards': len(re.findall(r'pci|hipaa|sox|iso', context, re.IGNORECASE)),
            'audit': len(re.findall(r'audit|compliance|regulation|legal', context, re.IGNORECASE)),
            'documentation': len(re.findall(r'document|record|trail|log', context, re.IGNORECASE))
        }
        
        score = min(sum(risk_indicators.values()) * 0.2, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_risk_level(score),
            'indicators': risk_indicators
        }
    
    def _categorize_risk_level(self, score: float) -> str:
        """Categorize risk level based on score"""
        if score >= 0.8:
            return 'Critical'
        elif score >= 0.6:
            return 'High'
        elif score >= 0.4:
            return 'Medium'
        else:
            return 'Low'
    
    def _prioritize_mitigations(self, risks: Dict[str, Any]) -> List[str]:
        """Prioritize risk mitigations"""
        high_risk_areas = []
        
        for risk_type, risk_data in risks.items():
            if risk_data.get('score', 0) >= 0.6:
                high_risk_areas.append(risk_type.replace('_', ' ').title())
        
        return high_risk_areas
    
    def _identify_testing_focus(self, risks: Dict[str, Any]) -> List[str]:
        """Identify testing focus areas based on risks"""
        focus_areas = []
        
        risk_to_testing = {
            'technical_risks': 'Unit and Integration Testing',
            'business_risks': 'User Acceptance Testing',
            'security_risks': 'Security Testing',
            'operational_risks': 'Operational Testing',
            'compliance_risks': 'Compliance Testing'
        }
        
        for risk_type, risk_data in risks.items():
            if risk_data.get('score', 0) >= 0.5:
                testing_type = risk_to_testing.get(risk_type, 'General Testing')
                focus_areas.append(testing_type)
        
        return focus_areas
    
    # Vulnerability detection methods
    def _detect_injection_vulnerabilities(self, content: str) -> Dict[str, Any]:
        """Detect injection vulnerability risks"""
        indicators = [
            'sql', 'query', 'database', 'search', 'input',
            'form', 'parameter', 'filter', 'where', 'select'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        severity = min(matches * 0.2, 1.0)
        
        return {
            'severity': severity,
            'risk_level': self._categorize_risk_level(severity),
            'indicators_found': matches,
            'description': 'SQL injection and other injection attack risks'
        }
    
    def _detect_auth_vulnerabilities(self, content: str) -> Dict[str, Any]:
        """Detect authentication vulnerability risks"""
        indicators = [
            'login', 'password', 'authenticate', 'credential',
            'token', 'session', 'cookie', 'remember', 'forgot'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        severity = min(matches * 0.15, 1.0)
        
        return {
            'severity': severity,
            'risk_level': self._categorize_risk_level(severity),
            'indicators_found': matches,
            'description': 'Authentication bypass and credential attack risks'
        }
    
    def _detect_authz_vulnerabilities(self, content: str) -> Dict[str, Any]:
        """Detect authorization vulnerability risks"""
        indicators = [
            'admin', 'role', 'permission', 'access', 'privilege',
            'authorize', 'allow', 'deny', 'restrict', 'control'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        severity = min(matches * 0.15, 1.0)
        
        return {
            'severity': severity,
            'risk_level': self._categorize_risk_level(severity),
            'indicators_found': matches,
            'description': 'Authorization bypass and privilege escalation risks'
        }
    
    def _detect_data_exposure_vulnerabilities(self, content: str) -> Dict[str, Any]:
        """Detect data exposure vulnerability risks"""
        indicators = [
            'data', 'information', 'personal', 'sensitive', 'confidential',
            'export', 'download', 'api', 'public', 'share', 'expose'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        severity = min(matches * 0.1, 1.0)
        
        return {
            'severity': severity,
            'risk_level': self._categorize_risk_level(severity),
            'indicators_found': matches,
            'description': 'Sensitive data exposure risks'
        }
    
    def _detect_session_vulnerabilities(self, content: str) -> Dict[str, Any]:
        """Detect session management vulnerability risks"""
        indicators = [
            'session', 'cookie', 'token', 'timeout', 'expire',
            'logout', 'remember', 'persistent', 'state'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        severity = min(matches * 0.15, 1.0)
        
        return {
            'severity': severity,
            'risk_level': self._categorize_risk_level(severity),
            'indicators_found': matches,
            'description': 'Session management and fixation risks'
        }
    
    def _detect_input_validation_vulnerabilities(self, content: str) -> Dict[str, Any]:
        """Detect input validation vulnerability risks"""
        indicators = [
            'input', 'form', 'upload', 'file', 'image', 'document',
            'validate', 'sanitize', 'escape', 'filter', 'clean'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        severity = min(matches * 0.1, 1.0)
        
        return {
            'severity': severity,
            'risk_level': self._categorize_risk_level(severity),
            'indicators_found': matches,
            'description': 'Input validation bypass risks'
        }
    
    def _map_to_owasp(self, vulnerabilities: Dict[str, Any]) -> Dict[str, str]:
        """Map detected vulnerabilities to OWASP Top 10"""
        owasp_mapping = {}
        
        if vulnerabilities.get('injection_risks', {}).get('severity', 0) > 0.3:
            owasp_mapping['A03:2021 – Injection'] = 'SQL, NoSQL, OS injection risks detected'
        
        if vulnerabilities.get('authentication_risks', {}).get('severity', 0) > 0.3:
            owasp_mapping['A07:2021 – Identification and Authentication Failures'] = 'Authentication weakness risks detected'
        
        if vulnerabilities.get('authorization_risks', {}).get('severity', 0) > 0.3:
            owasp_mapping['A01:2021 – Broken Access Control'] = 'Authorization bypass risks detected'
        
        if vulnerabilities.get('data_exposure_risks', {}).get('severity', 0) > 0.3:
            owasp_mapping['A02:2021 – Cryptographic Failures'] = 'Sensitive data exposure risks detected'
        
        return owasp_mapping
    
    def _recommend_security_tests(self, vulnerabilities: Dict[str, Any]) -> List[str]:
        """Recommend security tests based on detected vulnerabilities"""
        recommendations = []
        
        for vuln_type, vuln_data in vulnerabilities.items():
            if vuln_data.get('severity', 0) > 0.3:
                if 'injection' in vuln_type:
                    recommendations.append('SQL injection and input validation testing')
                elif 'authentication' in vuln_type:
                    recommendations.append('Authentication bypass and brute force testing')
                elif 'authorization' in vuln_type:
                    recommendations.append('Privilege escalation and access control testing')
                elif 'data_exposure' in vuln_type:
                    recommendations.append('Data leakage and information disclosure testing')
                elif 'session' in vuln_type:
                    recommendations.append('Session management and fixation testing')
                elif 'input_validation' in vuln_type:
                    recommendations.append('Input validation and XSS testing')
        
        return recommendations
    
    # Complexity analysis methods
    def _assess_algorithmic_complexity(self, content: str) -> Dict[str, Any]:
        """Assess algorithmic complexity"""
        indicators = [
            'algorithm', 'calculation', 'compute', 'process',
            'sort', 'search', 'optimize', 'analyze', 'complex'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        score = min(matches * 0.2, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_complexity_level(score),
            'indicators': matches
        }
    
    def _assess_integration_complexity(self, content: str) -> Dict[str, Any]:
        """Assess integration complexity"""
        indicators = [
            'integration', 'api', 'service', 'external', 'third-party',
            'webhook', 'callback', 'sync', 'async', 'interface'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        score = min(matches * 0.15, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_complexity_level(score),
            'indicators': matches
        }
    
    def _assess_data_complexity(self, content: str) -> Dict[str, Any]:
        """Assess data complexity"""
        indicators = [
            'data', 'database', 'model', 'schema', 'relationship',
            'migration', 'transformation', 'mapping', 'structure'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        score = min(matches * 0.1, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_complexity_level(score),
            'indicators': matches
        }
    
    def _assess_ui_complexity(self, content: str) -> Dict[str, Any]:
        """Assess UI complexity"""
        indicators = [
            'interface', 'ui', 'user interface', 'form', 'component',
            'responsive', 'mobile', 'interactive', 'dynamic', 'animation'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        score = min(matches * 0.1, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_complexity_level(score),
            'indicators': matches
        }
    
    def _assess_workflow_complexity(self, content: str) -> Dict[str, Any]:
        """Assess workflow complexity"""
        indicators = [
            'workflow', 'process', 'step', 'sequence', 'orchestration',
            'coordination', 'approval', 'review', 'stage', 'phase'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        score = min(matches * 0.15, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_complexity_level(score),
            'indicators': matches
        }
    
    def _assess_scalability_complexity(self, content: str) -> Dict[str, Any]:
        """Assess scalability complexity"""
        indicators = [
            'scale', 'scalability', 'concurrent', 'parallel', 'distributed',
            'load', 'performance', 'throughput', 'capacity', 'volume'
        ]
        
        matches = sum(1 for indicator in indicators 
                     if re.search(rf'\b{indicator}\b', content, re.IGNORECASE))
        
        score = min(matches * 0.15, 1.0)
        
        return {
            'score': score,
            'level': self._categorize_complexity_level(score),
            'indicators': matches
        }
    
    def _categorize_complexity_level(self, score: float) -> str:
        """Categorize complexity level based on score"""
        if score >= 0.8:
            return 'Very High'
        elif score >= 0.6:
            return 'High'
        elif score >= 0.4:
            return 'Medium'
        elif score >= 0.2:
            return 'Low'
        else:
            return 'Very Low'
    
    def _identify_complexity_drivers(self, complexity_analysis: Dict[str, Any]) -> List[str]:
        """Identify main complexity drivers"""
        drivers = []
        
        for complexity_type, analysis in complexity_analysis.items():
            if analysis.get('score', 0) >= 0.6:
                drivers.append(complexity_type.replace('_', ' ').title())
        
        return drivers
    
    def _derive_testing_implications(self, complexity_analysis: Dict[str, Any]) -> List[str]:
        """Derive testing implications from complexity analysis"""
        implications = []
        
        complexity_to_testing = {
            'algorithmic_complexity': 'Extensive unit testing with edge cases and performance validation',
            'integration_complexity': 'Comprehensive integration testing and service mesh validation',
            'data_complexity': 'Data integrity testing and migration validation',
            'ui_complexity': 'Cross-browser testing and responsive design validation',
            'workflow_complexity': 'End-to-end workflow testing and state management validation',
            'scalability_complexity': 'Load testing and performance benchmarking'
        }
        
        for complexity_type, analysis in complexity_analysis.items():
            if analysis.get('score', 0) >= 0.5:
                implication = complexity_to_testing.get(complexity_type, 'General comprehensive testing')
                implications.append(implication)
        
        return implications