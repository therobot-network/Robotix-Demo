#!/usr/bin/env python3
"""
Update metadata.json to include financial and marketing datasets
"""

import json
import os
from datetime import datetime

def update_metadata():
    """Update metadata.json with new financial and marketing datasets"""
    
    # Path to metadata file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    metadata_path = os.path.join(project_dir, "data", "metadata.json")
    
    # Load existing metadata
    with open(metadata_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    # Add new financial datasets
    metadata['datasets']['invoices'] = {
        "record_count": 200,
        "fields": [
            "invoice_id",
            "customer_id",
            "order_id",
            "invoice_date",
            "due_date",
            "subtotal",
            "tax",
            "shipping",
            "total",
            "payment_status",
            "payment_date",
            "payment_method",
            "notes"
        ]
    }
    
    # Add marketing campaigns
    metadata['datasets']['marketing_campaigns'] = {
        "record_count": 50,
        "fields": [
            "campaign_id",
            "campaign_name",
            "campaign_type",
            "target_audience",
            "start_date",
            "end_date",
            "budget",
            "actual_spend",
            "leads_generated",
            "conversions",
            "conversion_rate",
            "revenue_generated",
            "roi",
            "status",
            "owner",
            "notes"
        ]
    }
    
    # Update generated date
    metadata['generated_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save updated metadata
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"✅ Updated {metadata_path}")
    print(f"   - Added 'invoices' dataset (200 records)")
    print(f"   - Added 'marketing_campaigns' dataset (50 records)")

if __name__ == "__main__":
    update_metadata()

