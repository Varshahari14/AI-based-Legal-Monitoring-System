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

## 🎨 Modern Frontend Architecture (React + TypeScript)

The redesigned frontend provides an intuitive, modern dashboard for legal compliance management.

### Frontend Structure

```
frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── Dashboard/
│   │   │   ├── DashboardHome.tsx
│   │   │   ├── MetricCard.tsx
│   │   │   ├── RiskDistributionChart.tsx
│   │   │   └── RecentUpdates.tsx
│   │   ├── LegalUpdates/
│   │   │   ├── DocumentList.tsx
│   │   │   ├── DocumentFilter.tsx
│   │   │   └── DocumentDetailModal.tsx
│   │   ├── DocumentAnalysis/
│   │   │   ├── AnalysisHeader.tsx
│   │   │   ├── SummarySection.tsx
│   │   │   ├── KeyChangesPanel.tsx
│   │   │   ├── ImpactAnalysis.tsx
│   │   │   ├── RiskAssessment.tsx
│   │   │   └── ComplianceActions.tsx
│   │   ├── Alerts/
│   │   │   ├── AlertList.tsx
│   │   │   ├── AlertCard.tsx
│   │   │   ├── AlertPriority.tsx
│   │   │   └── AlertActions.tsx
│   │   ├── ComplianceTracker/
│   │   │   ├── TaskBoard.tsx
│   │   │   ├── TaskCard.tsx
│   │   │   ├── KanbanView.tsx
│   │   │   └── DeadlineReminders.tsx
│   │   ├── AuditLogs/
│   │   │   ├── LogTimeline.tsx
│   │   │   ├── LogFilter.tsx
│   │   │   └── LogExport.tsx
│   │   ├── Common/
│   │   │   ├── Navbar.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── BreadcrumbNav.tsx
│   │   │   ├── LoadingSpinner.tsx
│   │   │   ├── ErrorBoundary.tsx
│   │   │   ├── TooltipHelper.tsx
│   │   │   └── Modal.tsx
│   ├── pages/
│   │   ├── DashboardPage.tsx
│   │   ├── LegalUpdatesPage.tsx
│   │   ├── DocumentAnalysisPage.tsx
│   │   ├── AlertsPage.tsx
│   │   ├── ComplianceTrackerPage.tsx
│   │   ├── AuditLogsPage.tsx
│   │   ├── LoginPage.tsx
│   │   └── NotFoundPage.tsx
│   ├── hooks/
│   │   ├── useDocuments.ts
│   │   ├── useAlerts.ts
│   │   ├── useAnalysis.ts
│   │   └── useAuth.ts
│   ├── services/
│   │   ├── api.ts
│   │   ├── authService.ts
│   │   └── documentService.ts
│   ├── types/
│   │   ├── document.ts
│   │   ├── alert.ts
│   │   ├── analysis.ts
│   │   └── compliance.ts
│   ├── styles/
│   │   ├── colors.ts
│   │   ├── spacing.ts
│   │   └── global.css
│   ├── utils/
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   └── helpers.ts
│   └── App.tsx
├── package.json
└── tsconfig.json
```

### Key Features

- **React Hooks**: State management with custom hooks
- **TypeScript**: Full type safety
- **Tailwind CSS**: Modern utility-first styling
- **Material-UI Icons**: Professional icon library
- **Recharts**: Interactive data visualizations
- **React Router**: Client-side routing
- **Axios**: HTTP client with interceptors

---

## ⚙️ Modern Backend Architecture (FastAPI + PostgreSQL)

A scalable, high-performance backend using async Python.

### Backend Structure

