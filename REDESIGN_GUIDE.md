# AI Legal Monitoring System - v2.0 Redesign Guide

## 📋 Overview

This guide provides detailed implementation instructions for the redesigned AI Legal Monitoring System featuring a modern React frontend and FastAPI backend.

---

## 🎨 Frontend Architecture (React + TypeScript)

### Setup Instructions

```bash
# Create new React project with Vite
npm create vite@latest frontend -- --template react-ts
cd frontend

# Install dependencies
npm install

# Core packages
npm install -D typescript tailwindcss postcss autoprefixer
npm install react-router-dom axios zustand
npm install recharts @mui/icons-material
npm install react-hot-toast date-fns

# Initialize Tailwind
npx tailwindcss init -p
```

### Component Example: Dashboard Home

```typescript
// frontend/src/pages/DashboardPage.tsx
import React, { useEffect, useState } from 'react';
import { MetricCard, RiskDistributionChart, RecentUpdates } from '../components/Dashboard';
import { useDashboard } from '../hooks/useDashboard';

export const DashboardPage: React.FC = () => {
  const { data, loading, error } = useDashboard();

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorBoundary error={error} />;

  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <MetricCard
        title="Compliance Score"
        value={data.compliance_score}
        unit="%"
        trend="+2.5%"
        icon="shield"
        color="blue"
      />
      <MetricCard
        title="Active Alerts"
        value={data.active_alerts}
        trend={data.alert_trend}
        icon="bell"
        color="red"
      />
      <MetricCard
        title="Pending Actions"
        value={data.pending_actions}
        icon="checkbox"
        color="amber"
      />
      <MetricCard
        title="Risk Items"
        value={data.high_risk_count}
        icon="alert"
        color="orange"
      />

      <div className="md:col-span-2">
        <RiskDistributionChart data={data.risk_distribution} />
      </div>
      <div className="md:col-span-2">
        <RecentUpdates documents={data.recent_documents} />
      </div>
    </div>
  );
};
```

### Custom Hooks

```typescript
// frontend/src/hooks/useDashboard.ts
import { useEffect, useState } from 'react';
import { api } from '../services/api';

export const useDashboard = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get('/dashboard');
        setData(response.data.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return { data, loading, error };
};
```

### TypeScript Types

```typescript
// frontend/src/types/document.ts
export interface Document {
  id: string;
  title: string;
  content: string;
  url: string;
  source: string;
  jurisdiction: string;
  processed_at: string;
  status: 'pending' | 'processing' | 'processed' | 'error';
}

export interface Analysis {
  id: string;
  document_id: string;
  summary: string;
  key_changes: KeyChange[];
  impact_analysis: ImpactAnalysis;
  risk_assessment: RiskAssessment;
  compliance_actions: ComplianceAction[];
}

export interface RiskAssessment {
  level: 'low' | 'medium' | 'high' | 'critical';
  score: number;
  reasons: string[];
}

export interface ComplianceAction {
  id: string;
  action: string;
  priority: 'critical' | 'high' | 'medium' | 'low';
  deadline: string;
  responsible_department: string;
  status: 'pending' | 'in_progress' | 'completed' | 'blocked';
}
```

### API Service

```typescript
// frontend/src/services/api.ts
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add JWT token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle errors globally
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

---

## ⚙️ Backend Architecture (FastAPI + PostgreSQL)

### Setup Instructions

```bash
# Create backend project
mkdir backend
cd backend
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-jose passlib
pip install python-dotenv pytest pytest-asyncio httpx
pip install alembic celery redis # for async tasks

# Create project structure
mkdir app app/api app/api/routes app/db app/services app/processors app/core
```

### FastAPI Main Application

```python
# backend/app/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from app.api.routes import documents, analysis, alerts, compliance, audit, auth
from app.db.database import engine, Base
from app.core.logging import setup_logging

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="AI Legal Monitoring System",
    description="Enterprise legal compliance and monitoring platform",
    version="2.0.0"
)

