"""
Example usage of AI Legal Monitoring System
"""
import json
from src.main import LegalMonitoringSystem


def example_process_document():
    """Example: Process a legal document"""
    print("=" * 70)
    print("AI Legal Monitoring System - Example Usage")
    print("=" * 70)
    
    # Initialize system
    system = LegalMonitoringSystem()
    
    # Example 1: Process a legal document URL
    print("\n1. Processing Legal Document...")
    print("-" * 70)
    
    # In production, use real legal document URLs
    test_url = "https://example.com/legal-update"
    
    # Note: actual processing requires internet connectivity
    # This is a template for demonstration
    print(f"URL: {test_url}")
    print("Status: Ready to process")
    print("\nTo process:\n")
    print("  result = system.process_legal_content(test_url)")
    print("  print(json.dumps(result, indent=2))")
    
    # Example 2: Alert generation structure
    print("\n\n2. Alert Example Structure")
    print("-" * 70)
    
    sample_alert = {
        "title": "GDPR Compliance Update 2024",
        "summary": "New requirements for data subject rights have been introduced...",
        "source": "EU Regulations",
        "date": "2024-01-15",
        "risk_level": "High",
        "affected_areas": ["Data & Privacy", "Operations"],
        "impact_level": "High",
        "actions": [
            "Audit current data collection practices",
            "Update privacy policy",
            "Conduct privacy impact assessment"
        ]
    }
    
    print(json.dumps(sample_alert, indent=2))
    
    # Example 3: Send alerts to recipients
    print("\n\n3. Sending Alerts")
    print("-" * 70)
    
    recipients = [
        "legal@company.com",
        "compliance@company.com",
        "it@company.com"
    ]
    
    print(f"Recipients: {', '.join(recipients)}")
    print("\nTo send alerts:\n")
    print("  system.send_alerts(result, recipients)")
    
    # Example 4: Compliance Status
    print("\n\n4. Compliance Status")
    print("-" * 70)
    
    status = system.get_compliance_status()
    print(f"Overall Compliance Score: {status.get('compliance_score', 0)}%")
    print(f"Risk Level: {status.get('risk_level', 'Unknown')}")
    print(f"Pending Actions: {status.get('pending_actions', 0)}")
    print(f"Completed Actions: {status.get('completed_actions', 0)}")
    
    # Example 5: Impact analysis output format
    print("\n\n5. Impact Analysis Output Format")
    print("-" * 70)
    
    sample_impact = {
        "document_id": "https://example.com/legal-update",
        "impacts_by_category": {
            "Data & Privacy": {
                "affected": True,
                "impact_level": "High",
                "relevant_keywords": ["personal data", "privacy", "consent"]
            },
            "Employment": {
                "affected": True,
                "impact_level": "Medium",
                "relevant_keywords": ["employee", "working hours"]
            }
        },
        "affected_categories": ["Data & Privacy", "Employment"],
        "overall_impact_level": "High",
        "requires_action": True
    }
    
    print(json.dumps(sample_impact, indent=2))
    
    # Example 6: Recommendations output format
    print("\n\n6. Compliance Recommendations Output Format")
    print("-" * 70)
    
    sample_recommendations = [
        {
            "action": "Audit current data collection practices",
            "category": "Data & Privacy",
            "urgency": "High",
            "timeline": "7 days",
            "responsible": "Privacy Officer",
            "created_date": "2024-01-15T10:00:00",
            "deadline": "2024-01-22T10:00:00",
            "status": "pending"
        },
        {
            "action": "Update privacy policy",
            "category": "Data & Privacy",
            "urgency": "High",
            "timeline": "14 days",
            "responsible": "Legal",
            "created_date": "2024-01-15T10:00:00",
            "deadline": "2024-01-29T10:00:00",
            "status": "pending"
        }
    ]
    
    print(json.dumps(sample_recommendations, indent=2))
    
    # Example 7: Audit Log Entry
    print("\n\n7. Audit Log Entry Example")
    print("-" * 70)
    
    sample_audit = {
        "event_type": "DOCUMENT_PROCESSED",
        "timestamp": "2024-01-15T10:30:00",
        "document_id": "https://example.com/legal-update",
        "status": "document_processed"
    }
    
    print(json.dumps(sample_audit, indent=2))
    
    print("\n" + "=" * 70)
    print("For more documentation, see README.md")
    print("=" * 70)


def example_batch_processing():
    """Example: Process multiple documents"""
    print("\n\nExample: Batch Document Processing")
    print("-" * 70)
    
    system = LegalMonitoringSystem()
    
    # List of documents to process
    documents = [
        "https://example.gov/law-update-1",
        "https://courts.example.gov/decision-123",
        "https://regulator.example.gov/guidance-2024"
    ]
    
    results = []
    for doc_url in documents:
        print(f"\nProcessing: {doc_url}")
        # result = system.process_legal_content(doc_url)
        # results.append(result)
    
    print(f"\nTotal documents processed: {len(results)}")


def example_department_alerts():
    """Example: Department-specific alerts"""
    print("\n\nExample: Department-Specific Alerts")
    print("-" * 70)
    
    department_contacts = {
        "Legal": ["legal@company.com", "legal-manager@company.com"],
        "HR": ["hr@company.com", "hr-director@company.com"],
        "IT": ["ciso@company.com", "it-security@company.com"],
        "Finance": ["cfo@company.com", "compliance@company.com"],
        "Operations": ["ops-manager@company.com"]
    }
    
    print("Department Contact Mapping:")
    for dept, contacts in department_contacts.items():
        print(f"  {dept}: {', '.join(contacts)}")
    
    print("\nWhen alerts are sent, affected departments receive targeted notifications")


if __name__ == "__main__":
    example_process_document()
    example_batch_processing()
    example_department_alerts()
