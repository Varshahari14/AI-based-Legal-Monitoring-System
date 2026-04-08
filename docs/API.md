"""
API Documentation for AI Legal Monitoring System
"""

# API Endpoints Reference

## 1. Health Check
**Endpoint:** `GET /api/health`

**Description:** Check if the API is running

**Response:**
```json
{
    "status": "healthy",
    "timestamp": "2024-01-15T10:30:00.123456",
    "version": "1.0.0"
}
```

## 2. Dashboard Overview
**Endpoint:** `GET /api/dashboard`

**Description:** Get overall dashboard metrics

**Response:**
```json
{
    "status": "success",
    "data": {
        "documents_processed": 45,
        "active_alerts": 3,
        "pending_actions": 7,
        "compliance_score": 78.5,
        "risk_level": "Medium",
        "last_update": "2024-01-15T10:30:00.123456"
    }
}
```

## 3. Get Alerts
**Endpoint:** `GET /api/alerts?type=all&limit=10`

**Parameters:**
- `type` (optional): Filter by alert type (email, sms, all)
- `limit` (optional): Number of alerts to return (default: 10)

**Response:**
```json
{
    "status": "success",
    "data": {
        "alerts": [
            {
                "id": "alert_001",
                "title": "GDPR Update",
                "risk_level": "High",
                "recipients": ["legal@company.com"],
                "sent_at": "2024-01-15T09:00:00",
                "status": "sent"
            }
        ],
        "total": 1,
        "type_filter": "all"
    }
}
```

## 4. Get Documents
**Endpoint:** `GET /api/documents?page=1&limit=20`

**Parameters:**
- `page` (optional): Page number (default: 1)
- `limit` (optional): Items per page (default: 20)

**Response:**
```json
{
    "status": "success",
    "data": {
        "documents": [
            {
                "id": "doc_001",
                "title": "Document Title",
                "source": "government",
                "status": "processed",
                "extracted_at": "2024-01-15T09:00:00",
                "impact_level": "High"
            }
        ],
        "total": 45,
        "page": 1,
        "limit": 20
    }
}
```

## 5. Get Compliance Status
**Endpoint:** `GET /api/compliance`

**Description:** Get overall compliance metrics

**Response:**
```json
{
    "status": "success",
    "data": {
        "overall_score": 78.5,
        "risk_level": "Medium",
        "pending_actions": 7,
        "completed_actions": 23,
        "by_category": {
            "Data & Privacy": {
                "score": 85,
                "pending": 1,
                "completed": 5
            },
            "Employment": {
                "score": 70,
                "pending": 2,
                "completed": 3
            }
        }
    }
}
```

## 6. Get Recommendations
**Endpoint:** `GET /api/recommendations?status=pending`

**Parameters:**
- `status` (optional): Filter by status (pending, in_progress, completed, all)

**Response:**
```json
{
    "status": "success",
    "data": {
        "recommendations": [
            {
                "id": "rec_001",
                "action": "Update privacy policy",
                "category": "Data & Privacy",
                "urgency": "High",
                "deadline": "2024-01-22",
                "responsible": "Legal",
                "status": "pending"
            }
        ],
        "total": 7,
        "status_filter": "pending"
    }
}
```

## 7. Get Audit Logs
**Endpoint:** `GET /api/audit-logs?event_type=all&limit=50`

**Parameters:**
- `event_type` (optional): Filter by event type
- `limit` (optional): Number of logs to return (default: 50)

**Response:**
```json
{
    "status": "success",
    "data": {
        "logs": [
            {
                "event_type": "DOCUMENT_PROCESSED",
                "timestamp": "2024-01-15T10:30:00",
                "document_id": "doc_001",
                "status": "success"
            }
        ],
        "total": 150,
        "event_type_filter": "all"
    }
}
```

## 8. Get Document Details
**Endpoint:** `GET /api/document/<doc_id>`

**Description:** Get detailed information about a specific document

**Response:**
```json
{
    "status": "success",
    "data": {
        "document_id": "doc_001",
        "title": "Document Title",
        "summary": "This document covers...",
        "key_entities": {
            "PERSON": ["John Doe", "Jane Smith"],
            "ORG": ["Company A", "Regulator B"],
            "LAW": ["GDPR", "Data Protection Act"]
        },
        "sections": {
            "Introduction": "...",
            "Key Provisions": "...",
            "Penalties": "..."
        },
        "impact_analysis": {
            "affected_categories": ["Data & Privacy"],
            "overall_impact_level": "High"
        },
        "recommendations": [
            {
                "action": "Update privacy policy",
                "urgency": "High",
                "deadline": "2024-01-22"
            }
        ]
    }
}
```

## Error Responses

### 400 Bad Request
```json
{
    "status": "error",
    "message": "Invalid request parameters",
    "code": "BAD_REQUEST"
}
```

### 404 Not Found
```json
{
    "status": "error",
    "message": "Resource not found",
    "code": "NOT_FOUND"
}
```

### 500 Internal Server Error
```json
{
    "status": "error",
    "message": "Internal server error",
    "code": "INTERNAL_ERROR"
}
```

## Authentication

(To be implemented) Future versions will support:
- API Key authentication
- JWT tokens
- OAuth 2.0

## Rate Limiting

(To be implemented) Future versions will include:
- Request rate limits
- Quota management
- Priority queues

## WebSocket Support

(To be implemented) For real-time updates:
- `/ws/alerts` - Real-time alert stream
- `/ws/compliance` - Real-time compliance updates
- `/ws/documents` - Real-time document processing updates
