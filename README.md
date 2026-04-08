# AI-Based Legal Monitoring System

A comprehensive AI-powered platform for tracking, analyzing, and managing legal updates from government agencies, courts, and regulatory bodies.

## Architecture

```
Legal Sources (Govt, Courts, Regulators)
            ↓
Data Collection Module (Scraper / API)
            ↓
Document Processing (NLP Engine)
   • Text cleaning
   • Entity extraction
   • Section identification
            ↓
Legal Change Detection Engine
   • Compare old vs new versions
   • Detect modifications, additions, deletions
            ↓
AI Analysis Engine (Chatbot / LLM)
   • Summary generation
   • Key change extraction
            ↓
Impact Analysis Module
   • Map impact to departments
   • Categorize business impact
            ↓
Explainable Risk Engine
   • Calculate risk score
   • Provide reasoning (why risk is high/medium/low)
            ↓
Compliance Engine
   • Generate action items
   • Update internal policies automatically
   • Maintain version control
            ↓
Smart Alert System
   • Assign priority (Critical / High / Medium / Low)
   • Send Email / SMS alerts
            ↓
Dashboard & API Layer
   • Display insights
   • Show compliance score
   • Track recommendations
            ↓
Audit Trail System
   • Log all actions
   • Store history of changes
   • Ensure compliance tracking
```

## Features

### 1. **Data Collection Module**
- Web scraping from government, court, and regulatory sources
- Multi-source document aggregation
- Automatic URL fetching with error handling
- API-based data collection for multiple jurisdictions

### 2. **Document Processing (NLP Engine)**
- Text cleaning and normalization
- Named entity extraction (persons, organizations, dates, laws, penalties)
- Section identification and extraction
- Key phrase extraction and summarization

### 3. **Legal Change Detection Engine**
- Compare old vs new document versions
- Detect modifications, additions, and deletions
- Track regulatory amendment history
- Version control and change tracking

### 4. **AI Analysis Engine (Chatbot / LLM)**
- Intelligent summary generation
- Key change extraction and explanation
- Natural language processing for legal documents
- Context-aware interpretation

### 5. **Impact Analysis Module**
- Business impact assessment across departments
- Categorize impact within 8 legal categories:
  - Data & Privacy
  - Employment
  - Financial
  - Operations
  - Marketing & Advertising
  - Environmental
  - Safety & Health
  - Consumer Protection
- Department-level impact mapping (HR, Finance, IT, Operations, etc.)

### 6. **Explainable Risk Engine**
- Risk score calculation (0-100)
- Multi-factor risk assessment
- Clear reasoning for risk level (High/Medium/Low/Critical)
- Transparency in risk evaluation

### 7. **Compliance Engine**
- Automated action item generation
- Internal policy updates
- Version control for compliance documents
- Deadline calculation and prioritization
- Compliance scoring

### 8. **Smart Alert System**
- Intelligent priority assignment (Critical/High/Medium/Low)
- Email alerts with formatted templates
- SMS alert support (Twilio)
- Bulk alert distribution
- Configurable alert thresholds

### 9. **Dashboard & API Layer**
- RESTful API for frontend integration
- Real-time compliance metrics
- Interactive data visualization
- Document management interface
- Alert history and details
- Recommendation tracking

### 10. **Audit Trail System**
- Comprehensive event logging
- Document processing tracking
- User action logging
- Error tracking for compliance
- Audit report generation
- Change history maintenance

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

## System Objectives & Specifications

### 🎯 Task Objectives

The AI Legal Monitoring System is engineered to analyze legal updates and provide structured, actionable insights for organizations. Given a legal document, regulation, or update, the system performs:

1. **Document Summarization**
   - Summarize the document in simple, clear language
   - Extract executive summary
   - Identify document type and source

2. **Key Change Identification**
   - Identify modified sections
   - Detect new rules introduced
   - Find removed clauses
   - Highlight changes in penalties or deadlines

3. **Impact Analysis**
   - Identify affected business areas (HR, Finance, IT, Operations, etc.)
   - Explain how each area is impacted
   - Map impact to organizational departments
   - Prioritize impact areas by severity

4. **Risk Assessment**
   - Assign risk level (Low / Medium / High / Critical)
   - Generate a risk score (0–100)
   - Clearly explain reasons for the risk level
   - Provide transparency in risk evaluation

5. **Compliance Recommendations**
   - Generate immediate actions
   - Suggest long-term actions
   - Assign responsible departments
   - Calculate suggested deadlines

6. **Jurisdiction Identification**
   - Identify country
   - Determine regulatory authority
   - Assess applicability to organization

7. **Alert Prioritization**
   - Assign priority: Critical / High / Medium / Low
   - Based on risk level and organizational impact

### 📊 Mandatory Output Format (JSON)

All legal analysis outputs conform to the following specification:

```json
{
  "summary": "Clear, executive summary of the legal document in non-technical language",
  "key_changes": [
    {
      "type": "Modification/Add/Delete",
      "section": "Name of affected section",
      "description": "Clear description of what changed and why it matters"
    }
  ],
  "impact_analysis": {
    "affected_departments": ["HR", "Finance", "IT", "Operations"],
    "details": "Detailed explanation of how each department is impacted",
    "business_areas_affected": ["Data & Privacy", "Employment", "Financial Operations"]
  },
  "risk_assessment": {
    "level": "High",
    "score": 82,
    "reasons": [
      "High penalty increase from $X to $Y",
      "Multiple departments affected",
      "Short compliance deadline (30 days)"
    ],
    "critical_factors": []
  },
  "compliance_actions": [
    {
      "action": "Specific action to take",
      "type": "Immediate/Long-term",
      "priority": "Critical/High/Medium/Low",
      "responsible_department": "Legal/HR/IT",
      "estimated_effort": "Days/Weeks",
      "deadline": "YYYY-MM-DD",
      "success_criteria": "How to verify compliance"
    }
  ],
  "jurisdiction": {
    "country": "United States",
    "state_province": "California (if applicable)",
    "regulatory_authority": "California Department of Consumer Affairs",
    "applicability": "Applies to all companies processing California residents' data"
  },
  "alert_priority": "Critical",
  "metadata": {
    "document_date": "YYYY-MM-DD",
    "effective_date": "YYYY-MM-DD",
    "processing_timestamp": "ISO 8601 timestamp",
    "confidence_score": 0.95
  }
}
```

### ⚠️ Processing Instructions

When analyzing legal documents, follow these guidelines:

- **Use simple, clear language** - Avoid legal jargon when explaining to business stakeholders
- **Be precise and structured** - Follow the output format specification exactly
- **Handle missing data gracefully** - Make reasonable assumptions and document them explicitly
- **Focus on compliance, risk, and business impact** - Prioritize actionable insights
- **Ensure completeness** - Always provide all fields in the output format
- **Maintain accuracy** - When in doubt, mark sections as uncertain or requiring manual review
- **Provide reasoning** - Explain the "why" behind risk assessments and recommendations
- **Consider organizational context** - Tailor impact analysis to company type and size
- **Track deadline urgency** - Highlight documents with imminent compliance deadlines

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
