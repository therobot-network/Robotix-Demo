#!/usr/bin/env python3
"""
Standalone Sales & Marketing Data Generator
Generates only sales and marketing extended datasets
"""

import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))

from sales_marketing_extended_generator import SalesMarketingExtendedGenerator

def main():
    print("\n" + "="*70)
    print("ROBOTIX - SALES & MARKETING DATA GENERATION")
    print("="*70)
    print(f"\nStart Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Using AI: Yes (Claude 3.5 Sonnet)\n")
    
    try:
        # Initialize generator
        generator = SalesMarketingExtendedGenerator(
            data_dir="../data",
            use_ai=True
        )
        
        print("\n" + "-"*70)
        print("GENERATING SALES & MARKETING DATA")
        print("-"*70)
        print("Generating: pipeline, quotes, forecasts, quotas, engagement, lead scoring...\n")
        
        # Generate all datasets
        generator.generate_sales_pipeline(num_opportunities=200)
        generator.generate_quotes(num_quotes=150)
        generator.generate_sales_forecasts(num_quarters=8)
        generator.generate_quota_attainment(num_quarters=6)
        generator.generate_marketing_engagement(num_months=24)
        generator.generate_lead_scoring(num_leads=500)
        
        print("\n" + "="*70)
        print("✅ SALES & MARKETING DATA GENERATION COMPLETE!")
        print("="*70)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
    except Exception as e:
        print(f"\n❌ Error during generation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

