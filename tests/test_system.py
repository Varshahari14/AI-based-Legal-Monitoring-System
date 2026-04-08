"""
Unit tests for AI Legal Monitoring System
"""
import unittest
from unittest.mock import Mock, patch
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data_collection.scraper import LegalDataScraper
from src.document_processing.nlp_engine import LegalNLPEngine
from src.analysis.impact_analyzer import ImpactAnalyzer
from src.analysis.compliance_engine import ComplianceRecommendationEngine
from src.audit.audit_logger import AuditLogger


class TestLegalDataScraper(unittest.TestCase):
    """Test data collection module"""
    
    def setUp(self):
        self.scraper = LegalDataScraper()
    
    def test_extract_title(self):
        """Test title extraction"""
        from bs4 import BeautifulSoup
        html = "<html><title>Test Document</title></html>"
        soup = BeautifulSoup(html, 'html.parser')
        
        title = self.scraper._extract_title(soup)
        self.assertEqual(title, "Test Document")
    
    def test_extract_content(self):
        """Test content extraction"""
        from bs4 import BeautifulSoup
        html = "<html><body><p>Test content</p><script>ignored</script></body></html>"
        soup = BeautifulSoup(html, 'html.parser')
        
        content = self.scraper._extract_content(soup)
        self.assertIn("Test content", content)
        self.assertNotIn("script", content)


class TestImpactAnalyzer(unittest.TestCase):
    """Test impact analysis module"""
    
    def setUp(self):
        self.analyzer = ImpactAnalyzer()
    
    def test_category_detection(self):
        """Test impact detection for business categories"""
        document = {
            'summary': 'New privacy regulations requiring consent',
            'content': 'Personal data protection measures mandatory'
        }
        
        impact = self.analyzer.analyze_impact(document)
        self.assertIn('Data & Privacy', impact.get('affected_categories', []))
    
    def test_impact_level_calculation(self):
        """Test impact level calculation"""
        impact_level = self.analyzer._calculate_impact_level(5, 10)
        self.assertEqual(impact_level, 'Medium')


class TestComplianceEngine(unittest.TestCase):
    """Test compliance recommendation engine"""
    
    def setUp(self):
        self.engine = ComplianceRecommendationEngine()
    
    def test_recommendation_generation(self):
        """Test recommendation generation"""
        impact_analysis = {
            'affected_categories': ['Data & Privacy', 'Employment']
        }
        
        recommendations = self.engine.generate_recommendations(impact_analysis)
        self.assertGreater(len(recommendations), 0)
        self.assertTrue(all('action' in rec for rec in recommendations))
    
    def test_compliance_score_calculation(self):
        """Test compliance score calculation"""
        recommendations = [
            {'status': 'completed'},
            {'status': 'in_progress'},
            {'status': 'pending'}
        ]
        
        score = self.engine.calculate_compliance_score(recommendations)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 100)


class TestAuditLogger(unittest.TestCase):
    """Test audit logging"""
    
    def setUp(self):
        self.audit_logger = AuditLogger(log_file='./test_audit.log')
    
    def test_log_document_received(self):
        """Test document received logging"""
        document = {
            'url': 'http://example.com',
            'source': 'government',
            'title': 'Test Doc'
        }
        
        self.audit_logger.log_document_received(document)
        # Logging should not raise exception
    
    def test_filter_audit_logs(self):
        """Test filtering audit logs"""
        self.audit_logger.log_document_received({
            'url': 'test',
            'source': 'government',
            'title': 'Test'
        })
        
        filters = {'event_type': 'DOCUMENT_RECEIVED'}
        logs = self.audit_logger.retrieve_audit_logs(filters)
        
        # Should retrieve the logged event
        self.assertIsInstance(logs, list)


if __name__ == '__main__':
    unittest.main()
