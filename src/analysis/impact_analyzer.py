"""
Impact Analysis Module
Analyzes how legal changes impact business operations
"""
from typing import Dict, List
import json
import logging

logger = logging.getLogger(__name__)


class ImpactAnalyzer:
    """Analyzes impact of legal changes on business"""
    
    # Business operation categories
    BUSINESS_CATEGORIES = [
        'Data & Privacy',
        'Employment',
        'Financial',
        'Operations',
        'Marketing & Advertising',
        'Environmental',
        'Safety & Health',
        'Consumer Protection'
    ]
    
    def __init__(self):
        """Initialize impact analyzer"""
        self.impact_keywords = self._initialize_keywords()
    
    def _initialize_keywords(self) -> Dict[str, List[str]]:
        """Initialize keywords for impact detection"""
        return {
            'Data & Privacy': [
                'personal data', 'privacy', 'gdpr', 'data protection',
                'consent', 'processing', 'breach', 'privacy policy'
            ],
            'Employment': [
                'employee', 'labour', 'wages', 'working hours', 'safety',
                'discrimination', 'harassment', 'termination', 'benefits'
            ],
            'Financial': [
                'tax', 'revenue', 'fee', 'financial', 'accounting',
                'reporting', 'audit', 'payment', 'tariff'
            ],
            'Operations': [
                'manufacturing', 'supply chain', 'quality', 'distribution',
                'certification', 'compliance', 'procedure', 'standard'
            ],
            'Marketing & Advertising': [
                'advertising', 'marketing', 'claims', 'endorsement',
                'testimonial', 'disclosure', 'labeling', 'competition'
            ],
            'Environmental': [
                'environment', 'pollution', 'emissions', 'waste',
                'sustainability', 'carbon', 'climate', 'air quality'
            ],
            'Safety & Health': [
                'safety', 'health', 'hazard', 'risk', 'injury',
                'prevention', 'training', 'incident', 'accident'
            ],
            'Consumer Protection': [
                'consumer', 'customer', 'product', 'liability', 'warranty',
                'recall', 'refund', 'complaint', 'protection'
            ]
        }
    
    def analyze_impact(self, document: Dict) -> Dict:
        """
        Analyze impact of legal document on business
        
        Args:
            document: Processed legal document
            
        Returns:
            Impact analysis results
        """
        text = (document.get('summary', '') + ' ' + document.get('content', '')).lower()
        
        impacts = {}
        for category in self.BUSINESS_CATEGORIES:
            keywords = self.impact_keywords.get(category, [])
            match_count = sum(1 for keyword in keywords if keyword in text)
            
            if match_count > 0:
                impact_level = self._calculate_impact_level(match_count, len(keywords))
                impacts[category] = {
                    'affected': True,
                    'impact_level': impact_level,
                    'relevant_keywords': [kw for kw in keywords if kw in text]
                }
        
        return {
            'document_id': document.get('url', 'unknown'),
            'impacts_by_category': impacts,
            'affected_categories': list(impacts.keys()),
            'overall_impact_level': self._calculate_overall_impact(impacts),
            'requires_action': len(impacts) > 0
        }
    
    def _calculate_impact_level(self, matches: int, total_keywords: int) -> str:
        """Determine impact level based on keyword matches"""
        percentage = (matches / total_keywords) * 100
        
        if percentage >= 50:
            return 'High'
        elif percentage >= 25:
            return 'Medium'
        else:
            return 'Low'
    
    def _calculate_overall_impact(self, impacts: Dict) -> str:
        """Calculate overall impact across all categories"""
        if not impacts:
            return 'Low'
        
        high_count = sum(1 for impact in impacts.values() if impact.get('impact_level') == 'High')
        
        if high_count >= 3:
            return 'High'
        elif high_count >= 1 or len(impacts) >= 3:
            return 'Medium'
        else:
            return 'Low'
    
    def identify_affected_departments(self, impacts: Dict) -> Dict[str, List[str]]:
        """Map impacts to affected business departments"""
        department_mapping = {
            'Data & Privacy': ['Legal', 'IT', 'Privacy Officer'],
            'Employment': ['HR', 'Legal'],
            'Financial': ['Finance', 'Accounting', 'Legal'],
            'Operations': ['Operations', 'Quality', 'Compliance'],
            'Marketing & Advertising': ['Marketing', 'Legal', 'Sales'],
            'Environmental': ['Operations', 'Sustainability', 'Legal'],
            'Safety & Health': ['HR', 'Safety', 'Operations'],
            'Consumer Protection': ['Legal', 'Customer Service', 'Product']
        }
        
        affected_departments = {}
        for category in impacts.get('affected_categories', []):
            affected_departments[category] = department_mapping.get(category, ['Legal'])
        
        return affected_departments
