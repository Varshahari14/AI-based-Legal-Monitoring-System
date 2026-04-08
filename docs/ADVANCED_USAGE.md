"""
Advanced Usage Guide for AI Legal Monitoring System
"""

# Advanced Usage Scenarios

## Scenario 1: Custom Legal Source Integration

```python
from src.data_collection.scraper import LegalDataScraper
from src.document_processing.nlp_engine import LegalNLPEngine

class CustomLegalSource:
    def __init__(self):
        self.scraper = LegalDataScraper()
        self.nlp = LegalNLPEngine()
    
    def process_custom_source(self, source_data):
        # Process data from custom API or database
        document = {
            'content': source_data['text'],
            'source': 'custom-api',
            'title': source_data['title'],
            'url': source_data['url']
        }
        
        return self.nlp.process_document(document)
```

## Scenario 2: Automated Monitoring and Alerts

```python
import schedule
import time
from src.main import LegalMonitoringSystem

system = LegalMonitoringSystem()

def check_legal_updates():
    # Define monitoring sources
    sources = [
        'https://example.gov/updates',
        'https://courts.example.gov/decisions'
    ]
    
    for source in sources:
        result = system.process_legal_content(source)
        
        if result.get('status') == 'completed':
            # Send alerts if high risk
            if result['analysis']['risk_assessment']['overall_risk_level'] == 'High':
                system.send_alerts(result, ['legal@company.com'])

# Schedule daily checks
schedule.every().day.at("09:00").do(check_legal_updates)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Scenario 3: Custom Impact Analysis

```python
from src.analysis.impact_analyzer import ImpactAnalyzer

class IndustrySpecificImpactAnalyzer(ImpactAnalyzer):
    def __init__(self, industry='finance'):
        super().__init__()
        self.industry = industry
        self.industry_keywords = self._load_industry_keywords()
    
    def _load_industry_keywords(self):
        # Load industry-specific keywords
        return {
            'finance': ['banking', 'lending', 'interest rates', 'securities'],
            'healthcare': ['HIPAA', 'patient privacy', 'medical records'],
            'retail': ['consumer data', 'pricing', 'product liability']
        }
    
    def analyze_impact(self, document):
        base_impact = super().analyze_impact(document)
        
        # Add industry-specific analysis
        text = (document.get('summary', '') + ' ' + 
                document.get('content', '')).lower()
        
        industry_matches = sum(
            1 for keyword in self.industry_keywords.get(self.industry, [])
            if keyword in text
        )
        
        if industry_matches > 0:
            base_impact['industry_specific_impact'] = True
        
        return base_impact
```

## Scenario 4: Database Integration

```python
from sqlalchemy import create_engine, Column, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class LegalDocument(Base):
    __tablename__ = "legal_documents"
    
    id = Column(String(255), primary_key=True)
    url = Column(String(500), unique=True)
    source = Column(String(100))
    title = Column(String(500))
    summary = Column(String(5000))
    impact_analysis = Column(JSON)
    recommendations = Column(JSON)
    processed_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50))

# Create database session
engine = create_engine('sqlite:///legal_monitor.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_processed_document(result):
    session = Session()
    analysis = result.get('analysis', {})
    
    doc = LegalDocument(
        id=analysis['document']['url'],
        url=analysis['document']['url'],
        source=analysis['document'].get('source'),
        title=analysis['document']['title'],
        summary=analysis['document']['summary'],
        impact_analysis=analysis['impact_analysis'],
        recommendations=analysis['recommendations'],
        status='processed'
    )
    
    session.add(doc)
    session.commit()
    session.close()
```

## Scenario 5: Multi-Department Compliance Tracking

```python
from src.analysis.impact_analyzer import ImpactAnalyzer

def track_department_compliance(document, departments=['Legal', 'HR', 'IT']):
    analyzer = ImpactAnalyzer()
    impact = analyzer.analyze_impact(document)
    
    affected_departments = analyzer.identify_affected_departments(impact)
    
    tracking = {}
    for dept in departments:
        if dept in affected_departments:
            tracking[dept] = {
                'affected': True,
                'categories': affected_departments[dept],
                'responsible_person': get_department_head(dept),
                'priority': 'High'
            }
        else:
            tracking[dept] = {
                'affected': False,
                'priority': 'None'
            }
    
    return tracking

def get_department_head(department):
    dept_heads = {
        'Legal': 'General Counsel',
        'HR': 'HR Director',
        'IT': 'CTO',
        'Finance': 'CFO',
        'Operations': 'COO'
    }
    return dept_heads.get(department)
```

## Scenario 6: Cloud Storage Integration

```python
import boto3
import json
from datetime import datetime

class S3AuditStorage:
    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
    
    def save_analysis(self, result):
        key = f"legal-analysis/{datetime.now().strftime('%Y/%m/%d')}/{result['analysis']['document']['url'].replace('/', '_')}.json"
        
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=json.dumps(result, indent=2, default=str),
            ContentType='application/json',
            ServerSideEncryption='AES256'
        )
    
    def retrieve_analysis(self, doc_url, date):
        key = f"legal-analysis/{date}/{doc_url.replace('/', '_')}.json"
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        return json.loads(response['Body'].read())
```

## Scenario 7: Machine Learning Model Fine-tuning

```python
from transformers import DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch

class LegalComplianceClassifier:
    def __init__(self):
        self.model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')
    
    def fine_tune_on_custom_data(self, training_data):
        """
        Fine-tune model on custom legal compliance data
        training_data: List of (text, label) tuples
        """
        # Prepare training arguments
        training_args = TrainingArguments(
            output_dir='./models/legal-classifier',
            num_train_epochs=3,
            per_device_train_batch_size=8,
            save_steps=100,
            save_total_limit=2,
        )
        
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=training_data
        )
        
        trainer.train()
    
    def predict_compliance_risk(self, text):
        inputs = torch.tensor([self.tokenizer.encode(text)])
        outputs = self.model(inputs)
        logits = outputs[0]
        
        risk_scores = torch.softmax(logits, dim=1).detach().numpy()[0]
        
        return {
            'low_risk': risk_scores[0],
            'medium_risk': risk_scores[1],
            'high_risk': risk_scores[2]
        }
```

## Scenario 8: Real-time Dashboard with WebSockets

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    emit('response', {'data': 'Connected to Legal Monitor Dashboard'})

@socketio.on('request_update')
def handle_update_request():
    # Process new document
    result = system.process_legal_content(request.args.get('url'))
    
    # Broadcast to all connected clients
    socketio.emit('update', {
        'document': result['analysis']['document'],
        'impact': result['analysis']['impact_analysis']
    }, broadcast=True)

def emit_alerts(alert_data):
    socketio.emit('alert', alert_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=False)
```

## Scenario 9: Compliance Report Generation

```python
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def generate_compliance_report(analysis_results):
    filename = f"compliance_report_{datetime.now().strftime('%Y%m%d')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph("Compliance Compliance Report", styles['Heading1'])
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Document Summary
    for result in analysis_results:
        doc_title = result['analysis']['document']['title']
        elements.append(Paragraph(f"Document: {doc_title}", styles['Heading2']))
        
        summary = result['analysis']['document']['summary']
        elements.append(Paragraph(summary, styles['BodyText']))
        elements.append(Spacer(1, 12))
        
        # Recommendations Table
        rec_data = [['Action', 'Urgency', 'Deadline', 'Responsible']]
        for rec in result['analysis']['recommendations'][:5]:
            rec_data.append([
                rec['action'][:30],
                rec['urgency'],
                rec['deadline'][:10],
                rec['responsible']
            ])
        
        rec_table = Table(rec_data)
        elements.append(rec_table)
        elements.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(elements)
    return filename
```

## Scenario 10: Notification Preferences

```python
class NotificationManager:
    def __init__(self):
        self.preferences = {}
    
    def set_user_preferences(self, user_id, preferences):
        self.preferences[user_id] = {
            'email_enabled': preferences.get('email', True),
            'sms_enabled': preferences.get('sms', False),
            'notification_level': preferences.get('level', 'Medium'),  # Low, Medium, High
            'preferred_time': preferences.get('time', '09:00'),
            'categories': preferences.get('categories', [])
        }
    
    def should_notify(self, user_id, alert_data):
        prefs = self.preferences.get(user_id, {})
        
        # Check notification level
        if alert_data['risk_level'] == 'Low' and prefs['notification_level'] == 'High':
            return False
        
        # Check category interest
        if prefs['categories'] and alert_data['category'] not in prefs['categories']:
            return False
        
        return True
```

These scenarios demonstrate the flexibility and extensibility of the AI Legal Monitoring System.