```
backend/
├── app/
│   ├── main.py                    # FastAPI app initialization
│   ├── config.py                  # Configuration settings
│   ├── dependencies.py            # Shared dependencies
│   ├── api/
│   │   ├── routes/
│   │   │   ├── documents.py       # Document endpoints
│   │   │   ├── analysis.py        # Analysis endpoints
│   │   │   ├── alerts.py          # Alert endpoints
│   │   │   ├── compliance.py      # Compliance endpoints
│   │   │   ├── audit.py           # Audit log endpoints
│   │   │   ├── auth.py            # Authentication endpoints
│   │   │   └── health.py          # Health check
│   │   └── models/
│   │       ├── document.py        # Pydantic schemas
│   │       ├── alert.py
│   │       ├── analysis.py
│   │       └── compliance.py
│   ├── core/
│   │   ├── security.py            # JWT, password hashing
│   │   ├── logging.py             # Logging configuration
│   │   └── exceptions.py          # Custom exceptions
│   ├── db/
│   │   ├── database.py            # Database connection
│   │   ├── models.py              # SQLAlchemy models
│   │   └── migrations/            # Alembic migrations
│   ├── services/
│   │   ├── document_service.py    # Business logic
│   │   ├── analysis_service.py
│   │   ├── alert_service.py
│   │   ├── compliance_service.py
│   │   ├── change_detection.py
│   │   └── risk_engine.py
│   ├── processors/
│   │   ├── legal_processor.py     # Document processing
│   │   ├── nlp_engine.py          # Text analysis
│   │   └── impact_analyzer.py
│   └── utils/
│       ├── constants.py
│       ├── helpers.py
│       └── validators.py
├── tests/
│   ├── test_api.py
│   ├── test_services.py
│   └── test_processors.py
├── requirements.txt
└── .env.example
```

### Technology Stack

- **FastAPI**: Modern, fast web framework
- **PostgreSQL**: Robust relational database
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation and serialization
- **Alembic**: Database migrations
- **Celery**: Async task queue for heavy processing
- **Redis**: Caching and message broker
- **JWT**: Secure authentication
- **Pytest**: Testing framework

---

## 📊 Database Schema (PostgreSQL)

### Tables Design

```sql
-- Users table for authentication
CREATE TABLE users (
    id UUID PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    department VARCHAR(100),
    role VARCHAR(50) CHECK (role IN ('admin', 'analyst', 'reviewer')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Legal documents table
CREATE TABLE documents (
    id UUID PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    content TEXT NOT NULL,
    url VARCHAR(2048),
    source VARCHAR(255),
    document_type VARCHAR(100),
    jurisdiction VARCHAR(100),
    effective_date DATE,
    processed_at TIMESTAMP DEFAULT NOW(),
    processed_by UUID REFERENCES users(id),
    status VARCHAR(50) CHECK (status IN ('pending', 'processing', 'processed', 'error')),
    version INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_jurisdiction (jurisdiction),
    INDEX idx_processed_at (processed_at)
);

-- Analysis results table
CREATE TABLE analysis_results (
    id UUID PRIMARY KEY,
    document_id UUID NOT NULL REFERENCES documents(id),
    summary TEXT,
    key_changes JSONB,
    affected_departments JSONB,
    impact_analysis JSONB,
    risk_score INT CHECK (risk_score >= 0 AND risk_score <= 100),
    risk_level VARCHAR(50) CHECK (risk_level IN ('low', 'medium', 'high', 'critical')),
    risk_reasons JSONB,
    compliance_actions JSONB,
    estimated_effort VARCHAR(100),
    confidence_score FLOAT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_document_id (document_id),
    INDEX idx_risk_score (risk_score)
);

-- Legal alerts table
CREATE TABLE alerts (
    id UUID PRIMARY KEY,
    document_id UUID NOT NULL REFERENCES documents(id),
    analysis_id UUID REFERENCES analysis_results(id),
    title VARCHAR(500) NOT NULL,
    description TEXT,
    priority VARCHAR(50) CHECK (priority IN ('critical', 'high', 'medium', 'low')),
    risk_level VARCHAR(50),
    status VARCHAR(50) CHECK (status IN ('active', 'acknowledged', 'resolved')),
    assigned_to UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW(),
    resolved_at TIMESTAMP,
    INDEX idx_priority (priority),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
);

-- Compliance tasks table
CREATE TABLE compliance_tasks (
    id UUID PRIMARY KEY,
    analysis_id UUID NOT NULL REFERENCES analysis_results(id),
    action_description TEXT NOT NULL,
    urgency VARCHAR(50) CHECK (urgency IN ('critical', 'high', 'medium', 'low')),
    responsible_department VARCHAR(100),
    assigned_to UUID REFERENCES users(id),
    deadline DATE,
    status VARCHAR(50) CHECK (status IN ('pending', 'in_progress', 'completed', 'blocked')),
    estimated_effort VARCHAR(100),
    actual_effort VARCHAR(100),
    notes TEXT,
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_status (status),
    INDEX idx_deadline (deadline),
    INDEX idx_analysis_id (analysis_id)
);

-- Audit logs table
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    action VARCHAR(100),
    resource_type VARCHAR(100),
    resource_id UUID,
    changes JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    timestamp TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50),
    details JSONB,
    INDEX idx_timestamp (timestamp),
    INDEX idx_user_id (user_id),
    INDEX idx_action (action)
);

-- Document version history
CREATE TABLE document_versions (
    id UUID PRIMARY KEY,
    document_id UUID NOT NULL REFERENCES documents(id),
    content TEXT NOT NULL,
    version INT NOT NULL,
    changes JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    created_by UUID REFERENCES users(id),
    UNIQUE(document_id, version)
);

-- User notifications table
CREATE TABLE notifications (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id),
    document_id UUID REFERENCES documents(id),
    alert_id UUID REFERENCES alerts(id),
    title VARCHAR(500),
    message TEXT,
    notification_type VARCHAR(50),
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_user_id (user_id),
    INDEX idx_is_read (is_read)
);
```