# Setup logging
setup_logging()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["Analysis"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(compliance.router, prefix="/api/compliance", tags=["Compliance"])
app.include_router(audit.router, prefix="/api/audit-logs", tags=["Audit"])

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "2.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Database Models

```python
# backend/app/db/models.py
from sqlalchemy import Column, String, Text, Integer, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    full_name = Column(String(255))
    department = Column(String(100))
    role = Column(String(50), default="analyst")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    documents = relationship("Document", back_populates="processed_by")
    audit_logs = relationship("AuditLog", back_populates="user")

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500))
    content = Column(Text)
    url = Column(String(2048))
    source = Column(String(255))
    jurisdiction = Column(String(100), index=True)
    processed_at = Column(DateTime, default=datetime.utcnow, index=True)
    processed_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(String(50), default="pending")
    version = Column(Integer, default=1)
    
    processed_by = relationship("User", back_populates="documents")
    analysis = relationship("AnalysisResult", uselist=False, back_populates="document")
    alerts = relationship("Alert", back_populates="document")

class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), unique=True)
    summary = Column(Text)
    key_changes = Column(JSON)
    affected_departments = Column(JSON)
    impact_analysis = Column(JSON)
    risk_score = Column(Integer)
    risk_level = Column(String(50))
    risk_reasons = Column(JSON)
    compliance_actions = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    document = relationship("Document", back_populates="analysis")
    compliance_tasks = relationship("ComplianceTask", back_populates="analysis")
    alerts = relationship("Alert", back_populates="analysis")

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"))
    analysis_id = Column(UUID(as_uuid=True), ForeignKey("analysis_results.id"))
    title = Column(String(500))
    description = Column(Text)
    priority = Column(String(50))
    status = Column(String(50), default="active", index=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    resolved_at = Column(DateTime)
    
    document = relationship("Document", back_populates="alerts")
    analysis = relationship("AnalysisResult", back_populates="alerts")

class ComplianceTask(Base):
    __tablename__ = "compliance_tasks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_id = Column(UUID(as_uuid=True), ForeignKey("analysis_results.id"))
    action_description = Column(Text)
    urgency = Column(String(50))
    responsible_department = Column(String(100))
    deadline = Column(DateTime)
    status = Column(String(50), default="pending", index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    analysis = relationship("AnalysisResult", back_populates="compliance_tasks")

class AuditLog(Base):
    __tablename__ = "audit_logs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    action = Column(String(100))
    resource_type = Column(String(100))
    resource_id = Column(UUID(as_uuid=True))
    changes = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    user = relationship("User", back_populates="audit_logs")
```

### API Route Example: Documents

```python
# backend/app/api/routes/documents.py
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.models.document import ProcessDocumentRequest
from app.services.document_service import DocumentService

router = APIRouter()

@router.get("")
async def list_documents(
    limit: int = 20,
    offset: int = 0,
    jurisdiction: str = None,
    status: str = None,
    db: Session = Depends(get_db)
):
    """List all processed documents with filtering"""
    query = db.query(Document)
    
    if jurisdiction:
        query = query.filter(Document.jurisdiction == jurisdiction)
    if status:
        query = query.filter(Document.status == status)
    
    total = query.count()
    documents = query.offset(offset).limit(limit).all()
    
    return {
        "success": True,
        "data": {
            "documents": [doc.to_dict() for doc in documents],
            "total": total,
            "pagination": {
                "current_page": offset // limit + 1,
                "total_pages": (total + limit - 1) // limit,
                "has_next": offset + limit < total
            }
        }
    }

@router.post("/process")
async def process_document(
    request: ProcessDocumentRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Submit a document for processing"""
    # Create document record
    document = Document(
        title=request.title,
        url=request.url,
        jurisdiction=request.jurisdiction,
        status="processing"
    )
    db.add(document)
    db.commit()
    
    # Start async processing
    background_tasks.add_task(
        DocumentService.process_document,
        document.id,
        db
    )
    
    return {
        "success": True,
        "data": {
            "document_id": str(document.id),
            "status": "processing"
        }
    }

@router.get("/{document_id}")
async def get_document(document_id: str, db: Session = Depends(get_db)):
    """Get detailed document information with analysis"""
    document = db.query(Document).filter(Document.id == document_id).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return {
        "success": True,
        "data": {
            "document": document.to_dict(),
            "analysis": document.analysis.to_dict() if document.analysis else None,
            "alerts": [alert.to_dict() for alert in document.alerts],
            "compliance_tasks": [task.to_dict() for task in document.analysis.compliance_tasks if document.analysis]
        }
    }
```

### Risk Assessment Service

```python
# backend/app/services/risk_engine.py
from typing import List, Dict

class RiskEngine:
    """Calculate risk scores and levels for legal documents"""
    
    SEVERITY_PENALTIES = {
        "high_penalty_increase": 25,
        "new_restrictions": 20,
        "strict_deadline": 15,
        "multiple_departments": 10,
        "compliance_requirement": 8
    }
    
    @staticmethod
    def calculate_risk_score(assessment_data: Dict) -> Dict:
        """
        Calculate risk score based on multiple factors
        
        Args:
            assessment_data: Dict with risk factors
            
        Returns:
            Dict with score, level, and reasons
        """
        score = 0
        reasons = []
        
        # Factor 1: Deadline urgency
        if assessment_data.get("deadline_days", 0) < 30:
            score += 25
            reasons.append("Short compliance deadline (less than 30 days)")
        elif assessment_data.get("deadline_days", 0) < 90:
            score += 15
            reasons.append("Medium compliance timeline")
        
        # Factor 2: Department impact
        affected_count = len(assessment_data.get("affected_departments", []))
        if affected_count >= 5:
            score += 20
            reasons.append(f"Multiple departments affected ({affected_count})")
        elif affected_count >= 3:
            score += 10
            reasons.append(f"Several departments affected ({affected_count})")
        
        # Factor 3: Penalties
        penalty_amount = assessment_data.get("penalty_amount", 0)
        if penalty_amount > 10000000:
            score += 25
            reasons.append(f"Very high penalties ($${penalty_amount:,})")
        elif penalty_amount > 1000000:
            score += 15
            reasons.append(f"High penalties ($${penalty_amount:,})")
        
        # Factor 4: Restrictions/Changes
        change_count = len(assessment_data.get("key_changes", []))
        if change_count > 10:
            score += 20
            reasons.append(f"Multiple significant changes ({change_count})")
        
        # Ensure score is within 0-100
        score = min(score, 100)
        
        # Determine risk level
        if score >= 75:
            level = "critical"
        elif score >= 50:
            level = "high"
        elif score >= 25:
            level = "medium"
        else:
            level = "low"
        
        return {
            "score": score,
            "level": level,
            "reasons": reasons
        }
```

### Pydantic Models

```python
# backend/app/api/models/document.py
from pydantic import BaseModel, HttpUrl, validator
from typing import Optional, List
from datetime import datetime

class ProcessDocumentRequest(BaseModel):
    url: str
    title: Optional[str] = None
    jurisdiction: str
    document_type: Optional[str] = None
    
    @validator('url')
    def validate_url(cls, v):
        if not v.startswith(('http://', 'https://')):
            raise ValueError('URL must start with http:// or https://')
        return v
    
    @validator('jurisdiction')
    def validate_jurisdiction(cls, v):
        valid = ['US-CA', 'US-NY', 'EU', 'UK', 'APAC']
        if v not in valid:
            raise ValueError(f'Invalid jurisdiction. Must be one of {valid}')
        return v

class DocumentResponse(BaseModel):
    id: str
    title: str
    source: str
    jurisdiction: str
    processed_at: datetime
    status: str
    
    class Config:
        from_attributes = True

class AnalysisResponse(BaseModel):
    summary: str
    key_changes: List[Dict]
    impact_analysis: Dict
    risk_assessment: Dict
    compliance_actions: List[Dict]
    jurisdiction: Dict
    
    class Config:
        from_attributes = True
```

---

## 🧪 Testing Example

```python
# backend/tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def sample_document():
    return {
        "url": "https://example.com/regulation.pdf",
        "title": "GDPR Amendment 2024",
        "jurisdiction": "EU",
        "document_type": "regulation"
    }

def test_process_document(sample_document):
    response = client.post("/api/documents/process", json=sample_document)
    assert response.status_code == 202
    assert response.json()["data"]["status"] == "processing"

def test_list_documents():
    response = client.get("/api/documents")
    assert response.status_code == 200
    assert "documents" in response.json()["data"]

def test_invalid_url():
    response = client.post(
        "/api/documents/process",
        json={
            "url": "invalid-url",
            "jurisdiction": "EU"
        }
    )
    assert response.status_code == 422

def test_risk_calculation():
    from app.services.risk_engine import RiskEngine
    
    assessment = {
        "deadline_days": 15,
        "affected_departments": ["HR", "IT", "Legal", "Finance"],
        "penalty_amount": 5000000,
        "key_changes": ["change1", "change2"]
    }
    
    result = RiskEngine.calculate_risk_score(assessment)
    assert result["level"] in ["critical", "high", "medium", "low"]
    assert result["score"] >= 0 and result["score"] <= 100
    assert len(result["reasons"]) > 0
```

---

## 📦 Deployment Configuration

### Docker Files

```dockerfile
# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```dockerfile
# frontend/Dockerfile
FROM node:18-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secure_password
      POSTGRES_DB: legal_monitor
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  backend:
    build: ./backend
    depends_on:
      - postgres
      - redis
    environment:
      DATABASE_URL: postgresql://admin:secure_password@postgres:5432/legal_monitor
      REDIS_URL: redis://redis:6379
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    ports:
      - "3000:80"

volumes:
  postgres_data:
```

---

## ✅ Checklist for Implementation

### Backend
- [ ] Set up FastAPI project structure
- [ ] Configure PostgreSQL database
- [ ] Implement authentication (JWT)
- [ ] Create database models and migrations
- [ ] Build API endpoints
- [ ] Implement risk calculation engine
- [ ] Add input validation (Pydantic)
- [ ] Set up logging and error handling
- [ ] Write unit tests
- [ ] Implement caching (Redis)
- [ ] Set up async task queue (Celery)
- [ ] Deploy to production

### Frontend
- [ ] Create React + TypeScript project
- [ ] Set up Tailwind CSS
- [ ] Build component structure
- [ ] Create pages (Dashboard, Documents, Analysis, etc.)
- [ ] Implement authentication flow
- [ ] Connect to backend API
- [ ] Add state management
- [ ] Implement responsive design
- [ ] Add error handling
- [ ] Write component tests
- [ ] Optimize performance
- [ ] Deploy to production

### Database
- [ ] Design schema
- [ ] Create tables
- [ ] Set up indexes
- [ ] Configure backups
- [ ] Test disaster recovery

### Testing
- [ ] Write unit tests
- [ ] Write integration tests
- [ ] Perform security audit
- [ ] Load testing
- [ ] UAT (User Acceptance Testing)

---

## 🎯 Success Metrics

- **Performance**: API response time < 200ms
- **Uptime**: 99.9% availability
- **Scalability**: Support 10,000+ concurrent users
- **Security**: Zero critical vulnerabilities
- **User satisfaction**: NPS > 80
- **Data accuracy**: Risk prediction accuracy > 90%

