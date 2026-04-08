"""
Basic Demo of AI Legal Monitoring System (No ML Dependencies)
"""
import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def demo_basic_functionality():
    """Demonstrate basic functionality without heavy ML dependencies"""
    print("=" * 70)
    print("AI Legal Monitoring System - Basic Demo")
    print("=" * 70)

    try:
        # Test basic imports
        print("\n1. Testing Core Dependencies...")
        print("-" * 70)

        import flask
        print("✅ Flask imported successfully")

        import requests
        print("✅ Requests imported successfully")

        from bs4 import BeautifulSoup
        print("✅ BeautifulSoup4 imported successfully")

        # Import our modules
        print("\n2. Testing System Modules...")
        print("-" * 70)

        from src.data_collection.scraper import LegalDataScraper
        print("✅ Data Collection module imported")

        from src.analysis.impact_analyzer import ImpactAnalyzer
        print("✅ Impact Analysis module imported")

        from src.analysis.compliance_engine import ComplianceRecommendationEngine
        print("✅ Compliance Engine module imported")

        from src.alerts.alert_manager import AlertManager
        print("✅ Alert Manager module imported")

        from src.audit.audit_logger import AuditLogger
        print("✅ Audit Logger module imported")

        from src.dashboard.api import DashboardAPI
        print("✅ Dashboard API module imported")

        print("\n3. Testing Core Functionality...")
        print("-" * 70)

        # Test scraper
        scraper = LegalDataScraper()
        print("✅ Legal Data Scraper initialized")

        # Test impact analyzer
        analyzer = ImpactAnalyzer()
        print("✅ Impact Analyzer initialized")

        # Test compliance engine
        engine = ComplianceRecommendationEngine()
        print("✅ Compliance Engine initialized")

        # Test alert manager
        alert_manager = AlertManager(
            smtp_server='smtp.gmail.com',
            smtp_port=587,
            sender_email='test@example.com',
            sender_password='test'
        )
        print("✅ Alert Manager initialized")

        # Test audit logger
        audit_logger = AuditLogger()
        print("✅ Audit Logger initialized")

        # Test dashboard API
        dashboard = DashboardAPI()
        print("✅ Dashboard API initialized")

        print("\n4. Sample Data Processing...")
        print("-" * 70)

        # Sample document for testing
        sample_document = {
            'content': '''
            New data protection regulations require companies to implement enhanced privacy measures.
            Personal data processing must now include explicit consent from users.
            Companies must conduct privacy impact assessments for new data processing activities.
            Failure to comply may result in fines up to 4% of global turnover.
            ''',
            'title': 'GDPR Enhancement Regulation 2024',
            'url': 'https://example.gov/gdpr-update',
            'source': 'government'
        }

        print(f"Sample Document: {sample_document['title']}")
        print(f"Content Length: {len(sample_document['content'])} characters")

        # Test impact analysis
        impact_result = analyzer.analyze_impact(sample_document)
        print(f"✅ Impact Analysis: {len(impact_result['affected_categories'])} categories affected")
        print(f"Affected Categories: {', '.join(impact_result['affected_categories'])}")

        # Test compliance recommendations
        recommendations = engine.generate_recommendations(impact_result)
        print(f"✅ Generated {len(recommendations)} compliance recommendations")

        # Show sample recommendation
        if recommendations:
            rec = recommendations[0]
            print(f"Sample Recommendation: {rec['action'][:50]}...")
            print(f"Urgency: {rec['urgency']}, Deadline: {rec['deadline'][:10]}")

        # Test risk assessment
        risks = engine.identify_risks(recommendations)
        print(f"✅ Risk Assessment: Overall risk level = {risks['overall_risk_level']}")

        print("\n5. Sample Alert Generation...")
        print("-" * 70)

        # Generate sample alert
        alert_data = {
            'title': sample_document['title'],
            'summary': sample_document['content'][:200] + '...',
            'source': 'AI Legal Monitoring System',
            'date': '2024-01-15',
            'risk_level': risks['overall_risk_level'],
            'affected_areas': impact_result['affected_categories'],
            'impact_level': impact_result['overall_impact_level'],
            'actions': [rec['action'] for rec in recommendations[:3]]
        }

        subject, plain_body, html_body = alert_manager.generate_alert_email(alert_data)
        print(f"✅ Alert Email Generated: {subject}")
        print(f"Email Length: {len(plain_body)} characters")

        print("\n6. System Status...")
        print("-" * 70)

        # Test compliance status
        compliance_status = engine.get_compliance_status()
        print(f"✅ Compliance Status: {compliance_status}")

        # Test audit logging
        audit_logger.log_document_received(sample_document)
        print("✅ Audit Log: Document received event logged")

        print("\n7. API Endpoints Test...")
        print("-" * 70)

        # Test API health endpoint
        with dashboard.app.test_client() as client:
            response = client.get('/api/health')
            if response.status_code == 200:
                print("✅ API Health Check: OK")
                data = response.get_json()
                print(f"API Version: {data.get('version', 'Unknown')}")
            else:
                print("❌ API Health Check failed")

        print("\n" + "=" * 70)
        print("🎉 AI Legal Monitoring System - Basic Demo Complete!")
        print("=" * 70)

        print("\n📊 Summary:")
        print(f"• Core Dependencies: ✅ Working")
        print(f"• System Modules: ✅ All imported")
        print(f"• Data Processing: ✅ Functional")
        print(f"• Impact Analysis: ✅ {len(impact_result['affected_categories'])} categories")
        print(f"• Recommendations: ✅ {len(recommendations)} generated")
        print(f"• Risk Assessment: ✅ {risks['overall_risk_level']} level")
        print(f"• Alert System: ✅ Email templates generated")
        print(f"• Audit Logging: ✅ Events logged")
        print(f"• API Endpoints: ✅ Health check working")

        print("\n🚀 Next Steps:")
        print("1. Configure email settings in .env file")
        print("2. Add real legal document URLs")
        print("3. Install spaCy for full NLP features:")
        print("   python -m pip install spacy")
        print("   python -m spacy download en_core_web_lg")
        print("4. Start dashboard: python -c \"from src.main import LegalMonitoringSystem; s = LegalMonitoringSystem(); s.start_dashboard()\"")

        return True

    except Exception as e:
        print(f"\n❌ Error during demo: {str(e)}")
        print("\n🔧 Troubleshooting:")
        print("1. Check Python installation: python --version")
        print("2. Install missing dependencies: pip install flask requests beautifulsoup4")
        print("3. For full NLP features, install: pip install spacy && python -m spacy download en_core_web_lg")
        return False


def demo_data_collection():
    """Demonstrate data collection capabilities"""
    print("\n\n📡 Data Collection Demo")
    print("-" * 70)

    try:
        from src.data_collection.scraper import LegalDataScraper

        scraper = LegalDataScraper()

        # Test with a simple webpage
        test_url = "https://httpbin.org/html"  # Simple test page

        print(f"Testing data collection from: {test_url}")

        document = scraper.fetch_from_url(test_url)
        if document:
            print("✅ Document fetched successfully")
            print(f"Title: {document.get('title', 'No title')}")
            print(f"Content Length: {len(document.get('content', ''))} characters")
        else:
            print("❌ Failed to fetch document")

    except Exception as e:
        print(f"❌ Data collection error: {str(e)}")


if __name__ == "__main__":
    success = demo_basic_functionality()
    if success:
        demo_data_collection()

    print("\n" + "=" * 70)
    print("Demo completed. Check the output above for results.")
    print("=" * 70)