---

## 🔌 API Endpoints Documentation

### Authentication

```javascript
// POST /api/auth/login
{
  "username": "user@example.com",
  "password": "secure_password"
}

Response (200):
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

### Documents

```javascript
// POST /api/documents/process
{
  "url": "https://example.com/legal-document",
  "document_type": "regulation",
  "jurisdiction": "US-CA"
}

Response (202):
{
  "task_id": "uuid",
  "status": "processing",
  "message": "Document processing started"
}

// GET /api/documents
Query Params: ?limit=20&offset=0&jurisdiction=US-CA&status=processed

Response (200):
{
  "total": 150,
  "documents": [
    {
      "id": "uuid",
      "title": "GDPR Enhancement 2024",
      "source": "EU Commission",
      "jurisdiction": "EU",
      "processed_at": "2026-04-08T10:00:00Z",
      "status": "processed"
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 8,
    "has_next": true
  }
}

// GET /api/documents/{document_id}
Response (200):
{
  "id": "uuid",
  "title": "...",
  "content": "...",
  "versions": [...],
  "analysis": {...},
  "alerts": [...],
  "compliance_tasks": [...]
}
```

### Analysis & Insights

```javascript
// GET /api/analysis/{document_id}
Response (200):
{
  "summary": "Clear summary of legal document",
  "key_changes": [
    {
      "type": "Modification",
      "section": "Data Processing",
      "description": "Changed consent requirements..."
    }
  ],
  "impact_analysis": {
    "affected_departments": ["HR", "IT", "Legal"],
    "details": "Detailed impact for each department",
    "business_areas_affected": ["Data & Privacy"]
  },
  "risk_assessment": {
    "level": "High",
    "score": 82,
    "reasons": [
      "Strict compliance deadline",
      "High penalties for non-compliance"
    ]
  },
  "compliance_actions": [
    {
      "id": "uuid",
      "action": "Update privacy policy",
      "priority": "High",
      "responsible_department": "Legal",
      "deadline": "2026-05-08",
      "status": "pending"
    }
  ],
  "jurisdiction": {
    "country": "EU",
    "regulatory_authority": "European Commission",
    "applicability": "All EU member states"
  }
}

// GET /api/dashboard
Response (200):
{
  "compliance_score": 87,
  "high_risk_items": 3,
  "pending_actions": 12,
  "completed_actions": 23,
  "recent_alerts": [...],
  "upcoming_deadlines": [...],
  "risk_distribution": {
    "critical": 1,
    "high": 3,
    "medium": 8,
    "low": 15
  }
}
```

### Alerts

```javascript
// GET /api/alerts?priority=critical&status=active
Response (200):
{
  "total": 3,
  "alerts": [
    {
      "id": "uuid",
      "title": "Critical Compliance Alert",
      "description": "...",
      "priority": "critical",
      "risk_level": "high",
      "document_id": "uuid",
      "created_at": "2026-04-08T10:00:00Z",
      "status": "active",
      "assigned_to": null
    }
  ]
}

// PATCH /api/alerts/{alert_id}
{
  "status": "resolved",
  "notes": "Action taken"
}
```

### Compliance Tracker

```javascript
// GET /api/compliance/tasks?status=pending&sort_by=deadline
Response (200):
{
  "pending": 5,
  "in_progress": 3,
  "completed": 12,
  "blocked": 1,
  "tasks": [
    {
      "id": "uuid",
      "action_description": "Update privacy policy",
      "urgency": "high",
      "deadline": "2026-05-08",
      "status": "pending",
      "responsible_department": "Legal",
      "assigned_to": "analyst_123",
      "estimated_effort": "3 days"
    }
  ]
}

// PATCH /api/compliance/tasks/{task_id}
{
  "status": "in_progress",
  "assigned_to": "user_uuid",
  "notes": "Started implementation"
}
```

### Audit Logs

```javascript
// GET /api/audit-logs?start_date=2026-04-01&end_date=2026-04-08&action=document_processed
Response (200):
{
  "total": 42,
  "logs": [
    {
      "id": "uuid",
      "timestamp": "2026-04-08T10:30:00Z",
      "user": "john.doe@company.com",
      "action": "document_processed",
      "resource_type": "document",
      "resource_id": "uuid",
      "changes": {"status": "processing → processed"},
      "details": {...}
    }
  ]
}
```

---

## 🎨 UI Design Description

### Color Scheme

```typescript
const colors = {
  // Risk levels - Priority indicators
  critical: '#DC2626',    // Red
  high: '#EA580C',        // Orange
  medium: '#F59E0B',      // Amber
  low: '#10B981',         // Green
  
  // Semantic colors
  success: '#10B981',
  warning: '#F59E0B',
  error: '#DC2626',
  info: '#3B82F6',
  
  // Neutral
  dark: '#1F2937',
  light: '#F9FAFB',
  border: '#E5E7EB'
};
```

### Dashboard Home

**Layout:**
- Header with user profile, notifications, settings
- Top metrics row (Compliance Score, Active Alerts, Pending Actions, Risk Items)
- Charts section: Risk Distribution, Recent Activity Timeline
- Recent Legal Updates cards
- Quick actions panel

**Key Features:**
- Real-time compliance score with trend
- Color-coded alert badges
- Interactive risk distribution pie/bar chart
- Quick filter buttons for risk levels
- Recent documents with preview

### Legal Updates Page

**Layout:**
- Search bar with advanced filters
- Filter sidebar: Date range, Jurisdiction, Document Type, Risk Level
- Responsive document list/table view
- Document cards with key info and preview

**Features:**
- Click to view full analysis
- Download PDF capability
- Compare versions
- Share with team
- Bulk actions

### Document Analysis Page

**Layout:**
- Tabbed or collapsible interface
- Tab 1: Summary + Key Metadata
- Tab 2: Key Changes (list/tree view)
- Tab 3: Impact Analysis (affected departments)
- Tab 4: Risk Assessment (score + detailed reasons)
- Tab 5: Compliance Actions (checklist)

**Features:**
- Highlight important text
- Add notes/annotations
- Export analysis as PDF
- Share with stakeholders
- Track changes history

### Alerts Page

**Layout:**
- Alert filters: Priority, Status, Date range
- Alert list with color-coded priority bars
- Alert cards showing: Title, Priority, Risk Level, Document, Action buttons
- Alert detail modal

**Actions:**
- Mark as read/unread
- Acknowledge alert
- Resolve /close
- Reassign to team member
- Add notes

### Compliance Tracker

**Layout:**
- Kanban board: Pending | In Progress | Completed | Blocked
- or List view with filters and sort
- Task cards: Title, Deadline, Department, Status, Progress

**Features:**
- Drag-and-drop status updates
- Deadline badges (red if overdue)
- Task details modal
- Bulk status updates
- Email reminders

---

## 🔒 Security Implementation

### Authentication

```python
# JWT Token with expiration
from fastapi.security import HTTPBearer
from jose import JWTError, jwt

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthCredentials):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username: str = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401)
    return username
