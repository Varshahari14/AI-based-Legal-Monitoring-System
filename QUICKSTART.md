# Quick Start Guide

## 5-Minute Setup

### 1. Install Dependencies
```bash
cd AI-Legal-Monitoring
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your email settings
```

### 3. Run Example
```bash
python examples/usage_example.py
```

### 4. Start Dashboard API
```bash
python -c "from src.main import LegalMonitoringSystem; s = LegalMonitoringSystem(); s.start_dashboard()"
```

Access dashboard at: `http://localhost:5000`

---

## Basic Usage

### Process a Legal Document

```python
from src.main import LegalMonitoringSystem

system = LegalMonitoringSystem()

# Process document
result = system.process_legal_content("https://example.com/legal-update")

# Check results
print(f"Risk Level: {result['analysis']['risk_assessment']['overall_risk_level']}")
print(f"Affected: {result['analysis']['impact_analysis']['affected_categories']}")

# Send alerts
system.send_alerts(result, ['legal@company.com'])
```

### Run Tests
```bash
python -m pytest tests/
```

---

## Key Features

| Feature | Module | Usage |
|---------|--------|-------|
| **Data Scraping** | `data_collection/scraper.py` | Fetch legal documents |
| **NLP Processing** | `document_processing/nlp_engine.py` | Summarize and extract entities |
| **Impact Analysis** | `analysis/impact_analyzer.py` | Identify business impact |
| **Recommendations** | `analysis/compliance_engine.py` | Generate action items |
| **Alerts** | `alerts/alert_manager.py` | Send notifications |
| **Audit Trail** | `audit/audit_logger.py` | Track all activities |
| **API** | `dashboard/api.py` | REST endpoints |

---

## API Endpoints

```
GET  /api/health             - System status
GET  /api/dashboard          - Overview metrics
GET  /api/documents          - Processed documents
GET  /api/alerts             - Active alerts
GET  /api/compliance         - Compliance status
GET  /api/recommendations    - Pending actions
GET  /api/audit-logs         - Activity logs
GET  /api/document/<id>      - Document details
```

---

## Common Tasks

### ✅ Send Alert to Specific Department

```python
legal_team = ['legal@company.com', 'counsel@company.com']
system.send_alerts(result, legal_team)
```

### ✅ Get Compliance Score

```python
status = system.get_compliance_status()
print(f"Score: {status['compliance_score']}%")
```

### ✅ Check Audit Logs

```python
logs = system.audit_logger.retrieve_audit_logs(
    filters={'event_type': 'ALERT_SENT'}
)
print(f"Alerts sent: {len(logs)}")
```

### ✅ Export Audit Report

```python
system.audit_logger.export_audit_report(
    'annual_audit_report.json',
    filters={'event_type': 'DOCUMENT_PROCESSED'}
)
```

---

## Configuration

### Email Alerts
```env
SMTP_SERVER=smtp.gmail.com
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
ALERT_EMAIL_ENABLED=True
```

### Database
```env
DATABASE_URL=sqlite:///./legal_monitor.db
# Or: postgresql://user:password@localhost/legal_db
```

### NLP Models
```env
NLP_MODEL=en_core_web_lg
TRANSFORMERS_MODEL=distilbert-base-uncased
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **NLP Model Not Found** | Run: `python -m spacy download en_core_web_lg` |
| **Email Not Sending** | Check SMTP credentials in `.env` |
| **High Memory Usage** | Reduce batch size in `config/settings.py` |
| **Connection Timeout** | Increase `SCRAPER_TIMEOUT` in `.env` |

---

## Next Steps

1. **Customize Data Sources**: Add your own URLs in `config/settings.py`
2. **Fine-tune NLP Models**: See [ADVANCED_USAGE.md](docs/ADVANCED_USAGE.md)
3. **Integrate Database**: Use SQLAlchemy models in examples
4. **Build Frontend**: Use dashboard API to create UI
5. **Deploy**: Use Docker or cloud platform

---

## Example Output

```json
{
  "status": "completed",
  "analysis": {
    "document": {
      "title": "New Data Privacy Regulation",
      "summary": "This regulation requires user consent...",
      "extracted_at": "2024-01-15T10:30:00"
    },
    "impact_analysis": {
      "affected_categories": ["Data & Privacy", "Operations"],
      "overall_impact_level": "High"
    },
    "recommendations": [
      {
        "action": "Update privacy policy",
        "urgency": "High",
        "deadline": "2024-01-22",
        "responsible": "Legal"
      }
    ],
    "risk_assessment": {
      "overall_risk_level": "High",
      "requires_immediate_action": true
    }
  }
}
```

---

## Support

- **Documentation**: [README.md](README.md)
- **API Reference**: [docs/API.md](docs/API.md)
- **Advanced Usage**: [docs/ADVANCED_USAGE.md](docs/ADVANCED_USAGE.md)
- **Examples**: [examples/usage_example.py](examples/usage_example.py)

---

## Quick Links

- [GitHub](https://github.com/Varshahari14/AI-based-Legal-Monitoring-System)
- [Issues](https://github.com/Varshahari14/AI-based-Legal-Monitoring-System/issues)
- [Discussions](https://github.com/Varshahari14/AI-based-Legal-Monitoring-System/discussions)

---

**Ready to monitor legal updates? Start with:** `python examples/usage_example.py`
