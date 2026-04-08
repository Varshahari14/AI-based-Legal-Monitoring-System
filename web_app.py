#!/usr/bin/env python3
"""
AI Legal Monitoring System - Web Application
Flask web server for the dashboard interface
"""

import os
import sys
from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'legal-monitoring-secret-key-2024'

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Try to import the legal monitoring system, handle gracefully if dependencies are missing
try:
    from main import LegalMonitoringSystem
    legal_system = LegalMonitoringSystem()
    BACKEND_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Backend modules not available: {e}")
    print("Running in demo mode with mock data...")
    legal_system = None
    BACKEND_AVAILABLE = False

@app.route('/')
def index():
    """Serve the main dashboard page"""
    return render_template('index.html')

@app.route('/api/dashboard')
def get_dashboard_data():
    """Get dashboard overview data"""
    try:
        if BACKEND_AVAILABLE and legal_system:
            # Get system status from actual backend
            status = legal_system.get_system_status()
            dashboard_data = {
                'documents_processed': status.get('documents_processed', 0),
                'active_alerts': status.get('active_alerts', 0),
                'pending_actions': status.get('pending_actions', 0),
                'compliance_score': status.get('compliance_score', 85),
                'last_updated': datetime.now().isoformat()
            }
        else:
            # Mock data for demonstration when backend is not available
            dashboard_data = {
                'documents_processed': 42,
                'active_alerts': 3,
                'pending_actions': 7,
                'compliance_score': 87,
                'last_updated': datetime.now().isoformat()
            }

        return jsonify({
            'success': True,
            'data': dashboard_data
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/documents')
def get_documents():
    """Get processed documents"""
    try:
        limit = int(request.args.get('limit', 10))

        # Mock documents data for demonstration
        documents = [
            {
                'id': f'doc_{i}',
                'title': f'Legal Document {i}',
                'source': 'Sample Source',
                'status': 'processed',
                'impact_level': 'medium' if i % 3 == 0 else 'low',
                'processed_at': (datetime.now() - timedelta(days=i)).isoformat(),
                'summary': f'Summary of document {i}...'
            }
            for i in range(1, limit + 1)
        ]

        return jsonify({
            'success': True,
            'data': {
                'documents': documents,
                'total': len(documents)
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/alerts')
def get_alerts():
    """Get active alerts"""
    try:
        limit = int(request.args.get('limit', 5))

        # Mock alerts data
        alerts = [
            {
                'id': f'alert_{i}',
                'title': f'Legal Alert {i}',
                'description': f'Description of alert {i}',
                'risk_level': 'high' if i % 4 == 0 else 'medium',
                'sent_at': (datetime.now() - timedelta(hours=i*2)).isoformat(),
                'status': 'active'
            }
            for i in range(1, limit + 1)
        ]

        return jsonify({
            'success': True,
            'data': {
                'alerts': alerts,
                'total': len(alerts)
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/recommendations')
def get_recommendations():
    """Get pending recommendations"""
    try:
        limit = int(request.args.get('limit', 5))

        # Mock recommendations data
        recommendations = [
            {
                'id': f'rec_{i}',
                'action': f'Recommendation Action {i}',
                'description': f'Detailed description of recommendation {i}',
                'category': 'Compliance' if i % 2 == 0 else 'Risk Management',
                'urgency': 'high' if i % 3 == 0 else 'medium',
                'deadline': (datetime.now() + timedelta(days=7+i)).isoformat(),
                'status': 'pending'
            }
            for i in range(1, limit + 1)
        ]

        return jsonify({
            'success': True,
            'data': {
                'recommendations': recommendations,
                'total': len(recommendations)
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/audit-logs')
def get_audit_logs():
    """Get audit logs"""
    try:
        limit = int(request.args.get('limit', 10))

        # Mock audit logs data
        logs = [
            {
                'id': f'log_{i}',
                'timestamp': (datetime.now() - timedelta(minutes=i*15)).isoformat(),
                'event_type': 'Document Processed' if i % 2 == 0 else 'Alert Generated',
                'user_id': 'system',
                'document_id': f'doc_{i}' if i % 2 == 0 else None,
                'details': f'Additional details for log entry {i}'
            }
            for i in range(1, limit + 1)
        ]

        return jsonify({
            'success': True,
            'data': {
                'logs': logs,
                'total': len(logs)
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/process-document', methods=['POST'])
def process_document():
    """Process a new document"""
    try:
        data = request.get_json()
        url = data.get('url')

        if not url:
            return jsonify({
                'success': False,
                'error': 'Document URL is required'
            }), 400

        # In a real implementation, this would process the actual document
        # For now, return mock processing results
        result = {
            'document': {
                'id': f'doc_{datetime.now().strftime("%Y%m%d%H%M%S")}',
                'title': 'Processed Legal Document',
                'url': url,
                'processed_at': datetime.now().isoformat()
            },
            'impact_analysis': {
                'affected_categories': ['Data & Privacy', 'Consumer Protection'],
                'overall_impact_level': 'Medium'
            },
            'recommendations': [
                {
                    'action': 'Review privacy policy',
                    'urgency': 'High',
                    'deadline': (datetime.now() + timedelta(days=30)).isoformat()
                }
            ],
            'risk_assessment': {
                'overall_risk_level': 'Medium',
                'critical_risks': 0,
                'high_risks': 1,
                'medium_risks': 2
            }
        }

        return jsonify({
            'success': True,
            'data': result
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("Starting AI Legal Monitoring System Web Server...")
    print("Dashboard will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")

    # Run the Flask application
    app.run(
        host='localhost',
        port=5000,
        debug=True,
        use_reloader=False  # Disable reloader to avoid issues with our imports
    )