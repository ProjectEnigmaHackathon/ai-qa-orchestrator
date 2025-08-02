"""
Advanced Risk Analysis System - Multi-dimensional risk assessment
"""

import re
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import hashlib


class AdvancedRiskAnalyzer:
    """
    Comprehensive risk analysis engine for test prioritization
    """
    
    def __init__(self):
        self.risk_weights = {
            'business_criticality': 0.25,
            'technical_complexity': 0.20,
            'security_exposure': 0.25,
            'performance_impact': 0.15,
            'integration_complexity': 0.15
        }
        
        self.security_patterns = self._load_security_patterns()
        self.performance_indicators = self._load_performance_indicators()
        self.complexity_metrics = self._load_complexity_metrics()
        
    def calculate_comprehensive_risk_matrix(
        self, 
        user_story: str, 
        code_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """Calculate multi-dimensional risk analysis"""
        
        risk_categories = {
            'business_risks': self._assess_business_risks(user_story),
            'technical_risks': self._assess_technical_risks(user_story, code_context),
            'security_risks': self._assess_security_risks(user_story),
            'performance_risks': self._assess_performance_risks(user_story),
            'operational_risks': self._assess_operational_risks(user_story)
        }
        
        # Calculate weighted overall risk score
        overall_risk_score = self._calculate_weighted_risk(risk_categories)
        
        # Generate risk-based test priorities
        test_priorities = self._generate_test_priorities(risk_categories)
        
        # Create mitigation strategies
        mitigation_strategies = self._recommend_mitigations(risk_categories)
        
        return {
            'risk_matrix': risk_categories,
            'overall_risk_score': overall_risk_score,
            'risk_level': self._categorize_risk_level(overall_risk_score),
            'test_priorities': test_priorities,
            'mitigation_strategies': mitigation_strategies,
            'risk_analysis_metadata': {
                'timestamp': datetime.now().isoformat(),
                'analyzer_version': '1.0.0',
                'risk_calculation_method': 'weighted_multi_dimensional'
            }
        }
    
    def _assess_business_risks(self, user_story: str) -> Dict[str, Any]:
        """Assess business-related risks"""
        
        business_risk_indicators = {
            'financial_impact': self._detect_financial_keywords(user_story),
            'regulatory_compliance': self._detect_compliance_requirements(user_story),
            'user_experience': self._assess_ux_impact(user_story),
            'data_privacy': self._detect_privacy_concerns(user_story),
            'business_continuity': self._assess_continuity_impact(user_story)
        }
        
        # Calculate business risk score
        business_score = sum([
            business_risk_indicators['financial_impact'] * 0.3,
            business_risk_indicators['regulatory_compliance'] * 0.25,
            business_risk_indicators['user_experience'] * 0.2,
            business_risk_indicators['data_privacy'] * 0.15,
            business_risk_indicators['business_continuity'] * 0.1
        ])
        
        return {
            'score': min(business_score, 1.0),
            'level': self._score_to_level(business_score),
            'indicators': business_risk_indicators,
            'critical_factors': self._identify_critical_business_factors(business_risk_indicators),
            'recommendations': self._generate_business_risk_recommendations(business_risk_indicators)
        }
    
    def _assess_technical_risks(self, user_story: str, code_context: Optional[str]) -> Dict[str, Any]:
        """Assess technical complexity and implementation risks"""
        
        technical_indicators = {
            'complexity_score': self._calculate_complexity_score(user_story, code_context),
            'integration_complexity': self._assess_integration_complexity(user_story),
            'technology_maturity': self._assess_technology_maturity(user_story, code_context),
            'scalability_concerns': self._identify_scalability_risks(user_story),
            'maintainability_risks': self._assess_maintainability_risks(user_story, code_context)
        }
        
        technical_score = sum([
            technical_indicators['complexity_score'] * 0.25,
            technical_indicators['integration_complexity'] * 0.25,
            technical_indicators['technology_maturity'] * 0.2,
            technical_indicators['scalability_concerns'] * 0.15,
            technical_indicators['maintainability_risks'] * 0.15
        ])
        
        return {
            'score': min(technical_score, 1.0),
            'level': self._score_to_level(technical_score),
            'indicators': technical_indicators,
            'complexity_breakdown': self._breakdown_complexity(user_story, code_context),
            'recommendations': self._generate_technical_recommendations(technical_indicators)
        }
    
    def _assess_security_risks(self, user_story: str) -> Dict[str, Any]:
        """Assess security vulnerabilities and attack vectors"""
        
        security_indicators = {
            'authentication_risks': self._detect_auth_risks(user_story),
            'authorization_risks': self._detect_authz_risks(user_story),
            'data_exposure_risks': self._detect_data_exposure_risks(user_story),
            'injection_vulnerabilities': self._detect_injection_risks(user_story),
            'session_management_risks': self._detect_session_risks(user_story),
            'owasp_risk_coverage': self._assess_owasp_coverage(user_story)
        }
        
        security_score = max([
            security_indicators['authentication_risks'],
            security_indicators['authorization_risks'],
            security_indicators['data_exposure_risks'],
            security_indicators['injection_vulnerabilities'],
            security_indicators['session_management_risks']
        ])
        
        return {
            'score': security_score,
            'level': self._score_to_level(security_score),
            'indicators': security_indicators,
            'owasp_mapping': self._map_to_owasp_top10(security_indicators),
            'attack_vectors': self._identify_attack_vectors(security_indicators),
            'recommendations': self._generate_security_recommendations(security_indicators)
        }
    
    def _assess_performance_risks(self, user_story: str) -> Dict[str, Any]:
        """Assess performance and scalability risks"""
        
        performance_indicators = {
            'load_sensitivity': self._assess_load_sensitivity(user_story),
            'resource_intensity': self._assess_resource_requirements(user_story),
            'response_time_criticality': self._assess_response_time_requirements(user_story),
            'concurrent_user_impact': self._assess_concurrency_risks(user_story),
            'data_volume_sensitivity': self._assess_data_volume_risks(user_story)
        }
        
        performance_score = sum([
            performance_indicators['load_sensitivity'] * 0.25,
            performance_indicators['resource_intensity'] * 0.2,
            performance_indicators['response_time_criticality'] * 0.25,
            performance_indicators['concurrent_user_impact'] * 0.15,
            performance_indicators['data_volume_sensitivity'] * 0.15
        ])
        
        return {
            'score': min(performance_score, 1.0),
            'level': self._score_to_level(performance_score),
            'indicators': performance_indicators,
            'bottleneck_predictions': self._predict_bottlenecks(performance_indicators),
            'sla_requirements': self._extract_sla_requirements(user_story),
            'recommendations': self._generate_performance_recommendations(performance_indicators)
        }
    
    def _assess_operational_risks(self, user_story: str) -> Dict[str, Any]:
        """Assess operational and deployment risks"""
        
        operational_indicators = {
            'deployment_complexity': self._assess_deployment_complexity(user_story),
            'monitoring_requirements': self._assess_monitoring_needs(user_story),
            'backup_recovery_needs': self._assess_backup_requirements(user_story),
            'support_complexity': self._assess_support_requirements(user_story),
            'rollback_complexity': self._assess_rollback_requirements(user_story)
        }
        
        operational_score = sum([
            operational_indicators['deployment_complexity'] * 0.25,
            operational_indicators['monitoring_requirements'] * 0.2,
            operational_indicators['backup_recovery_needs'] * 0.2,
            operational_indicators['support_complexity'] * 0.2,
            operational_indicators['rollback_complexity'] * 0.15
        ])
        
        return {
            'score': min(operational_score, 1.0),
            'level': self._score_to_level(operational_score),
            'indicators': operational_indicators,
            'operational_checklist': self._generate_operational_checklist(operational_indicators),
            'recommendations': self._generate_operational_recommendations(operational_indicators)
        }
    
    # Business Risk Assessment Methods
    def _detect_financial_keywords(self, user_story: str) -> float:
        """Detect financial transaction keywords"""
        financial_keywords = [
            'payment', 'money', 'transfer', 'transaction', 'billing', 'invoice',
            'credit', 'debit', 'bank', 'account', 'financial', 'purchase',
            'refund', 'charge', 'cost', 'price', 'subscription', 'revenue'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in financial_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _detect_compliance_requirements(self, user_story: str) -> float:
        """Detect regulatory compliance requirements"""
        compliance_keywords = [
            'gdpr', 'hipaa', 'pci', 'sox', 'compliance', 'regulation',
            'audit', 'legal', 'privacy', 'consent', 'data protection',
            'security', 'encryption', 'anonymization'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in compliance_keywords if keyword in story_lower)
        return min(matches * 0.25, 1.0)
    
    def _assess_ux_impact(self, user_story: str) -> float:
        """Assess user experience impact"""
        ux_keywords = [
            'user', 'customer', 'interface', 'experience', 'usability',
            'accessibility', 'responsive', 'mobile', 'performance',
            'loading', 'navigation', 'workflow'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in ux_keywords if keyword in story_lower)
        return min(matches * 0.15, 1.0)
    
    def _detect_privacy_concerns(self, user_story: str) -> float:
        """Detect data privacy concerns"""
        privacy_keywords = [
            'personal', 'pii', 'sensitive', 'confidential', 'private',
            'email', 'phone', 'address', 'ssn', 'medical', 'health',
            'biometric', 'location', 'tracking'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in privacy_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _assess_continuity_impact(self, user_story: str) -> float:
        """Assess business continuity impact"""
        continuity_keywords = [
            'critical', 'essential', 'important', 'core', 'main',
            '24/7', 'availability', 'uptime', 'downtime', 'backup',
            'recovery', 'disaster', 'failover'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in continuity_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    # Technical Risk Assessment Methods
    def _calculate_complexity_score(self, user_story: str, code_context: Optional[str]) -> float:
        """Calculate technical complexity score"""
        complexity_indicators = []
        
        # Story complexity indicators
        story_lower = user_story.lower()
        complex_keywords = [
            'algorithm', 'machine learning', 'ai', 'complex', 'advanced',
            'integration', 'synchronization', 'real-time', 'concurrent',
            'distributed', 'microservice', 'workflow', 'orchestration'
        ]
        
        keyword_matches = sum(1 for keyword in complex_keywords if keyword in story_lower)
        complexity_indicators.append(min(keyword_matches * 0.1, 0.5))
        
        # Code context complexity
        if code_context:
            code_complexity = self._analyze_code_complexity(code_context)
            complexity_indicators.append(code_complexity)
        
        # Story length and detail complexity
        story_length_factor = min(len(user_story.split()) / 100, 0.3)
        complexity_indicators.append(story_length_factor)
        
        return min(sum(complexity_indicators), 1.0)
    
    def _assess_integration_complexity(self, user_story: str) -> float:
        """Assess integration complexity"""
        integration_keywords = [
            'api', 'service', 'external', 'third-party', 'integration',
            'webhook', 'callback', 'sync', 'async', 'queue', 'message',
            'database', 'cache', 'search', 'email', 'sms', 'notification'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in integration_keywords if keyword in story_lower)
        return min(matches * 0.15, 1.0)
    
    def _assess_technology_maturity(self, user_story: str, code_context: Optional[str]) -> float:
        """Assess technology maturity risks"""
        # Look for bleeding-edge or experimental technologies
        experimental_keywords = [
            'beta', 'alpha', 'experimental', 'preview', 'unstable',
            'new', 'latest', 'cutting-edge', 'bleeding-edge'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in experimental_keywords if keyword in story_lower)
        
        # Code context analysis for experimental patterns
        if code_context:
            code_lower = code_context.lower()
            code_matches = sum(1 for keyword in experimental_keywords if keyword in code_lower)
            matches += code_matches
        
        return min(matches * 0.2, 1.0)
    
    # Security Risk Assessment Methods
    def _detect_auth_risks(self, user_story: str) -> float:
        """Detect authentication risks"""
        auth_keywords = [
            'login', 'password', 'authentication', 'auth', 'signin',
            'credentials', 'token', 'session', 'oauth', 'sso',
            'multi-factor', '2fa', 'biometric'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in auth_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _detect_authz_risks(self, user_story: str) -> float:
        """Detect authorization risks"""
        authz_keywords = [
            'permission', 'role', 'access', 'admin', 'user', 'privilege',
            'authorization', 'access control', 'rbac', 'acl',
            'scope', 'resource', 'ownership'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in authz_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _detect_data_exposure_risks(self, user_story: str) -> float:
        """Detect data exposure risks"""
        exposure_keywords = [
            'data', 'information', 'personal', 'sensitive', 'confidential',
            'export', 'download', 'share', 'public', 'api', 'endpoint',
            'log', 'error', 'debug', 'trace'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in exposure_keywords if keyword in story_lower)
        return min(matches * 0.15, 1.0)
    
    def _detect_injection_risks(self, user_story: str) -> float:
        """Detect injection vulnerability risks"""
        injection_keywords = [
            'input', 'form', 'search', 'query', 'parameter', 'upload',
            'file', 'image', 'document', 'sql', 'database', 'script',
            'html', 'xml', 'json', 'csv'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in injection_keywords if keyword in story_lower)
        return min(matches * 0.15, 1.0)
    
    # Performance Risk Assessment Methods
    def _assess_load_sensitivity(self, user_story: str) -> float:
        """Assess load sensitivity"""
        load_keywords = [
            'concurrent', 'simultaneous', 'parallel', 'bulk', 'batch',
            'multiple', 'mass', 'scale', 'volume', 'load', 'traffic',
            'users', 'requests', 'transactions'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in load_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _assess_resource_requirements(self, user_story: str) -> float:
        """Assess resource intensity"""
        resource_keywords = [
            'processing', 'calculation', 'computation', 'algorithm',
            'analysis', 'report', 'export', 'large', 'big', 'heavy',
            'memory', 'cpu', 'disk', 'storage', 'bandwidth'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in resource_keywords if keyword in story_lower)
        return min(matches * 0.15, 1.0)
    
    def _assess_response_time_requirements(self, user_story: str) -> float:
        """Assess response time criticality"""
        time_keywords = [
            'real-time', 'instant', 'immediate', 'fast', 'quick',
            'responsive', 'latency', 'delay', 'timeout', 'performance',
            'speed', 'millisecond', 'second'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in time_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    # Helper Methods
    def _calculate_weighted_risk(self, risk_categories: Dict[str, Any]) -> float:
        """Calculate weighted overall risk score"""
        weighted_score = 0
        
        for category, weight in self.risk_weights.items():
            if category in risk_categories:
                category_score = risk_categories[category].get('score', 0)
                weighted_score += category_score * weight
        
        return min(weighted_score, 1.0)
    
    def _score_to_level(self, score: float) -> str:
        """Convert numeric score to risk level"""
        if score < 0.3:
            return 'Low'
        elif score < 0.6:
            return 'Medium'
        elif score < 0.8:
            return 'High'
        else:
            return 'Critical'
    
    def _categorize_risk_level(self, overall_score: float) -> str:
        """Categorize overall risk level"""
        return self._score_to_level(overall_score)
    
    def _generate_test_priorities(self, risk_categories: Dict[str, Any]) -> Dict[str, Any]:
        """Generate test priorities based on risk analysis"""
        priorities = {
            'high_priority': [],
            'medium_priority': [],
            'low_priority': []
        }
        
        # Prioritize based on risk scores
        for category, details in risk_categories.items():
            score = details.get('score', 0)
            
            if score >= 0.7:
                priorities['high_priority'].append({
                    'category': category,
                    'score': score,
                    'rationale': f"High risk in {category.replace('_', ' ')} requires immediate attention"
                })
            elif score >= 0.4:
                priorities['medium_priority'].append({
                    'category': category,
                    'score': score,
                    'rationale': f"Moderate risk in {category.replace('_', ' ')} should be addressed"
                })
            else:
                priorities['low_priority'].append({
                    'category': category,
                    'score': score,
                    'rationale': f"Low risk in {category.replace('_', ' ')} can be addressed later"
                })
        
        return priorities
    
    def _recommend_mitigations(self, risk_categories: Dict[str, Any]) -> Dict[str, List[str]]:
        """Recommend risk mitigation strategies"""
        mitigations = {}
        
        for category, details in risk_categories.items():
            score = details.get('score', 0)
            
            if score >= 0.5:  # Only recommend mitigations for significant risks
                mitigations[category] = self._get_category_mitigations(category, details)
        
        return mitigations
    
    def _get_category_mitigations(self, category: str, details: Dict[str, Any]) -> List[str]:
        """Get specific mitigation strategies for a risk category"""
        
        mitigation_strategies = {
            'business_risks': [
                "Implement comprehensive user acceptance testing",
                "Establish clear business requirements validation",
                "Create rollback procedures for critical changes",
                "Implement feature flags for gradual rollout"
            ],
            'technical_risks': [
                "Conduct thorough code reviews",
                "Implement comprehensive unit and integration testing",
                "Use proven design patterns and architectures",
                "Create detailed technical documentation"
            ],
            'security_risks': [
                "Implement security code reviews",
                "Conduct penetration testing",
                "Use automated security scanning tools",
                "Follow OWASP security guidelines"
            ],
            'performance_risks': [
                "Implement load testing and performance monitoring",
                "Use caching strategies where appropriate",
                "Optimize database queries and indexes",
                "Implement horizontal scaling capabilities"
            ],
            'operational_risks': [
                "Create comprehensive deployment procedures",
                "Implement monitoring and alerting",
                "Establish backup and recovery procedures",
                "Create operational runbooks"
            ]
        }
        
        return mitigation_strategies.get(category, ["Implement standard risk mitigation procedures"])
    
    def _load_security_patterns(self) -> Dict[str, List[str]]:
        """Load security risk patterns"""
        return {
            'sql_injection': ['query', 'sql', 'database', 'search', 'filter'],
            'xss': ['input', 'html', 'script', 'form', 'user content'],
            'csrf': ['form', 'post', 'action', 'state changing'],
            'auth_bypass': ['admin', 'privilege', 'role', 'permission']
        }
    
    def _load_performance_indicators(self) -> Dict[str, List[str]]:
        """Load performance risk indicators"""
        return {
            'high_load': ['concurrent', 'bulk', 'batch', 'multiple'],
            'resource_intensive': ['processing', 'calculation', 'analysis'],
            'real_time': ['instant', 'real-time', 'immediate', 'live']
        }
    
    def _load_complexity_metrics(self) -> Dict[str, float]:
        """Load complexity scoring metrics"""
        return {
            'integration_weight': 0.3,
            'algorithm_weight': 0.4,
            'data_processing_weight': 0.2,
            'ui_complexity_weight': 0.1
        }
    
    # Additional helper methods (implementations would be added based on requirements)
    def _analyze_code_complexity(self, code_context: str) -> float:
        """Analyze code complexity from context"""
        # Simple heuristic based on code patterns
        complexity_patterns = [
            r'for\s+.*\s+in\s+.*:',  # Loops
            r'if\s+.*:',             # Conditionals
            r'def\s+\w+\(',          # Function definitions
            r'class\s+\w+',          # Class definitions
            r'try\s*:',              # Exception handling
            r'async\s+def',          # Async functions
        ]
        
        total_matches = 0
        for pattern in complexity_patterns:
            matches = len(re.findall(pattern, code_context, re.IGNORECASE))
            total_matches += matches
        
        # Normalize based on code length
        lines = len(code_context.split('\n'))
        complexity_ratio = total_matches / max(lines, 1)
        
        return min(complexity_ratio, 1.0)
    
    def _identify_critical_business_factors(self, indicators: Dict[str, float]) -> List[str]:
        """Identify critical business risk factors"""
        critical_factors = []
        
        for factor, score in indicators.items():
            if score >= 0.7:
                critical_factors.append(factor.replace('_', ' ').title())
        
        return critical_factors
    
    def _generate_business_risk_recommendations(self, indicators: Dict[str, float]) -> List[str]:
        """Generate business risk recommendations"""
        recommendations = []
        
        if indicators.get('financial_impact', 0) >= 0.5:
            recommendations.append("Implement financial transaction validation and audit trails")
        
        if indicators.get('regulatory_compliance', 0) >= 0.5:
            recommendations.append("Conduct compliance review and implement necessary controls")
        
        if indicators.get('user_experience', 0) >= 0.5:
            recommendations.append("Perform usability testing and accessibility audits")
        
        return recommendations
    
    def _breakdown_complexity(self, user_story: str, code_context: Optional[str]) -> Dict[str, float]:
        """Break down complexity into components"""
        return {
            'story_complexity': len(user_story.split()) / 100,
            'integration_complexity': self._assess_integration_complexity(user_story),
            'code_complexity': self._analyze_code_complexity(code_context) if code_context else 0,
            'domain_complexity': self._assess_domain_complexity(user_story)
        }
    
    def _assess_domain_complexity(self, user_story: str) -> float:
        """Assess domain-specific complexity"""
        complex_domains = [
            'financial', 'medical', 'legal', 'scientific', 'educational',
            'government', 'insurance', 'logistics', 'manufacturing'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for domain in complex_domains if domain in story_lower)
        return min(matches * 0.3, 1.0)
    
    def _generate_technical_recommendations(self, indicators: Dict[str, float]) -> List[str]:
        """Generate technical risk recommendations"""
        recommendations = []
        
        if indicators.get('complexity_score', 0) >= 0.6:
            recommendations.append("Break down complex functionality into smaller, manageable components")
        
        if indicators.get('integration_complexity', 0) >= 0.5:
            recommendations.append("Implement comprehensive integration testing and monitoring")
        
        if indicators.get('scalability_concerns', 0) >= 0.5:
            recommendations.append("Design for horizontal scaling and load distribution")
        
        return recommendations
    
    def _map_to_owasp_top10(self, security_indicators: Dict[str, float]) -> Dict[str, str]:
        """Map security risks to OWASP Top 10"""
        owasp_mapping = {}
        
        if security_indicators.get('injection_vulnerabilities', 0) >= 0.3:
            owasp_mapping['A03:2021 – Injection'] = 'High priority testing required'
        
        if security_indicators.get('authentication_risks', 0) >= 0.3:
            owasp_mapping['A07:2021 – Identification and Authentication Failures'] = 'Authentication testing required'
        
        if security_indicators.get('data_exposure_risks', 0) >= 0.3:
            owasp_mapping['A01:2021 – Broken Access Control'] = 'Access control testing required'
        
        return owasp_mapping
    
    def _identify_attack_vectors(self, security_indicators: Dict[str, float]) -> List[Dict[str, str]]:
        """Identify potential attack vectors"""
        attack_vectors = []
        
        if security_indicators.get('injection_vulnerabilities', 0) >= 0.3:
            attack_vectors.append({
                'vector': 'SQL Injection',
                'description': 'Malicious SQL queries through input fields',
                'impact': 'High - Data breach, data manipulation'
            })
        
        if security_indicators.get('authentication_risks', 0) >= 0.3:
            attack_vectors.append({
                'vector': 'Credential Stuffing',
                'description': 'Automated login attempts with stolen credentials',
                'impact': 'Medium - Account takeover'
            })
        
        return attack_vectors
    
    def _generate_security_recommendations(self, indicators: Dict[str, float]) -> List[str]:
        """Generate security recommendations"""
        recommendations = []
        
        if indicators.get('authentication_risks', 0) >= 0.4:
            recommendations.append("Implement multi-factor authentication and account lockout policies")
        
        if indicators.get('data_exposure_risks', 0) >= 0.4:
            recommendations.append("Implement data encryption and access logging")
        
        if indicators.get('injection_vulnerabilities', 0) >= 0.4:
            recommendations.append("Use parameterized queries and input validation")
        
        return recommendations
    
    def _predict_bottlenecks(self, performance_indicators: Dict[str, float]) -> List[Dict[str, str]]:
        """Predict potential performance bottlenecks"""
        bottlenecks = []
        
        if performance_indicators.get('load_sensitivity', 0) >= 0.5:
            bottlenecks.append({
                'type': 'Concurrency Bottleneck',
                'description': 'System may struggle under high concurrent load',
                'mitigation': 'Implement connection pooling and load balancing'
            })
        
        if performance_indicators.get('resource_intensity', 0) >= 0.5:
            bottlenecks.append({
                'type': 'Resource Bottleneck',
                'description': 'High CPU/memory usage may impact performance',
                'mitigation': 'Optimize algorithms and implement caching'
            })
        
        return bottlenecks
    
    def _extract_sla_requirements(self, user_story: str) -> Dict[str, str]:
        """Extract SLA requirements from user story"""
        sla_requirements = {}
        
        # Look for response time requirements
        time_patterns = [
            r'(\d+)\s*(millisecond|ms)',
            r'(\d+)\s*(second|s)',
            r'within\s+(\d+)\s*(second|minute)'
        ]
        
        for pattern in time_patterns:
            matches = re.findall(pattern, user_story.lower())
            if matches:
                sla_requirements['response_time'] = f"{matches[0][0]} {matches[0][1]}"
                break
        
        # Look for availability requirements
        if '24/7' in user_story or 'always available' in user_story.lower():
            sla_requirements['availability'] = '99.9% uptime'
        
        return sla_requirements
    
    def _generate_performance_recommendations(self, indicators: Dict[str, float]) -> List[str]:
        """Generate performance recommendations"""
        recommendations = []
        
        if indicators.get('load_sensitivity', 0) >= 0.5:
            recommendations.append("Implement load testing and auto-scaling capabilities")
        
        if indicators.get('response_time_criticality', 0) >= 0.5:
            recommendations.append("Optimize critical path performance and implement caching")
        
        if indicators.get('data_volume_sensitivity', 0) >= 0.5:
            recommendations.append("Implement data pagination and efficient querying")
        
        return recommendations
    
    # Operational risk assessment methods (implementations would continue similarly...)
    def _assess_deployment_complexity(self, user_story: str) -> float:
        """Assess deployment complexity"""
        deployment_keywords = [
            'deploy', 'migration', 'database', 'configuration', 'environment',
            'production', 'staging', 'rollout', 'release', 'version'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in deployment_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _assess_monitoring_needs(self, user_story: str) -> float:
        """Assess monitoring requirements"""
        monitoring_keywords = [
            'monitor', 'track', 'log', 'alert', 'notification', 'metric',
            'performance', 'health', 'status', 'availability', 'error'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in monitoring_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _assess_backup_requirements(self, user_story: str) -> float:
        """Assess backup and recovery requirements"""
        backup_keywords = [
            'backup', 'recovery', 'restore', 'disaster', 'failover',
            'redundancy', 'replication', 'archive', 'snapshot'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in backup_keywords if keyword in story_lower)
        return min(matches * 0.25, 1.0)
    
    def _assess_support_requirements(self, user_story: str) -> float:
        """Assess support complexity"""
        support_keywords = [
            'support', 'help', 'documentation', 'training', 'guide',
            'manual', 'tutorial', 'troubleshoot', 'debug', 'maintenance'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in support_keywords if keyword in story_lower)
        return min(matches * 0.15, 1.0)
    
    def _assess_rollback_requirements(self, user_story: str) -> float:
        """Assess rollback complexity"""
        rollback_keywords = [
            'rollback', 'revert', 'undo', 'previous version', 'restore',
            'fallback', 'downgrade', 'cancel', 'abort'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in rollback_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _generate_operational_checklist(self, indicators: Dict[str, float]) -> List[str]:
        """Generate operational checklist"""
        checklist = [
            "Verify deployment procedures are documented and tested",
            "Ensure monitoring and alerting are configured",
            "Confirm backup and recovery procedures are in place",
            "Validate rollback procedures are tested and ready"
        ]
        
        if indicators.get('deployment_complexity', 0) >= 0.5:
            checklist.append("Conduct deployment dry run in staging environment")
        
        if indicators.get('monitoring_requirements', 0) >= 0.5:
            checklist.append("Set up comprehensive application monitoring")
        
        return checklist
    
    def _generate_operational_recommendations(self, indicators: Dict[str, float]) -> List[str]:
        """Generate operational recommendations"""
        recommendations = []
        
        if indicators.get('deployment_complexity', 0) >= 0.5:
            recommendations.append("Implement blue-green deployment strategy")
        
        if indicators.get('monitoring_requirements', 0) >= 0.5:
            recommendations.append("Set up proactive monitoring and alerting")
        
        if indicators.get('support_complexity', 0) >= 0.5:
            recommendations.append("Create comprehensive operational documentation")
        
        return recommendations
    
    def _identify_scalability_risks(self, user_story: str) -> float:
        """Identify scalability concerns"""
        scalability_keywords = [
            'scale', 'growth', 'expand', 'increase', 'volume', 'load',
            'capacity', 'throughput', 'concurrent', 'parallel'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in scalability_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _assess_maintainability_risks(self, user_story: str, code_context: Optional[str]) -> float:
        """Assess maintainability risks"""
        maintainability_score = 0
        
        # Story complexity affects maintainability
        story_complexity = len(user_story.split()) / 100
        maintainability_score += min(story_complexity, 0.3)
        
        # Code complexity affects maintainability
        if code_context:
            code_complexity = self._analyze_code_complexity(code_context)
            maintainability_score += code_complexity * 0.4
        
        return min(maintainability_score, 1.0)
    
    def _detect_session_risks(self, user_story: str) -> float:
        """Detect session management risks"""
        session_keywords = [
            'session', 'cookie', 'token', 'login', 'logout', 'timeout',
            'remember', 'stay logged', 'persistent', 'expire'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in session_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)
    
    def _assess_owasp_coverage(self, user_story: str) -> float:
        """Assess OWASP risk coverage needed"""
        owasp_indicators = [
            self._detect_auth_risks(user_story),
            self._detect_authz_risks(user_story),
            self._detect_data_exposure_risks(user_story),
            self._detect_injection_risks(user_story),
            self._detect_session_risks(user_story)
        ]
        
        return max(owasp_indicators)
    
    def _assess_concurrency_risks(self, user_story: str) -> float:
        """Assess concurrent access risks"""
        concurrency_keywords = [
            'concurrent', 'simultaneous', 'parallel', 'same time',
            'multiple users', 'shared', 'lock', 'synchronize'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in concurrency_keywords if keyword in story_lower)
        return min(matches * 0.25, 1.0)
    
    def _assess_data_volume_risks(self, user_story: str) -> float:
        """Assess data volume sensitivity"""
        volume_keywords = [
            'large', 'big', 'massive', 'bulk', 'batch', 'thousands',
            'millions', 'huge', 'enormous', 'gigabyte', 'terabyte'
        ]
        
        story_lower = user_story.lower()
        matches = sum(1 for keyword in volume_keywords if keyword in story_lower)
        return min(matches * 0.2, 1.0)