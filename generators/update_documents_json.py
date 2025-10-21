#!/usr/bin/env python3
"""
Update website documents.json to include new financial and marketing HTML documents
"""

import json
import os


def update_documents_json():
    """Update documents.json with new HTML documents"""

    # Path to documents file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    docs_path = os.path.join(project_dir, "website", "src", "data", "documents.json")

    # Load existing documents
    with open(docs_path, "r", encoding="utf-8") as f:
        documents = json.load(f)

    # Add financial budget reports
    quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024", "Q1 2025"]
    for quarter in quarters:
        doc_id = f"budget-report-{quarter.lower().replace(' ', '-')}"
        # Check if already exists
        if not any(d["id"] == doc_id for d in documents):
            documents.append(
                {
                    "id": doc_id,
                    "title": f"Budget Report - {quarter}",
                    "category": "Financial",
                    "type": "Budget Report",
                    "path": f"/html_documents/financial/budget-report---{quarter.lower().replace(' ', '-')}.html",
                    "description": f"Quarterly budget report for {quarter} showing revenue and expenses by department",
                }
            )

    # Add marketing customer feedback forms
    survey_types = [
        (
            "product-satisfaction-survey",
            "Product Satisfaction Survey",
            "Customer survey about product quality and satisfaction",
        ),
        (
            "customer-service-experience-survey",
            "Customer Service Experience Survey",
            "Survey about customer service interactions and support quality",
        ),
        (
            "post-purchase-feedback-form",
            "Post-Purchase Feedback Form",
            "Feedback form for customers after product delivery",
        ),
    ]

    for doc_id, title, description in survey_types:
        # Check if already exists
        if not any(d["id"] == doc_id for d in documents):
            documents.append(
                {
                    "id": doc_id,
                    "title": title,
                    "category": "Marketing",
                    "type": "Survey Template",
                    "path": f"/html_documents/marketing/{doc_id}.html",
                    "description": description,
                }
            )

    # Save updated documents
    with open(docs_path, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    print(f"✅ Updated {docs_path}")
    print(f"   - Added 5 financial budget reports")
    print(f"   - Added 3 marketing feedback forms")
    print(f"   - Total documents: {len(documents)}")


if __name__ == "__main__":
    update_documents_json()
