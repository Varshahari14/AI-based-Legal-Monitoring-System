# AI-Based Legal Monitoring System

A comprehensive AI-powered platform for tracking, analyzing, and managing legal updates from government agencies, courts, and regulatory bodies.

## Architecture

```
Legal Sources (Govt, Courts, Regulators)
            ↓
Data Collection (Scraper/API)
            ↓
Document Processing (NLP Engine)
            ↓
AI Chatbot Analysis Engine
            ↓
Impact Analysis Module
            ↓
Compliance Recommendation Engine
            ↓
Outputs:
   • Alerts (Email/SMS)
   • Dashboard
   • Audit Logs
```

## Features

### 1. **Data Collection**
- Web scraping from government, court, and regulatory sources
- Multi-source document aggregation
- Automatic URL fetching with error handling

### 2. **Document Processing**
- NLP-powered text summarization
- Named entity extraction (persons, organizations, dates, laws, penalties)
- Section identification and extraction
- Key phrase extraction

### 3. **Impact Analysis**
- Business impact assessment across 8 categories:
  - Data & Privacy
  - Employment
  - Financial
  - Operations
  - Marketing & Advertising
  - Environmental
  - Safety & Health
  - Consumer Protection
- Department-level impact mapping

### 4. **Compliance Engine**
- Automated recommendation generation
- Deadline calculation and prioritization
- Compliance scoring
- Risk level assessment

### 5. **Alert System**
- Email alerts with formatted templates
- SMS alert support (Twilio)
- Bulk alert distribution
- Configurable alert levels

### 6. **Audit Trail**
- Comprehensive event logging
- Document tracking
- User action logging
- Error tracking
- Audit report generation

### 7. **Dashboard**
- RESTful API for frontend integration
- Real-time compliance metrics
- Document management interface
- Alert history and details
- Recommendation tracking

## System Structure

```
AI-Legal-Monitoring/
├── src/
│   ├── data_collection/      # Web scraping modules
│   ├── document_processing/  # NLP and text analysis
│   ├── analysis/             # Impact & compliance modules
│   ├── alerts/              # Alert management
│   ├── audit/               # Audit logging
│   ├── dashboard/           # API endpoints
│   └── main.py              # System orchestrator
├── config/
│   └── settings.py          # Configuration
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── .env.example            # Environment setup
└── README.md               # Documentation
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Varshahari14/AI-based-Legal-Monitoring-System.git
cd AI-Legal-Monitoring
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Download NLP models**
```bash
python -m spacy download en_core_web_lg
```

## Usage

### Quick Start

```python
from src.main import LegalMonitoringSystem

# Initialize system
system = LegalMonitoringSystem()

# Process a legal document
result = system.process_legal_content("https://example.com/legal-update")

# Send alerts
system.send_alerts(result, ['user@example.com'])

