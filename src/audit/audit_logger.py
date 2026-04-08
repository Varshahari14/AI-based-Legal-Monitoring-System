"""
Audit Logger
Maintains comprehensive audit trail of all system activities
"""
import json
import logging
from datetime import datetime
from typing import Dict, Any
import os
from pathlib import Path

logger = logging.getLogger(__name__)


class AuditLogger:
    """Manages audit logging for compliance tracking"""
    
    def __init__(self, log_file: str = './logs/audit.log'):
        """Initialize audit logger"""
        self.log_file = log_file
        self._create_log_directory()
        self.setup_logging()
    
    def _create_log_directory(self):
        """Create logs directory if it doesn't exist"""
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def log_document_received(self, document: Dict) -> None:
        """Log when a document is received"""
        event = {
            'event_type': 'DOCUMENT_RECEIVED',
            'timestamp': datetime.now().isoformat(),
            'document_id': document.get('url', 'unknown'),
            'source': document.get('source', 'unknown'),
            'title': document.get('title', 'unknown')
        }
        self._write_audit_log(event)
    
    def log_document_processed(self, document: Dict) -> None:
        """Log when a document is processed"""
        event = {
            'event_type': 'DOCUMENT_PROCESSED',
            'timestamp': datetime.now().isoformat(),
            'document_id': document.get('url', 'unknown'),
            'status': document.get('status', 'unknown')
        }
        self._write_audit_log(event)
    
    def log_impact_analysis(self, impact_analysis: Dict) -> None:
        """Log impact analysis results"""
        event = {
            'event_type': 'IMPACT_ANALYSIS',
            'timestamp': datetime.now().isoformat(),
            'document_id': impact_analysis.get('document_id', 'unknown'),
            'affected_categories': impact_analysis.get('affected_categories', []),
            'overall_impact_level': impact_analysis.get('overall_impact_level', 'Unknown')
        }
        self._write_audit_log(event)
    
    def log_recommendation_generated(self, recommendations: Dict) -> None:
        """Log when recommendations are generated"""
        event = {
            'event_type': 'RECOMMENDATION_GENERATED',
            'timestamp': datetime.now().isoformat(),
            'recommendation_count': len(recommendations) if isinstance(recommendations, list) else 1,
            'details': str(recommendations)[:500]  # Truncate for logging
        }
        self._write_audit_log(event)
    
    def log_alert_sent(self, alert_info: Dict) -> None:
        """Log when an alert is sent"""
        event = {
            'event_type': 'ALERT_SENT',
            'timestamp': datetime.now().isoformat(),
            'recipients': alert_info.get('recipients', []),
            'alert_type': alert_info.get('type', 'email'),
            'risk_level': alert_info.get('risk_level', 'Unknown'),
            'status': alert_info.get('status', 'sent')
        }
        self._write_audit_log(event)
    
    def log_compliance_check(self, compliance_data: Dict) -> None:
        """Log compliance check execution"""
        event = {
            'event_type': 'COMPLIANCE_CHECK',
            'timestamp': datetime.now().isoformat(),
            'compliance_score': compliance_data.get('score', 0),
            'risk_level': compliance_data.get('risk_level', 'Unknown'),
            'pending_actions': compliance_data.get('pending_count', 0)
        }
        self._write_audit_log(event)
    
    def log_user_action(self, action_type: str, user_id: str, details: Dict) -> None:
        """Log user actions"""
        event = {
            'event_type': 'USER_ACTION',
            'timestamp': datetime.now().isoformat(),
            'action_type': action_type,
            'user_id': user_id,
            'details': details
        }
        self._write_audit_log(event)
    
    def log_error(self, error_type: str, error_message: str, context: Dict = None) -> None:
        """Log system errors"""
        event = {
            'event_type': 'ERROR',
            'timestamp': datetime.now().isoformat(),
            'error_type': error_type,
            'error_message': error_message,
            'context': context or {}
        }
        self._write_audit_log(event)
    
    def _write_audit_log(self, event: Dict) -> None:
        """Write event to audit log"""
        try:
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(event) + '\n')
        except Exception as e:
            logger.error(f"Failed to write audit log: {str(e)}")
    
    def retrieve_audit_logs(self, filters: Dict = None) -> list:
        """
        Retrieve audit logs with optional filtering
        
        Args:
            filters: Dictionary of filter criteria
            
        Returns:
            List of audit events
        """
        events = []
        
        try:
            if not os.path.exists(self.log_file):
                return events
            
            with open(self.log_file, 'r') as f:
                for line in f:
                    try:
                        event = json.loads(line)
                        
                        # Apply filters if provided
                        if filters:
                            if self._matches_filters(event, filters):
                                events.append(event)
                        else:
                            events.append(event)
                    except json.JSONDecodeError:
                        continue
        
        except Exception as e:
            logger.error(f"Failed to retrieve audit logs: {str(e)}")
        
        return events
    
    def _matches_filters(self, event: Dict, filters: Dict) -> bool:
        """Check if event matches filter criteria"""
        for key, value in filters.items():
            if key not in event:
                return False
            
            if isinstance(value, list):
                if event[key] not in value:
                    return False
            else:
                if event[key] != value:
                    return False
        
        return True
    
    def export_audit_report(self, output_file: str, filters: Dict = None) -> bool:
        """Export audit log to file"""
        try:
            events = self.retrieve_audit_logs(filters)
            
            with open(output_file, 'w') as f:
                f.write(json.dumps(events, indent=2, default=str))
            
            logger.info(f"Audit report exported to {output_file}")
            return True
        
        except Exception as e:
            logger.error(f"Failed to export audit report: {str(e)}")
            return False
