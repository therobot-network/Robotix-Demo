#!/usr/bin/env python3
"""
Master Script - Generate All Extended Data
Runs all extended generators to fill data gaps for analytics queries
"""

import sys
import time
from datetime import datetime
from pathlib import Path

# Import all generators
from finance_extended_generator import FinanceExtendedGenerator
from hr_extended_generator import HRExtendedGenerator
from legal_contracts_generator import LegalContractsGenerator
from product_extended_generator import ProductExtendedGenerator
from sales_marketing_extended_generator import SalesMarketingExtendedGenerator


def print_header():
    print("\n" + "=" * 70)
    print("ROBOTIX - EXTENDED DATA GENERATION SUITE")
    print("Filling Data Gaps for Comprehensive Analytics")
    print("=" * 70 + "\n")


def print_section(title):
    print("\n" + "-" * 70)
    print(f" {title}")
    print("-" * 70)


def main():
    start_time = time.time()
    print_header()
    
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Using AI: Yes (Claude 3.5 Sonnet)\n")
    
    # Track statistics
    stats = {
        "generators_run": 0,
        "total_records": 0,
        "files_created": 0
    }
    
    try:
        # 1. Finance Extended Data
        print_section("1. FINANCE EXTENDED DATA")
        print("Generating: expenses, cash flow, debt, AR/AP, vendor data...")
        finance_gen = FinanceExtendedGenerator(use_ai=True)
        
        finance_gen.generate_monthly_expenses(num_months=24)
        finance_gen.generate_cash_flow_statements(num_months=24)
        finance_gen.generate_debt_schedule()
        finance_gen.generate_vendor_spend(num_months=24)
        finance_gen.generate_ar_aging()
        finance_gen.generate_ap_aging(num_records=150)
        
        stats["generators_run"] += 1
        stats["total_records"] += (24*17*8 + 24 + 4 + 24*15 + 150 + 150)  # Approximate
        stats["files_created"] += 12  # 6 datasets * 2 formats
        
        # 2. HR Extended Data
        print_section("2. HR EXTENDED DATA")
        print("Generating: headcount, attrition, recruiting, training, diversity...")
        hr_gen = HRExtendedGenerator(use_ai=True)
        
        hr_gen.generate_historical_headcount(num_months=36)
        hr_gen.generate_attrition_records(num_records=80)
        hr_gen.generate_recruiting_pipeline(num_records=120)
        hr_gen.generate_training_records(num_records=300)
        hr_gen.generate_diversity_records()
        hr_gen.generate_compensation_analysis()
        
        stats["generators_run"] += 1
        stats["total_records"] += (36*8 + 80 + 120 + 300 + 50 + 64)
        stats["files_created"] += 14
        
        # 3. Legal & Contracts Data
        print_section("3. LEGAL & CONTRACTS DATA")
        print("Generating: contracts, litigation, compliance, IP portfolio...")
        legal_gen = LegalContractsGenerator(use_ai=True)
        
        legal_gen.generate_contracts(num_contracts=100)
        legal_gen.generate_litigation_records(num_cases=25)
        legal_gen.generate_compliance_records(num_records=60)
        legal_gen.generate_ip_portfolio()
        
        stats["generators_run"] += 1
        stats["total_records"] += (100 + 25 + 60 + 19)
        stats["files_created"] += 8
        
        # 4. Product Extended Data
        print_section("4. PRODUCT EXTENDED DATA")
        print("Generating: releases, bugs, features, user metrics, feedback...")
        product_gen = ProductExtendedGenerator(use_ai=True)
        
        product_gen.generate_product_releases(num_releases=20)
        product_gen.generate_bug_records(num_bugs=250)
        product_gen.generate_feature_adoption(num_features=40)
        product_gen.generate_user_metrics(num_months=24)
        product_gen.generate_customer_feedback(num_feedback=150)
        
        stats["generators_run"] += 1
        stats["total_records"] += (20 + 250 + 40 + 72 + 150)
        stats["files_created"] += 10
        
        # 5. Sales & Marketing Extended Data
        print_section("5. SALES & MARKETING EXTENDED DATA")
        print("Generating: pipeline, quotes, forecasts, quotas, engagement, lead scoring...")
        sales_mkt_gen = SalesMarketingExtendedGenerator(use_ai=True)
        
        sales_mkt_gen.generate_sales_pipeline(num_opportunities=200)
        sales_mkt_gen.generate_quotes(num_quotes=150)
        sales_mkt_gen.generate_sales_forecasts(num_quarters=8)
        sales_mkt_gen.generate_quota_attainment(num_quarters=6)
        sales_mkt_gen.generate_marketing_engagement(num_months=24)
        sales_mkt_gen.generate_lead_scoring(num_leads=500)
        
        stats["generators_run"] += 1
        stats["total_records"] += (200 + 150 + 160 + 120 + 120 + 500)
        stats["files_created"] += 12
        
    except Exception as e:
        print(f"\n❌ Error during generation: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Print Summary
    elapsed_time = time.time() - start_time
    
    print("\n" + "=" * 70)
    print(" GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\n📊 Statistics:")
    print(f"   • Generators Run: {stats['generators_run']}")
    print(f"   • Total Records: {stats['total_records']:,}")
    print(f"   • Files Created: {stats['files_created']} (CSV + JSON pairs)")
    print(f"   • Time Elapsed: {elapsed_time:.1f} seconds")
    print(f"   • End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n✅ All extended data has been generated successfully!")
    print("   Data is now ready for comprehensive analytics queries.\n")
    
    print("📁 Data Locations:")
    print("   • Finance: data/finance/")
    print("   • HR: data/hr-legal/hr/")
    print("   • Legal: data/hr-legal/legal/")
    print("   • Product: data/product/")
    print("   • Sales/Marketing: data/sales-marketing/")
    
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()