```

### Input Validation

```python
from pydantic import BaseModel, validator

class ProcessDocumentRequest(BaseModel):
    url: str
    document_type: str
    jurisdiction: str
    
    @validator('url')
    def validate_url(cls, v):
        if not v.startswith(('http://', 'https://')):
            raise ValueError('Invalid URL')
        return v
```

### Rate Limiting

```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.post("/api/documents/process")
@limiter.limit("10/minute")
async def process_document(request: Request):
    ...
```

---

## 🧪 Testing Structure

### Unit Tests

```python
# tests/test_api.py
import pytest
from fastapi.testclient import TestClient

t client = TestClient(app)

def test_get_dashboard():
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    assert "compliance_score" in response.json()["data"]

def test_process_document_invalid_url():
    response = client.post(
        "/api/documents/process",
        json={"url": "invalid", "jurisdiction": "US"}
    )
    assert response.status_code == 422

# tests/test_services.py
def test_risk_calculation():
    from app.services.risk_engine import calculate_risk_score
    score = calculate_risk_score(
        affected_departments=3,
        deadline_days=7,
        penalty_amount=1000000
    )
    assert score >= 80  # High risk
```

---

## 🚀 Implementation Steps

### Phase 1: Backend (Week 1-2)
1. Set up FastAPI project with PostgreSQL
2. Create database schema and migrations
3. Implement authentication (JWT)
4. Build core API endpoints
5. Create risk calculation engine
6. Add input validation and error handling

### Phase 2: Frontend (Week 2-3)
1. Set up React + TypeScript project
2. Create component structure
3. Build UI pages (Dashboard, Updates, Analysis, etc.)
4. Integrate with backend API
5. Add authentication flow
6. Implement state management

### Phase 3: Testing & Deployment (Week 3-4)
1. Write unit tests
2. Integration tests
3. Performance testing
4. Security audit
5. Deploy to production

---

## 💡 UX Improvement Suggestions

1. **AI Chat Assistant**: Add a chatbot for legal queries
   - "Explain this regulation"
   - "What actions should we take?"
   - "Show similar documents"

2. **Smart Notifications**: Personalized alerts based on user role
   - Email for critical items
   - In-app for medium priority
   - Digest for low priority

3. **Document Comparison**: Side-by-side comparison of document versions

4. **Policy Auto-Generation**: Suggest policy updates based on legal changes

5. **Team Collaboration**: Comments, mentions, task assignments

6. **Export Features**: PDF, Excel, Word reports

7. **Mobile App**: Native iOS/Android for on-the-go access

8. **Calendar View**: Visualize compliance deadlines

9. **Integration**: Connect with Slack, Microsoft Teams, Jira

10. **Advanced Analytics**: Predictive trends, compliance patterns

---

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

**AI Legal Monitoring System v2.0.0 - Redesigned**
*Enterprise-grade legal compliance monitoring with modern architecture*
