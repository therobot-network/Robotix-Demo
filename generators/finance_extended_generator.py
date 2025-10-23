#!/usr/bin/env python3
"""
Finance Extended Data Generator
Generates additional finance data: expenses, cash flow, debt, AR/AP, vendors
"""

import json
import csv
import random
import os
from datetime import datetime, timedelta
from pathlib import Path
import sys
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))
from company_data import EMPLOYEES, DEPARTMENTS, get_random_date, format_date

# Load environment variables
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
env_path = os.path.join(project_root, '.env')
load_dotenv(env_path)

# AI Integration
try:
    from langchain_anthropic import ChatAnthropic
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    print("⚠️  LangChain not installed.")


class FinanceExtendedGenerator:
    
    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = Path(data_dir)
        self.finance_dir = self.data_dir / "finance"
        self.use_ai = use_ai and AI_AVAILABLE
        
        # Initialize AI
        if self.use_ai:
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key:
                self.llm = ChatAnthropic(
                    model="claude-3-5-sonnet-20241022",
                    temperature=0.7,
                    max_tokens=2000
                )
                print("✅ AI content generation enabled")
            else:
                self.use_ai = False
                print("⚠️  ANTHROPIC_API_KEY not found.")
        
        # Ensure directories exist
        (self.finance_dir / "expenses").mkdir(parents=True, exist_ok=True)
        (self.finance_dir / "cash_flow").mkdir(parents=True, exist_ok=True)
        (self.finance_dir / "debt").mkdir(parents=True, exist_ok=True)
        (self.finance_dir / "ar_ap").mkdir(parents=True, exist_ok=True)
        (self.finance_dir / "vendors").mkdir(parents=True, exist_ok=True)
        
        self.expense_categories = [
            "Salaries & Wages", "Benefits", "Office Rent", "Utilities",
            "Marketing & Advertising", "Travel & Entertainment", "Software & Licenses",
            "Equipment & Maintenance", "Professional Services", "Insurance",
            "Supplies", "Shipping & Freight", "Telecommunications", "Training",
            "R&D Materials", "Facility Maintenance", "Depreciation"
        ]
        
        self.vendor_categories = [
            "Component Supplier", "Software Vendor", "Logistics Provider",
            "Professional Services", "Facility Services", "Equipment Supplier",
            "Marketing Agency", "Consulting", "Insurance Provider"
        ]
        
    def generate_monthly_expenses(self, num_months=24):
        """Generate detailed monthly expenses by department and category"""
        print(f"Generating monthly expense records for {num_months} months...")
        
        expenses = []
        expense_id = 1
        
        # Start from 24 months ago
        start_date = datetime.now() - timedelta(days=30*num_months)
        
        for month_offset in range(num_months):
            month_date = start_date + timedelta(days=30*month_offset)
            month_str = month_date.strftime("%Y-%m")
            
            for dept in DEPARTMENTS:
                # Base department monthly budget based on department type
                if "Executive" in dept:
                    dept_budget = 220000
                elif "Product" in dept or "Development" in dept or "Engineering" in dept:
                    dept_budget = 450000
                elif "Sales" in dept or "Marketing" in dept:
                    dept_budget = 320000
                elif "Manufacturing" in dept or "Operations" in dept:
                    dept_budget = 380000
                elif "Finance" in dept or "Accounting" in dept:
                    dept_budget = 140000
                elif "Human Resources" in dept or "HR" in dept:
                    dept_budget = 95000
                elif "Customer" in dept or "Support" in dept or "Service" in dept:
                    dept_budget = 110000
                elif "Quality" in dept:
                    dept_budget = 120000
                else:
                    dept_budget = 100000
                
                # Distribute budget across expense categories
                for category in self.expense_categories:
                    # Different departments have different expense patterns
                    if category == "Salaries & Wages":
                        amount = dept_budget * random.uniform(0.55, 0.65)
                    elif category == "Benefits":
                        amount = dept_budget * random.uniform(0.12, 0.18)
                    elif category == "Marketing & Advertising" and ("Marketing" in dept or "Sales" in dept):
                        amount = dept_budget * random.uniform(0.15, 0.25)
                    elif category == "R&D Materials" and ("Product" in dept or "Development" in dept):
                        amount = dept_budget * random.uniform(0.08, 0.12)
                    elif category == "Travel & Entertainment" and ("Sales" in dept or "Executive" in dept):
                        amount = dept_budget * random.uniform(0.05, 0.10)
                    else:
                        amount = dept_budget * random.uniform(0.01, 0.05)
                    
                    # Add some variance
                    variance = random.uniform(-0.15, 0.15)
                    actual_amount = amount * (1 + variance)
                    budget_amount = amount
                    
                    expenses.append({
                        "expense_id": f"EXP-{expense_id:06d}",
                        "month": month_str,
                        "department": dept,
                        "category": category,
                        "budget_amount": round(budget_amount, 2),
                        "actual_amount": round(actual_amount, 2),
                        "variance": round(actual_amount - budget_amount, 2),
                        "variance_pct": round(((actual_amount - budget_amount) / budget_amount) * 100, 2),
                        "status": "Approved" if actual_amount <= budget_amount * 1.1 else "Requires Review",
                        "notes": "" if abs(variance) < 0.1 else "Variance exceeds threshold"
                    })
                    expense_id += 1
        
        self._export_to_csv_json(expenses, self.finance_dir / "expenses" / "monthly_expenses")
        print(f"✓ Generated {len(expenses)} monthly expense records")
        return expenses
    
    def generate_cash_flow_statements(self, num_months=24):
        """Generate monthly cash flow statements"""
        print(f"Generating cash flow statements for {num_months} months...")
        
        cash_flows = []
        starting_cash = 8500000  # $8.5M starting cash
        
        start_date = datetime.now() - timedelta(days=30*num_months)
        
        for month_offset in range(num_months):
            month_date = start_date + timedelta(days=30*month_offset)
            month_str = month_date.strftime("%Y-%m")
            
            # Operating activities
            revenue = random.uniform(3200000, 4500000)
            operating_expenses = random.uniform(2800000, 3600000)
            depreciation = random.uniform(80000, 120000)
            change_ar = random.uniform(-200000, 200000)
            change_ap = random.uniform(-150000, 150000)
            change_inventory = random.uniform(-100000, 100000)
            
            operating_cash = (revenue - operating_expenses + depreciation - 
                            change_ar + change_ap - change_inventory)
            
            # Investing activities
            capex = random.uniform(-150000, -50000) if random.random() > 0.3 else 0
            asset_sales = random.uniform(0, 50000) if random.random() > 0.8 else 0
            investing_cash = capex + asset_sales
            
            # Financing activities
            debt_proceeds = random.uniform(0, 500000) if random.random() > 0.9 else 0
            debt_repayment = random.uniform(-100000, 0) if random.random() > 0.7 else 0
            dividends = 0  # Private company
            financing_cash = debt_proceeds + debt_repayment + dividends
            
            # Total cash flow
            net_change = operating_cash + investing_cash + financing_cash
            ending_cash = starting_cash + net_change
            
            cash_flows.append({
                "month": month_str,
                "beginning_cash": round(starting_cash, 2),
                # Operating
                "revenue_collected": round(revenue, 2),
                "operating_expenses_paid": round(-operating_expenses, 2),
                "depreciation": round(depreciation, 2),
                "change_accounts_receivable": round(change_ar, 2),
                "change_accounts_payable": round(change_ap, 2),
                "change_inventory": round(change_inventory, 2),
                "operating_cash_flow": round(operating_cash, 2),
                # Investing
                "capital_expenditures": round(capex, 2),
                "asset_sales": round(asset_sales, 2),
                "investing_cash_flow": round(investing_cash, 2),
                # Financing
                "debt_proceeds": round(debt_proceeds, 2),
                "debt_repayment": round(debt_repayment, 2),
                "dividends_paid": round(dividends, 2),
                "financing_cash_flow": round(financing_cash, 2),
                # Totals
                "net_cash_change": round(net_change, 2),
                "ending_cash": round(ending_cash, 2),
                "days_cash_on_hand": round((ending_cash / (operating_expenses / 30)), 1)
            })
            
            starting_cash = ending_cash
        
        self._export_to_csv_json(cash_flows, self.finance_dir / "cash_flow" / "monthly_cash_flow")
        print(f"✓ Generated {len(cash_flows)} cash flow statements")
        return cash_flows
    
    def generate_debt_schedule(self):
        """Generate debt and loan schedule"""
        print("Generating debt schedule...")
        
        debts = []
        
        # Term Loan
        debts.append({
            "loan_id": "LOAN-001",
            "loan_type": "Term Loan",
            "lender": "First National Bank",
            "principal_amount": 5000000,
            "outstanding_balance": 3200000,
            "interest_rate": 5.25,
            "monthly_payment": 47500,
            "origination_date": "2022-03-15",
            "maturity_date": "2027-03-15",
            "payment_frequency": "Monthly",
            "collateral": "Equipment and Inventory",
            "covenants": "Debt Service Coverage Ratio > 1.25x",
            "status": "Active"
        })
        
        # Line of Credit
        debts.append({
            "loan_id": "LOC-001",
            "loan_type": "Line of Credit",
            "lender": "Pacific Business Bank",
            "principal_amount": 2000000,
            "outstanding_balance": 800000,
            "interest_rate": 6.75,
            "monthly_payment": 0,  # Variable based on usage
            "origination_date": "2023-01-10",
            "maturity_date": "2025-01-10",
            "payment_frequency": "Interest Only Monthly",
            "collateral": "Accounts Receivable",
            "covenants": "Current Ratio > 1.5x",
            "status": "Active"
        })
        
        # Equipment Financing
        debts.append({
            "loan_id": "LOAN-002",
            "loan_type": "Equipment Financing",
            "lender": "Industrial Equipment Finance",
            "principal_amount": 1200000,
            "outstanding_balance": 650000,
            "interest_rate": 4.95,
            "monthly_payment": 18500,
            "origination_date": "2023-06-01",
            "maturity_date": "2028-06-01",
            "payment_frequency": "Monthly",
            "collateral": "Manufacturing Equipment",
            "covenants": "None",
            "status": "Active"
        })
        
        # Calculate ratios
        total_debt = sum(d["outstanding_balance"] for d in debts)
        total_equity = 12000000  # Approximate
        debt_to_equity = total_debt / total_equity
        
        # Add summary record
        debts.append({
            "loan_id": "SUMMARY",
            "loan_type": "Total Outstanding",
            "lender": "Multiple",
            "principal_amount": sum(d["principal_amount"] for d in debts if d["loan_id"] != "SUMMARY"),
            "outstanding_balance": total_debt,
            "interest_rate": 0,
            "monthly_payment": sum(d["monthly_payment"] for d in debts if d["loan_id"] != "SUMMARY"),
            "origination_date": "",
            "maturity_date": "",
            "payment_frequency": "",
            "collateral": "",
            "covenants": f"Debt-to-Equity: {debt_to_equity:.2f}x",
            "status": "Summary"
        })
        
        self._export_to_csv_json(debts, self.finance_dir / "debt" / "debt_schedule")
        print(f"✓ Generated debt schedule with {len(debts)} entries")
        return debts
    
    def generate_ar_aging(self):
        """Generate accounts receivable aging report"""
        print("Generating AR aging report...")
        
        # Load invoices to create AR
        invoices_path = self.finance_dir / "invoices" / "invoices.json"
        with open(invoices_path) as f:
            invoices = json.load(f)
        
        ar_records = []
        current_date = datetime.now()
        
        for inv in invoices:
            if inv["payment_status"] in ["Pending", "Overdue"]:
                invoice_date = datetime.strptime(inv["invoice_date"], "%Y-%m-%d")
                due_date = datetime.strptime(inv["due_date"], "%Y-%m-%d")
                days_outstanding = (current_date - invoice_date).days
                days_overdue = (current_date - due_date).days if current_date > due_date else 0
                
                # Aging buckets
                if days_outstanding <= 30:
                    bucket = "0-30 days"
                elif days_outstanding <= 60:
                    bucket = "31-60 days"
                elif days_outstanding <= 90:
                    bucket = "61-90 days"
                else:
                    bucket = "90+ days"
                
                ar_records.append({
                    "invoice_id": inv["invoice_id"],
                    "customer_id": inv["customer_id"],
                    "invoice_date": inv["invoice_date"],
                    "due_date": inv["due_date"],
                    "amount": inv["total"],
                    "days_outstanding": days_outstanding,
                    "days_overdue": days_overdue,
                    "aging_bucket": bucket,
                    "payment_status": inv["payment_status"],
                    "risk_level": "High" if days_overdue > 60 else "Medium" if days_overdue > 30 else "Low"
                })
        
        self._export_to_csv_json(ar_records, self.finance_dir / "ar_ap" / "accounts_receivable_aging")
        print(f"✓ Generated {len(ar_records)} AR aging records")
        return ar_records
    
    def generate_ap_aging(self, num_records=150):
        """Generate accounts payable aging report"""
        print(f"Generating AP aging report with {num_records} records...")
        
        ap_records = []
        vendors = self._generate_vendor_list()
        current_date = datetime.now()
        
        for i in range(num_records):
            vendor = random.choice(vendors)
            invoice_date = current_date - timedelta(days=random.randint(1, 120))
            payment_terms = random.choice([30, 45, 60])
            due_date = invoice_date + timedelta(days=payment_terms)
            amount = random.uniform(5000, 150000)
            days_outstanding = (current_date - invoice_date).days
            days_overdue = (current_date - due_date).days if current_date > due_date else 0
            
            # Aging buckets
            if days_outstanding <= 30:
                bucket = "0-30 days"
            elif days_outstanding <= 60:
                bucket = "31-60 days"
            elif days_outstanding <= 90:
                bucket = "61-90 days"
            else:
                bucket = "90+ days"
            
            status = "Scheduled" if days_overdue <= 0 else "Overdue"
            
            ap_records.append({
                "ap_id": f"AP-{i+1:05d}",
                "vendor_id": vendor["vendor_id"],
                "vendor_name": vendor["vendor_name"],
                "invoice_number": f"VINV-{random.randint(10000, 99999)}",
                "invoice_date": invoice_date.strftime("%Y-%m-%d"),
                "due_date": due_date.strftime("%Y-%m-%d"),
                "amount": round(amount, 2),
                "days_outstanding": days_outstanding,
                "days_overdue": days_overdue,
                "aging_bucket": bucket,
                "payment_status": status,
                "payment_terms": f"Net {payment_terms}",
                "category": vendor["category"]
            })
        
        self._export_to_csv_json(ap_records, self.finance_dir / "ar_ap" / "accounts_payable_aging")
        print(f"✓ Generated {len(ap_records)} AP aging records")
        return ap_records
    
    def _generate_vendor_list(self):
        """Generate vendor master list"""
        vendors = [
            {"vendor_id": "VEN-001", "vendor_name": "Precision Components Inc", "category": "Component Supplier"},
            {"vendor_id": "VEN-002", "vendor_name": "TechMotion Systems", "category": "Component Supplier"},
            {"vendor_id": "VEN-003", "vendor_name": "Industrial Sensors Co", "category": "Component Supplier"},
            {"vendor_id": "VEN-004", "vendor_name": "Atlas Logistics", "category": "Logistics Provider"},
            {"vendor_id": "VEN-005", "vendor_name": "CloudSoft Solutions", "category": "Software Vendor"},
            {"vendor_id": "VEN-006", "vendor_name": "Enterprise Systems Inc", "category": "Software Vendor"},
            {"vendor_id": "VEN-007", "vendor_name": "DataGuard Security", "category": "Software Vendor"},
            {"vendor_id": "VEN-008", "vendor_name": "BuildRight Construction", "category": "Facility Services"},
            {"vendor_id": "VEN-009", "vendor_name": "Bright Marketing Group", "category": "Marketing Agency"},
            {"vendor_id": "VEN-010", "vendor_name": "Strategic Advisors LLC", "category": "Consulting"},
            {"vendor_id": "VEN-011", "vendor_name": "Premier Insurance Group", "category": "Insurance Provider"},
            {"vendor_id": "VEN-012", "vendor_name": "Elite Equipment Supply", "category": "Equipment Supplier"},
            {"vendor_id": "VEN-013", "vendor_name": "Global Freight Services", "category": "Logistics Provider"},
            {"vendor_id": "VEN-014", "vendor_name": "Innovation Labs", "category": "Professional Services"},
            {"vendor_id": "VEN-015", "vendor_name": "Metro Facilities Management", "category": "Facility Services"}
        ]
        return vendors
    
    def generate_vendor_spend(self, num_months=24):
        """Generate vendor spend analysis"""
        print(f"Generating vendor spend data for {num_months} months...")
        
        vendors = self._generate_vendor_list()
        spend_records = []
        
        start_date = datetime.now() - timedelta(days=30*num_months)
        
        for month_offset in range(num_months):
            month_date = start_date + timedelta(days=30*month_offset)
            month_str = month_date.strftime("%Y-%m")
            
            for vendor in vendors:
                # Different vendor types have different spend patterns
                if vendor["category"] == "Component Supplier":
                    base_spend = random.uniform(100000, 300000)
                elif vendor["category"] == "Software Vendor":
                    base_spend = random.uniform(15000, 50000)
                elif vendor["category"] == "Logistics Provider":
                    base_spend = random.uniform(30000, 80000)
                else:
                    base_spend = random.uniform(10000, 60000)
                
                num_invoices = random.randint(1, 8)
                avg_invoice = base_spend / num_invoices
                
                spend_records.append({
                    "month": month_str,
                    "vendor_id": vendor["vendor_id"],
                    "vendor_name": vendor["vendor_name"],
                    "category": vendor["category"],
                    "total_spend": round(base_spend, 2),
                    "num_invoices": num_invoices,
                    "avg_invoice_amount": round(avg_invoice, 2),
                    "payment_terms": random.choice(["Net 30", "Net 45", "Net 60", "Due on Receipt"]),
                    "on_time_payment_pct": round(random.uniform(85, 100), 1)
                })
        
        self._export_to_csv_json(spend_records, self.finance_dir / "vendors" / "vendor_spend")
        
        # Also create vendor master list
        self._export_to_csv_json(vendors, self.finance_dir / "vendors" / "vendor_master")
        
        print(f"✓ Generated {len(spend_records)} vendor spend records")
        return spend_records
    
    def _export_to_csv_json(self, data, base_filename):
        """Export data to both CSV and JSON formats"""
        if not data:
            return
        
        # CSV export
        csv_path = f"{base_filename}.csv"
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        # JSON export
        json_path = f"{base_filename}.json"
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)


def main():
    print("=" * 60)
    print("Finance Extended Data Generator")
    print("=" * 60)
    
    generator = FinanceExtendedGenerator()
    
    # Generate all finance data
    generator.generate_monthly_expenses(num_months=24)
    generator.generate_cash_flow_statements(num_months=24)
    generator.generate_debt_schedule()
    generator.generate_vendor_spend(num_months=24)
    generator.generate_ar_aging()
    generator.generate_ap_aging(num_records=150)
    
    print("\n" + "=" * 60)
    print("✓ Finance extended data generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

