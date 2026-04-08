"""
Main Application Entry Point
AI Legal Monitoring System
"""
import logging
import sys
from typing import Dict, List

# Import modules
from data_collection.scraper import LegalDataScraper
from document_processing.nlp_engine import LegalNLPEngine
from analysis.impact_analyzer import ImpactAnalyzer
from analysis.compliance_engine import ComplianceRecommendationEngine
from alerts.alert_manager import AlertManager
from audit.audit_logger import AuditLogger
from dashboard.api import DashboardAPI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LegalMonitoringSystem:
    """Main system orchestrator"""
    
    def __init__(self, config: Dict = None):
        """Initialize the legal monitoring system"""
        self.config = config or {}
        
        # Initialize components
        logger.info("Initializing AI Legal Monitoring System...")
        
        self.scraper = LegalDataScraper(timeout=10)
        self.nlp_engine = LegalNLPEngine()
        self.impact_analyzer = ImpactAnalyzer()
        self.compliance_engine = ComplianceRecommendationEngine()
        self.alert_manager = AlertManager(
            smtp_server='smtp.gmail.com',
            smtp_port=587,
            sender_email='',
            sender_password=''
        )
        self.audit_logger = AuditLogger()
        self.dashboard_api = DashboardAPI()
        
        logger.info("System initialization complete")
    
    def process_legal_content(self, content_url: str) -> Dict:
        """
        Complete pipeline for processing legal content
        
        Args:
            content_url: URL of legal document or direct text
            
        Returns:
            Complete analysis result
        """
        logger.info(f"Processing legal content from: {content_url}")
        
        result = {
            'status': 'processing',
            'steps': []
        }
        
        try:
            # Step 1: Data Collection
            logger.info("Step 1: Collecting data...")
            document = self.scraper.fetch_from_url(content_url)
            if not document:
                logger.error("Failed to fetch document")
                return {'status': 'error', 'message': 'Failed to fetch document'}
            
            self.audit_logger.log_document_received(document)
            result['steps'].append({'name': 'Data Collection', 'status': 'completed'})
            
            # Step 2: Document Processing
            logger.info("Step 2: Processing document...")
            processed_document = self.nlp_engine.process_document(document)
            self.audit_logger.log_document_processed(processed_document)
            result['steps'].append({'name': 'Document Processing', 'status': 'completed'})
            
            # Step 3: Impact Analysis
            logger.info("Step 3: Analyzing impact...")
            impact_analysis = self.impact_analyzer.analyze_impact(processed_document)
            departments = self.impact_analyzer.identify_affected_departments(impact_analysis)
            self.audit_logger.log_impact_analysis(impact_analysis)
            result['steps'].append({'name': 'Impact Analysis', 'status': 'completed'})
            
            # Step 4: Compliance Recommendations
            logger.info("Step 4: Generating recommendations...")
            recommendations = self.compliance_engine.generate_recommendations(impact_analysis)
            self.audit_logger.log_recommendation_generated(recommendations)
            result['steps'].append({'name': 'Compliance Recommendations', 'status': 'completed'})
            
            # Step 5: Risk Assessment
            logger.info("Step 5: Assessing risks...")
            risks = self.compliance_engine.identify_risks(recommendations)
            result['steps'].append({'name': 'Risk Assessment', 'status': 'completed'})
            
            # Compile results
            result['status'] = 'completed'
            result['analysis'] = {
                'document': {
                    'title': processed_document.get('title'),
                    'summary': processed_document.get('summary'),
                    'url': processed_document.get('url'),
                    'extracted_at': processed_document.get('extracted_at')
                },
                'impact_analysis': impact_analysis,
                'affected_departments': departments,
                'recommendations': recommendations,
                'risk_assessment': risks
            }
            
            return result
        
        except Exception as e:
            logger.error(f"Error processing legal content: {str(e)}")
            return {'status': 'error', 'message': str(e)}
    
    def send_alerts(self, analysis_result: Dict, recipients: List[str]) -> bool:
        """
        Send alerts based on analysis results
        
        Args:
            analysis_result: Results from process_legal_content
            recipients: List of email addresses
            
        Returns:
            True if alerts sent successfully
        """
        if analysis_result.get('status') != 'completed':
            logger.warning("Cannot send alerts for incomplete analysis")
            return False
        
        try:
            analysis = analysis_result.get('analysis', {})
            alert_data = {
                'title': analysis.get('document', {}).get('title', 'Legal Update'),
                'summary': analysis.get('document', {}).get('summary', ''),
                'source': 'AI Legal Monitoring System',
                'date': analysis.get('document', {}).get('extracted_at'),
                'risk_level': analysis.get('risk_assessment', {}).get('overall_risk_level', 'Medium'),
                'affected_areas': analysis.get('impact_analysis', {}).get('affected_categories', []),
                'impact_level': analysis.get('impact_analysis', {}).get('overall_impact_level', 'Medium'),
                'actions': [rec.get('action') for rec in analysis.get('recommendations', [])[:5]]
            }
            
            results = self.alert_manager.send_bulk_alerts(recipients, alert_data)
            
            alert_info = {
                'recipients': recipients,
                'type': 'email',
                'risk_level': alert_data['risk_level'],
                'status': 'sent' if results['failed'] == 0 else 'partially_sent'
            }
            self.audit_logger.log_alert_sent(alert_info)
            
            logger.info(f"Alerts sent: {results['sent']}/{results['total']} successful")
            return results['failed'] == 0
        
        except Exception as e:
            logger.error(f"Error sending alerts: {str(e)}")
            return False
    
    def get_compliance_status(self) -> Dict:
        """Get overall compliance status"""
        try:
            # This would aggregate data from database/storage
            return {
                'compliance_score': 0.0,
                'risk_level': 'Unknown',
                'pending_actions': 0,
                'completed_actions': 0,
                'by_category': {}
            }
        except Exception as e:
            logger.error(f"Error getting compliance status: {str(e)}")
            return {}
    
    def start_dashboard(self, host: str = '0.0.0.0', port: int = 5000):
        """Start the dashboard API"""
        logger.info(f"Starting dashboard API on {host}:{port}")
        self.dashboard_api.run(host=host, port=port, debug=False)


def main():
    """Main entry point"""
    logger.info("Starting AI Legal Monitoring System")
    
    # Initialize system
    system = LegalMonitoringSystem()
    
    # Example: Process a legal document
    # result = system.process_legal_content("https://example.com/legal-document")
    
    # Start dashboard
    system.start_dashboard()


if __name__ == '__main__':
    main()
