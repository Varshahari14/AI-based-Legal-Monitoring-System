// AI Legal Monitoring System - Frontend JavaScript

class LegalMonitorDashboard {
    constructor() {
        this.apiBase = '/api';
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadDashboardData();
        this.startAutoRefresh();
    }

    bindEvents() {
        // Refresh button
        document.getElementById('refreshBtn').addEventListener('click', () => {
            this.loadDashboardData();
        });

        // Process document button
        document.getElementById('processBtn').addEventListener('click', () => {
            this.processDocument();
        });

        // Enter key on URL input
        document.getElementById('documentUrl').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.processDocument();
            }
        });

        // Modal close
        document.querySelector('.close').addEventListener('click', () => {
            document.getElementById('documentModal').style.display = 'none';
        });

        // Close modal when clicking outside
        window.addEventListener('click', (e) => {
            const modal = document.getElementById('documentModal');
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });
    }

    async loadDashboardData() {
        try {
            this.updateStatus('Loading...', 'warning');

            // Load all dashboard data in parallel
            const [dashboardData, documents, alerts, recommendations, auditLogs] = await Promise.all([
                this.fetchAPI('/dashboard'),
                this.fetchAPI('/documents?limit=10'),
                this.fetchAPI('/alerts?limit=5'),
                this.fetchAPI('/recommendations?limit=5'),
                this.fetchAPI('/audit-logs?limit=10')
            ]);

            // Update UI
            this.updateMetrics(dashboardData.data);
            this.updateDocumentsTable(documents.data.documents);
            this.updateAlerts(alerts.data.alerts);
            this.updateRecommendations(recommendations.data.recommendations);
            this.updateAuditLogs(auditLogs.data.logs);

            this.updateStatus('Online', 'online');

        } catch (error) {
            console.error('Error loading dashboard data:', error);
            this.updateStatus('Error loading data', 'offline');
            this.showError('Failed to load dashboard data. Please try again.');
        }
    }

    async fetchAPI(endpoint) {
        const response = await fetch(`${this.apiBase}${endpoint}`);
        if (!response.ok) {
            throw new Error(`API request failed: ${response.status}`);
        }
        return await response.json();
    }

    updateStatus(text, status) {
        const statusText = document.getElementById('statusText');
        const statusDot = document.getElementById('statusDot');

        statusText.textContent = text;
        statusDot.className = 'status-dot';

        if (status === 'online') {
            statusDot.classList.add('online');
        } else if (status === 'offline') {
            statusDot.classList.add('offline');
        }
    }

    updateMetrics(data) {
        document.getElementById('documentsProcessed').textContent = data.documents_processed || 0;
        document.getElementById('activeAlerts').textContent = data.active_alerts || 0;
        document.getElementById('pendingActions').textContent = data.pending_actions || 0;
        document.getElementById('complianceScore').textContent = `${data.compliance_score || 0}%`;
    }

    updateDocumentsTable(documents) {
        const tbody = document.getElementById('documentsTableBody');

        if (!documents || documents.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" class="loading">No documents processed yet.</td></tr>';
            return;
        }

        tbody.innerHTML = documents.map(doc => `
            <tr>
                <td>${this.escapeHtml(doc.title || 'Untitled')}</td>
                <td>${this.escapeHtml(doc.source || 'Unknown')}</td>
                <td><span class="status-badge ${doc.status || 'pending'}">${doc.status || 'pending'}</span></td>
                <td><span class="risk-badge ${this.getRiskClass(doc.impact_level || 'low')}">${doc.impact_level || 'low'}</span></td>
                <td>${this.formatDate(doc.processed_at || doc.extracted_at)}</td>
                <td>
                    <button class="btn btn-primary" onclick="dashboard.viewDocument('${doc.id || doc.url}')">
                        <i class="fas fa-eye"></i> View
                    </button>
                </td>
            </tr>
        `).join('');
    }

    updateAlerts(alerts) {
        const container = document.getElementById('alertsContainer');

        if (!alerts || alerts.length === 0) {
            container.innerHTML = '<div class="loading">No active alerts.</div>';
            return;
        }

        container.innerHTML = alerts.map(alert => `
            <div class="alert-card ${this.getRiskClass(alert.risk_level || 'medium')}">
                <div class="alert-title">${this.escapeHtml(alert.title || 'Alert')}</div>
                <div class="alert-meta">
                    Risk Level: ${alert.risk_level || 'Medium'} |
                    Date: ${this.formatDate(alert.sent_at || alert.date)}
                </div>
                <div class="alert-actions">
                    <button class="btn btn-primary" onclick="dashboard.viewAlert('${alert.id || 'alert_' + Math.random()}')">
                        <i class="fas fa-eye"></i> View Details
                    </button>
                    <button class="btn btn-success" onclick="dashboard.dismissAlert('${alert.id || 'alert_' + Math.random()}')">
                        <i class="fas fa-check"></i> Dismiss
                    </button>
                </div>
            </div>
        `).join('');
    }

    updateRecommendations(recommendations) {
        const container = document.getElementById('recommendationsContainer');

        if (!recommendations || recommendations.length === 0) {
            container.innerHTML = '<div class="loading">No pending recommendations.</div>';
            return;
        }

        container.innerHTML = recommendations.map(rec => `
            <div class="recommendation-card">
                <div class="recommendation-header">
                    <div>
                        <div class="recommendation-title">${this.escapeHtml(rec.action || 'Recommendation')}</div>
                        <div class="recommendation-meta">
                            <span>Category: ${rec.category || 'General'}</span>
                            <span>Urgency: ${rec.urgency || 'Medium'}</span>
                            <span class="recommendation-deadline">Deadline: ${this.formatDate(rec.deadline)}</span>
                        </div>
                    </div>
                    <span class="status-badge ${rec.status || 'pending'}">${rec.status || 'pending'}</span>
                </div>
                <div class="alert-actions">
                    <button class="btn btn-success" onclick="dashboard.completeRecommendation('${rec.id || 'rec_' + Math.random()}')">
                        <i class="fas fa-check"></i> Mark Complete
                    </button>
                    <button class="btn btn-primary" onclick="dashboard.viewRecommendation('${rec.id || 'rec_' + Math.random()}')">
                        <i class="fas fa-eye"></i> View Details
                    </button>
                </div>
            </div>
        `).join('');
    }

    updateAuditLogs(logs) {
        const container = document.getElementById('auditLogsContainer');

        if (!logs || logs.length === 0) {
            container.innerHTML = '<div class="loading">No audit logs available.</div>';
            return;
        }

        container.innerHTML = logs.map(log => `
            <div class="audit-entry">
                <div class="audit-timestamp">${this.formatDateTime(log.timestamp)}</div>
                <div class="audit-event">${this.escapeHtml(log.event_type || 'Event')}</div>
                <div class="audit-details">${this.formatAuditDetails(log)}</div>
            </div>
        `).join('');
    }

    async processDocument() {
        const url = document.getElementById('documentUrl').value.trim();
        const resultDiv = document.getElementById('processingResult');

        if (!url) {
            this.showError('Please enter a document URL');
            return;
        }

        try {
            resultDiv.style.display = 'block';
            resultDiv.className = 'processing-result';
            resultDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing document...';

            // Simulate processing (in real implementation, this would call the backend)
            const response = await this.simulateDocumentProcessing(url);

            resultDiv.className = 'processing-result success';
            resultDiv.innerHTML = `
                <h4><i class="fas fa-check-circle"></i> Document Processed Successfully</h4>
                <p><strong>Title:</strong> ${response.document.title}</p>
                <p><strong>Risk Level:</strong> ${response.risk_assessment.overall_risk_level}</p>
                <p><strong>Affected Categories:</strong> ${response.impact_analysis.affected_categories.join(', ')}</p>
                <p><strong>Recommendations Generated:</strong> ${response.recommendations.length}</p>
            `;

            // Refresh dashboard data
            setTimeout(() => this.loadDashboardData(), 1000);

        } catch (error) {
            resultDiv.className = 'processing-result error';
            resultDiv.innerHTML = `<i class="fas fa-exclamation-triangle"></i> Error processing document: ${error.message}`;
        }
    }

    async simulateDocumentProcessing(url) {
        // Simulate document processing with sample data
        await new Promise(resolve => setTimeout(resolve, 2000)); // Simulate processing time

        return {
            document: {
                title: "Sample Legal Document",
                summary: "This is a sample legal document for demonstration purposes.",
                url: url,
                extracted_at: new Date().toISOString()
            },
            impact_analysis: {
                affected_categories: ["Data & Privacy", "Consumer Protection"],
                overall_impact_level: "Medium"
            },
            recommendations: [
                {
                    action: "Review privacy policy",
                    urgency: "High",
                    deadline: "2026-04-15T00:00:00"
                },
                {
                    action: "Update consent forms",
                    urgency: "Medium",
                    deadline: "2026-04-30T00:00:00"
                }
            ],
            risk_assessment: {
                overall_risk_level: "Medium",
                critical_risks: 0,
                high_risks: 1,
                medium_risks: 2
            }
        };
    }

    viewDocument(docId) {
        // In a real implementation, this would fetch document details from API
        const modal = document.getElementById('documentModal');
        const modalTitle = document.getElementById('modalTitle');
        const modalBody = document.getElementById('modalBody');

        modalTitle.textContent = 'Document Details';
        modalBody.innerHTML = `
            <div class="document-details">
                <h4>Document Information</h4>
                <p><strong>ID:</strong> ${docId}</p>
                <p><strong>Status:</strong> Processed</p>
                <p><strong>Last Updated:</strong> ${new Date().toLocaleString()}</p>

                <h4>Analysis Results</h4>
                <p><strong>Risk Level:</strong> Medium</p>
                <p><strong>Affected Areas:</strong> Data & Privacy, Consumer Protection</p>

                <h4>Recommendations</h4>
                <ul>
                    <li>Review privacy policy (High priority)</li>
                    <li>Update consent forms (Medium priority)</li>
                </ul>
            </div>
        `;

        modal.style.display = 'block';
    }

    viewAlert(alertId) {
        // Similar to viewDocument but for alerts
        const modal = document.getElementById('documentModal');
        const modalTitle = document.getElementById('modalTitle');
        const modalBody = document.getElementById('modalBody');

        modalTitle.textContent = 'Alert Details';
        modalBody.innerHTML = `
            <div class="alert-details">
                <h4>Alert Information</h4>
                <p><strong>ID:</strong> ${alertId}</p>
                <p><strong>Risk Level:</strong> High</p>
                <p><strong>Triggered:</strong> ${new Date().toLocaleString()}</p>

                <h4>Description</h4>
                <p>New legal requirements detected that may impact data processing operations.</p>

                <h4>Recommended Actions</h4>
                <ul>
                    <li>Review compliance requirements</li>
                    <li>Update internal policies</li>
                    <li>Notify relevant stakeholders</li>
                </ul>
            </div>
        `;

        modal.style.display = 'block';
    }

    dismissAlert(alertId) {
        // In real implementation, this would call API to dismiss alert
        alert(`Alert ${alertId} dismissed`);
        this.loadDashboardData();
    }

    completeRecommendation(recId) {
        // In real implementation, this would call API to mark recommendation complete
        alert(`Recommendation ${recId} marked as complete`);
        this.loadDashboardData();
    }

    viewRecommendation(recId) {
        // Similar to viewDocument but for recommendations
        const modal = document.getElementById('documentModal');
        const modalTitle = document.getElementById('modalTitle');
        const modalBody = document.getElementById('modalBody');

        modalTitle.textContent = 'Recommendation Details';
        modalBody.innerHTML = `
            <div class="recommendation-details">
                <h4>Recommendation Details</h4>
                <p><strong>ID:</strong> ${recId}</p>
                <p><strong>Status:</strong> Pending</p>
                <p><strong>Urgency:</strong> High</p>
                <p><strong>Deadline:</strong> 2026-04-15</p>

                <h4>Description</h4>
                <p>Review and update the current privacy policy to ensure compliance with new legal requirements.</p>

                <h4>Responsible Party</h4>
                <p>Legal Department / Privacy Officer</p>

                <h4>Estimated Effort</h4>
                <p>2-3 days</p>
            </div>
        `;

        modal.style.display = 'block';
    }

    startAutoRefresh() {
        // Auto-refresh every 30 seconds
        setInterval(() => {
            this.loadDashboardData();
        }, 30000);
    }

    // Utility functions
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    formatDate(dateString) {
        if (!dateString) return 'N/A';
        try {
            return new Date(dateString).toLocaleDateString();
        } catch {
            return dateString;
        }
    }

    formatDateTime(dateString) {
        if (!dateString) return 'N/A';
        try {
            return new Date(dateString).toLocaleString();
        } catch {
            return dateString;
        }
    }

    getRiskClass(riskLevel) {
        const classes = {
            'low': 'low',
            'medium': 'medium',
            'high': 'high',
            'critical': 'critical'
        };
        return classes[riskLevel.toLowerCase()] || 'medium';
    }

    formatAuditDetails(log) {
        // Format audit log details based on event type
        const details = [];
        if (log.document_id) details.push(`Document: ${log.document_id}`);
        if (log.status) details.push(`Status: ${log.status}`);
        if (log.user_id) details.push(`User: ${log.user_id}`);
        return details.join(' | ') || 'No additional details';
    }

    showError(message) {
        // Simple error display - in production, use a proper notification system
        alert(`Error: ${message}`);
    }
}

// Initialize dashboard when page loads
let dashboard;
document.addEventListener('DOMContentLoaded', () => {
    dashboard = new LegalMonitorDashboard();
});