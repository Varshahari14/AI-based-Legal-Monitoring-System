"""
Alert Manager
Sends alerts via Email and SMS
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class AlertManager:
    """Manages alerts and notifications"""
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """Initialize alert manager"""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_email_alert(self, recipient_email: str, subject: str, body: str, 
                        html_body: str = None) -> bool:
        """
        Send email alert
        
        Args:
            recipient_email: Recipient email address
            subject: Email subject
            body: Plain text body
            html_body: HTML body (optional)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
            
            # Attach plain text part
            part1 = MIMEText(body, 'plain')
            msg.attach(part1)
            
            # Attach HTML part if provided
            if html_body:
                part2 = MIMEText(html_body, 'html')
                msg.attach(part2)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            logger.info(f"Email alert sent to {recipient_email}")
            return True
        
        except Exception as e:
            logger.error(f"Failed to send email alert: {str(e)}")
            return False
    
    def generate_alert_email(self, alert_data: Dict) -> tuple:
        """
        Generate formatted alert email
        
        Args:
            alert_data: Alert information
            
        Returns:
            Tuple of (subject, plain_body, html_body)
        """
        risk_level = alert_data.get('risk_level', 'Medium')
        subject = f"[{risk_level}] Legal Compliance Alert - {alert_data.get('title', 'Update')}"
        
        plain_body = f"""
Legal Compliance Update Alert

Title: {alert_data.get('title', 'N/A')}
Date: {alert_data.get('date', datetime.now().isoformat())}
Risk Level: {risk_level}
Source: {alert_data.get('source', 'Unknown')}

Summary:
{alert_data.get('summary', 'N/A')}

Affected Areas:
{', '.join(alert_data.get('affected_areas', ['N/A']))}

Recommended Actions:
{chr(10).join(f"• {action}" for action in alert_data.get('actions', ['Review the update']))}

Impact Level: {alert_data.get('impact_level', 'Medium')}

Please review and take necessary compliance actions.

---
AI Legal Monitoring System
"""
        
        html_body = f"""
<html>
<head></head>
<body>
    <h2>Legal Compliance Update Alert</h2>
    <p><strong>Title:</strong> {alert_data.get('title', 'N/A')}</p>
    <p><strong>Date:</strong> {alert_data.get('date', datetime.now().isoformat())}</p>
    <p><strong>Risk Level:</strong> <span style="color: red; font-weight: bold;">{risk_level}</span></p>
    <p><strong>Source:</strong> {alert_data.get('source', 'Unknown')}</p>
    
    <h3>Summary</h3>
    <p>{alert_data.get('summary', 'N/A')}</p>
    
    <h3>Affected Areas</h3>
    <ul>
        {''.join(f"<li>{area}</li>" for area in alert_data.get('affected_areas', ['N/A']))}
    </ul>
    
    <h3>Recommended Actions</h3>
    <ul>
        {''.join(f"<li>{action}</li>" for action in alert_data.get('actions', ['Review the update']))}
    </ul>
    
    <p><strong>Impact Level:</strong> {alert_data.get('impact_level', 'Medium')}</p>
    <p>Please review and take necessary compliance actions.</p>
</body>
</html>
"""
        
        return subject, plain_body, html_body
    
    def send_bulk_alerts(self, recipients: List[str], alert_data: Dict) -> Dict:
        """
        Send alerts to multiple recipients
        
        Args:
            recipients: List of email addresses
            alert_data: Alert information
            
        Returns:
            Results summary
        """
        subject, plain_body, html_body = self.generate_alert_email(alert_data)
        
        results = {
            'total': len(recipients),
            'sent': 0,
            'failed': 0,
            'failed_recipients': []
        }
        
        for recipient in recipients:
            if self.send_email_alert(recipient, subject, plain_body, html_body):
                results['sent'] += 1
            else:
                results['failed'] += 1
                results['failed_recipients'].append(recipient)
        
        return results
    
    def format_sms_alert(self, alert_data: Dict, max_chars: int = 160) -> str:
        """Format alert for SMS (160 char limit)"""
        title = alert_data.get('title', 'Legal Update')
        risk = alert_data.get('risk_level', 'M')
        
        message = f"LEGAL ALERT [{risk}] {title[:50]}... Check dashboard for details."
        
        return message[:max_chars]