# Start dashboard
system.start_dashboard()
```

### Web Dashboard

The system includes a modern web interface for monitoring and management.

#### Quick Web Start

1. **Install web dependencies**
```bash
pip install -r requirements-web.txt
```

2. **Run the web application**
```bash
python web_app.py
```
Or use the batch file:
```bash
run_web.bat  # Windows only
```

3. **Access the dashboard**
```
http://localhost:5000
```

#### Web Features

- **Real-time Dashboard**: Live metrics and system status
- **Document Processing**: Process legal documents by URL
- **Interactive Charts**: Compliance status, risk distribution, activity trends
- **Alert Management**: View and manage active alerts
- **Recommendation Tracking**: Monitor pending compliance actions
- **Audit Logging**: Complete activity history
- **Responsive Design**: Works on desktop and mobile

#### Web API Endpoints

- `GET /api/dashboard` - Dashboard overview data
- `GET /api/documents` - Processed documents
- `GET /api/alerts` - Active alerts
- `GET /api/recommendations` - Pending recommendations
- `GET /api/audit-logs` - Audit logs
- `POST /api/process-document` - Process new document

### API Endpoints

- `GET /api/health` - Health check
- `GET /api/dashboard` - Dashboard overview
- `GET /api/alerts` - Active alerts
- `GET /api/documents` - Processed documents
- `GET /api/compliance` - Compliance status
- `GET /api/recommendations` - Recommendations
- `GET /api/audit-logs` - Audit trail
- `GET /api/document/<doc_id>` - Document details

## Output Format

### Structured Analysis Result

```json
{
  "status": "completed",
  "analysis": {
    "document": {
      "title": "Document Title",
      "summary": "Concise summary...",
      "url": "source_url",
      "extracted_at": "2024-01-01T12:00:00"
    },
    "impact_analysis": {
      "affected_categories": ["Data & Privacy", "Employment"],
      "overall_impact_level": "High"
    },
    "recommendations": [
      {
        "action": "Update privacy policy",
        "urgency": "High",
        "timeline": "14 days",
        "responsible": "Legal",
        "deadline": "2024-01-15T12:00:00"
      }
    ],
    "risk_assessment": {
      "overall_risk_level": "High",
      "critical_risks": 1,
      "high_risks": 3
    }
  }
}
```

## Configuration

Edit `.env` file to customize:

```env
# Database
DATABASE_URL=sqlite:///./legal_monitor.db

# Email Alerts
SMTP_SERVER=smtp.gmail.com
SENDER_EMAIL=your_email@gmail.com

# API
API_HOST=0.0.0.0
API_PORT=5000

# NLP Models
NLP_MODEL=en_core_web_lg
```

## Compliance Output

### Summary
- Executive overview of legal change
- Source and date

### Key Changes
- Sections affected
- Regulatory amendments
- Penalties for non-compliance

### Impact Analysis
- Affected business areas
- Operational changes needed
- Risk level assessment

### Recommended Actions
- Prioritized compliance tasks
- Deadlines and responsible parties
- Resource requirements

### Risk Level
- Low: Minor changes, simple compliance
- Medium: Moderate impact, multiple changes
- High: Critical impact, immediate action required

## Risk Assessment

Risk levels are determined by:
- Number of affected business areas
- Severity of impact (penalties, restrictions)
- Implementation timeline
- Resource requirements

## Audit Trail Features

- Document processing tracking
- All alerts and recommendations logged
- User actions recorded
- Error tracking for compliance
- Export capability for audits

## Development

### Running Tests
```bash
pytest tests/
```

### Adding New Data Sources
1. Create new scraper in `data_collection/`
2. Implement `fetch_content()` method
3. Register in `main.py`

### Customizing Impact Analysis
1. Edit `BUSINESS_CATEGORIES` in `impact_analyzer.py`
2. Add keywords for new categories
3. Update department mapping

## Performance Considerations

- Document processing uses batching for large documents
- NLP model loading cached in memory
- Alert emails sent asynchronously
- Audit logs rotated to prevent filesystem overflow

## Security

- Environment variables for sensitive data
- SQL injection protection via ORM
- SMTP authentication for email
- Audit trail for compliance

## Roadmap

- [ ] Machine learning model fine-tuning
- [ ] Multi-language support
- [ ] Advanced visualization dashboard
- [ ] Integration with legal databases
- [ ] Predictive compliance alerts
- [ ] Mobile app support

## Troubleshooting

### NLP Model Not Found
```bash
python -m spacy download en_core_web_lg
```

### Email Not Sending
- Verify SMTP credentials in `.env`
- Check Gmail app password (if using Gmail)
- Ensure "Less secure apps" enabled

### High Memory Usage
- Reduce batch size in `config/settings.py`
- Use smaller NLP models
- Clear cache regularly

## Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - See LICENSE file for details

## Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: support@legalmonioring.com

## Support

Documentation: [docs/](./docs/)
Examples: [examples/](./examples/)
FAQs: [docs/FAQ.md](./docs/FAQ.md)

---

**AI Legal Monitoring System v1.0.0**
*Ensuring compliance through intelligent legal monitoring*
