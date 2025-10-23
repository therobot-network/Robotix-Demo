#!/usr/bin/env python3
"""
Finance Compensation Data Generator
Generates finance-related compensation data: payroll liabilities, benefits costs,
payroll taxes, compensation accruals, and related financial accounting data.
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
    print("⚠️  LangChain not installed. AI features disabled.")


class FinanceCompensationGenerator:
    
    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = Path(data_dir)
        self.finance_dir = self.data_dir / "finance"
        self.comp_dir = self.finance_dir / "compensation"
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
                print("⚠️  ANTHROPIC_API_KEY not found. AI features disabled.")
        
        # Ensure directories exist
        self.comp_dir.mkdir(parents=True, exist_ok=True)
        
        # Load HR compensation data for reference
        self.hr_comp_data = self._load_hr_compensation()
        
        # Company employee count and payroll constants
        self.total_employees = 290
        self.avg_salary = 105000
        self.total_annual_payroll = self.total_employees * self.avg_salary
        
    def _load_hr_compensation(self):
        """Load HR compensation data for reference"""
        hr_comp_path = self.data_dir / "hr-legal" / "compensation" / "compensation_analysis.json"
        if hr_comp_path.exists():
            with open(hr_comp_path) as f:
                return json.load(f)
        return []
    
    def generate_payroll_liability_ledger(self, num_months=24):
        """Generate monthly payroll liability tracking"""
        print(f"Generating payroll liability ledger for {num_months} months...")
        
        records = []
        record_id = 1
        start_date = datetime.now() - timedelta(days=30*num_months)
        
        # Track running balances
        accrued_wages_balance = 0
        accrued_bonus_balance = 0
        
        for month_offset in range(num_months):
            month_date = start_date + timedelta(days=30*month_offset)
            month_str = month_date.strftime("%Y-%m")
            month_name = month_date.strftime("%B %Y")
            
            for dept in DEPARTMENTS:
                # Get employee count and avg salary for department
                dept_data = next((d for d in self.hr_comp_data if d["department"] == dept), None)
                if dept_data:
                    emp_count = dept_data["employee_count"]
                    avg_salary = dept_data["avg_base_salary"]
                    avg_bonus_pct = dept_data["avg_bonus_pct"] / 100
                else:
                    emp_count = random.randint(15, 40)
                    avg_salary = 95000
                    avg_bonus_pct = 0.10
                
                # Monthly payroll calculations
                gross_wages = (emp_count * avg_salary) / 12
                
                # Payroll taxes (employer portion)
                fica_medicare = gross_wages * 0.0765  # 7.65% (SS + Medicare)
                futa = gross_wages * 0.006  # 0.6% federal unemployment
                suta = gross_wages * 0.027  # 2.7% state unemployment (varies by state)
                
                # Benefits (employer costs)
                health_insurance = emp_count * random.uniform(450, 650)  # per employee per month
                retirement_401k_match = gross_wages * random.uniform(0.03, 0.06)  # 3-6% match
                life_insurance = emp_count * random.uniform(25, 50)
                disability_insurance = emp_count * random.uniform(15, 30)
                
                # Accruals
                bonus_accrual = (gross_wages * avg_bonus_pct) / 12  # Accrue monthly
                vacation_accrual = gross_wages * 0.08  # ~4 weeks vacation = 8% of pay
                
                # Workers comp
                workers_comp = gross_wages * random.uniform(0.015, 0.035)  # 1.5-3.5% of payroll
                
                # Total compensation cost
                total_comp_cost = (gross_wages + fica_medicare + futa + suta + 
                                 health_insurance + retirement_401k_match + 
                                 life_insurance + disability_insurance + 
                                 bonus_accrual + vacation_accrual + workers_comp)
                
                records.append({
                    "record_id": f"PL-{record_id:06d}",
                    "month": month_str,
                    "month_name": month_name,
                    "department": dept,
                    "employee_count": emp_count,
                    "gross_wages": round(gross_wages, 2),
                    "fica_medicare_tax": round(fica_medicare, 2),
                    "futa_tax": round(futa, 2),
                    "suta_tax": round(suta, 2),
                    "total_payroll_taxes": round(fica_medicare + futa + suta, 2),
                    "health_insurance": round(health_insurance, 2),
                    "retirement_401k_match": round(retirement_401k_match, 2),
                    "life_insurance": round(life_insurance, 2),
                    "disability_insurance": round(disability_insurance, 2),
                    "total_benefits": round(health_insurance + retirement_401k_match + 
                                          life_insurance + disability_insurance, 2),
                    "bonus_accrual": round(bonus_accrual, 2),
                    "vacation_accrual": round(vacation_accrual, 2),
                    "workers_comp_insurance": round(workers_comp, 2),
                    "total_compensation_cost": round(total_comp_cost, 2),
                    "avg_cost_per_employee": round(total_comp_cost / emp_count, 2)
                })
                record_id += 1
        
        self._export_to_csv_json(records, self.comp_dir / "payroll_liability_ledger")
        print(f"✓ Generated {len(records)} payroll liability records")
        return records
    
    def generate_compensation_accruals(self, num_quarters=8):
        """Generate quarterly compensation accrual tracking"""
        print(f"Generating compensation accruals for {num_quarters} quarters...")
        
        accruals = []
        accrual_id = 1
        start_date = datetime.now() - timedelta(days=90*num_quarters)
        
        for quarter_offset in range(num_quarters):
            quarter_date = start_date + timedelta(days=90*quarter_offset)
            year = quarter_date.year
            quarter = ((quarter_date.month - 1) // 3) + 1
            quarter_str = f"Q{quarter} {year}"
            
            for dept in DEPARTMENTS:
                # Get department compensation data
                dept_data = next((d for d in self.hr_comp_data if d["department"] == dept), None)
                if dept_data:
                    emp_count = dept_data["employee_count"]
                    avg_salary = dept_data["avg_base_salary"]
                    avg_bonus_pct = dept_data["avg_bonus_pct"] / 100
                else:
                    emp_count = random.randint(15, 40)
                    avg_salary = 95000
                    avg_bonus_pct = 0.10
                
                # Quarterly calculations
                quarterly_wages = (emp_count * avg_salary) / 4
                
                # Accruals
                bonus_pool_accrued = quarterly_wages * avg_bonus_pct
                vacation_liability_accrued = quarterly_wages * 0.08
                sick_leave_accrued = quarterly_wages * 0.03
                merit_increase_reserve = quarterly_wages * random.uniform(0.02, 0.04)  # 2-4% annual
                
                # Actual payments (some accruals are paid out)
                bonus_paid = bonus_pool_accrued * random.uniform(0.1, 0.3) if quarter == 4 else 0
                vacation_paid = vacation_liability_accrued * random.uniform(0.6, 0.9)
                sick_leave_paid = sick_leave_accrued * random.uniform(0.3, 0.7)
                
                # Net change in accruals
                net_bonus_accrual = bonus_pool_accrued - bonus_paid
                net_vacation_accrual = vacation_liability_accrued - vacation_paid
                net_sick_accrual = sick_leave_accrued - sick_leave_paid
                
                # Severance/termination costs (occasional)
                severance_expense = 0
                if random.random() > 0.85:  # 15% chance
                    severance_expense = avg_salary * random.uniform(0.5, 2.0)  # 6mo-2yr severance
                
                total_accrued = (bonus_pool_accrued + vacation_liability_accrued + 
                               sick_leave_accrued + merit_increase_reserve + severance_expense)
                total_paid = bonus_paid + vacation_paid + sick_leave_paid
                net_change = total_accrued - total_paid
                
                accruals.append({
                    "accrual_id": f"ACC-{accrual_id:06d}",
                    "quarter": quarter_str,
                    "year": year,
                    "quarter_num": quarter,
                    "department": dept,
                    "employee_count": emp_count,
                    "quarterly_wages": round(quarterly_wages, 2),
                    # Accrued
                    "bonus_pool_accrued": round(bonus_pool_accrued, 2),
                    "vacation_liability_accrued": round(vacation_liability_accrued, 2),
                    "sick_leave_accrued": round(sick_leave_accrued, 2),
                    "merit_increase_reserve": round(merit_increase_reserve, 2),
                    "severance_expense": round(severance_expense, 2),
                    "total_accrued": round(total_accrued, 2),
                    # Paid
                    "bonus_paid": round(bonus_paid, 2),
                    "vacation_paid": round(vacation_paid, 2),
                    "sick_leave_paid": round(sick_leave_paid, 2),
                    "total_paid": round(total_paid, 2),
                    # Net
                    "net_bonus_accrual": round(net_bonus_accrual, 2),
                    "net_vacation_accrual": round(net_vacation_accrual, 2),
                    "net_sick_accrual": round(net_sick_accrual, 2),
                    "net_change_in_accruals": round(net_change, 2)
                })
                accrual_id += 1
        
        self._export_to_csv_json(accruals, self.comp_dir / "compensation_accruals")
        print(f"✓ Generated {len(accruals)} compensation accrual records")
        return accruals
    
    def generate_benefits_liability_schedule(self):
        """Generate benefits liability and cost schedule"""
        print("Generating benefits liability schedule...")
        
        benefits = []
        benefit_id = 1
        
        benefit_types = [
            {
                "type": "Health Insurance",
                "category": "Medical",
                "monthly_employer_cost_per_ee": 550,
                "monthly_employee_contribution": 150,
                "eligible_employees_pct": 0.95,
                "participation_rate": 0.88
            },
            {
                "type": "Dental Insurance",
                "category": "Medical",
                "monthly_employer_cost_per_ee": 45,
                "monthly_employee_contribution": 15,
                "eligible_employees_pct": 0.95,
                "participation_rate": 0.82
            },
            {
                "type": "Vision Insurance",
                "category": "Medical",
                "monthly_employer_cost_per_ee": 18,
                "monthly_employee_contribution": 8,
                "eligible_employees_pct": 0.95,
                "participation_rate": 0.75
            },
            {
                "type": "401(k) Employer Match",
                "category": "Retirement",
                "monthly_employer_cost_per_ee": 350,  # ~4% of salary
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 1.0,
                "participation_rate": 0.78
            },
            {
                "type": "Life Insurance",
                "category": "Insurance",
                "monthly_employer_cost_per_ee": 35,
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 1.0,
                "participation_rate": 1.0
            },
            {
                "type": "Short-Term Disability",
                "category": "Insurance",
                "monthly_employer_cost_per_ee": 22,
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 1.0,
                "participation_rate": 1.0
            },
            {
                "type": "Long-Term Disability",
                "category": "Insurance",
                "monthly_employer_cost_per_ee": 28,
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 1.0,
                "participation_rate": 1.0
            },
            {
                "type": "Flexible Spending Account (FSA)",
                "category": "Wellness",
                "monthly_employer_cost_per_ee": 5,  # Admin fees
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 0.95,
                "participation_rate": 0.45
            },
            {
                "type": "Employee Assistance Program (EAP)",
                "category": "Wellness",
                "monthly_employer_cost_per_ee": 8,
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 1.0,
                "participation_rate": 1.0
            },
            {
                "type": "Tuition Reimbursement",
                "category": "Development",
                "monthly_employer_cost_per_ee": 85,  # Annual $5k divided by participating employees
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 0.80,
                "participation_rate": 0.12
            },
            {
                "type": "Commuter Benefits",
                "category": "Wellness",
                "monthly_employer_cost_per_ee": 75,
                "monthly_employee_contribution": 0,
                "eligible_employees_pct": 0.70,
                "participation_rate": 0.35
            },
            {
                "type": "Gym Membership Subsidy",
                "category": "Wellness",
                "monthly_employer_cost_per_ee": 50,
                "monthly_employee_contribution": 25,
                "eligible_employees_pct": 1.0,
                "participation_rate": 0.42
            }
        ]
        
        for benefit in benefit_types:
            eligible_count = int(self.total_employees * benefit["eligible_employees_pct"])
            participating_count = int(eligible_count * benefit["participation_rate"])
            
            monthly_employer_cost = benefit["monthly_employer_cost_per_ee"] * participating_count
            monthly_employee_cost = benefit["monthly_employee_contribution"] * participating_count
            annual_employer_cost = monthly_employer_cost * 12
            annual_employee_cost = monthly_employee_cost * 12
            
            # Accrued but unpaid liability (usually 1-2 months)
            accrued_liability = monthly_employer_cost * random.uniform(1.0, 2.0)
            
            benefits.append({
                "benefit_id": f"BEN-{benefit_id:03d}",
                "benefit_type": benefit["type"],
                "category": benefit["category"],
                "eligible_employees": eligible_count,
                "participating_employees": participating_count,
                "participation_rate": round(benefit["participation_rate"] * 100, 1),
                "monthly_cost_per_employee": benefit["monthly_employer_cost_per_ee"],
                "monthly_employer_cost": round(monthly_employer_cost, 2),
                "monthly_employee_contribution": round(monthly_employee_cost, 2),
                "annual_employer_cost": round(annual_employer_cost, 2),
                "annual_employee_contribution": round(annual_employee_cost, 2),
                "total_annual_cost": round(annual_employer_cost + annual_employee_cost, 2),
                "accrued_liability": round(accrued_liability, 2),
                "vendor": self._get_benefit_vendor(benefit["type"]),
                "payment_frequency": "Monthly",
                "renewal_month": random.choice(["January", "July"]),
                "status": "Active"
            })
            benefit_id += 1
        
        # Add summary row
        total_monthly_cost = sum(b["monthly_employer_cost"] for b in benefits)
        total_annual_cost = sum(b["annual_employer_cost"] for b in benefits)
        total_liability = sum(b["accrued_liability"] for b in benefits)
        
        benefits.append({
            "benefit_id": "SUMMARY",
            "benefit_type": "Total All Benefits",
            "category": "Summary",
            "eligible_employees": self.total_employees,
            "participating_employees": self.total_employees,
            "participation_rate": 100.0,
            "monthly_cost_per_employee": round(total_monthly_cost / self.total_employees, 2),
            "monthly_employer_cost": round(total_monthly_cost, 2),
            "monthly_employee_contribution": 0,
            "annual_employer_cost": round(total_annual_cost, 2),
            "annual_employee_contribution": 0,
            "total_annual_cost": round(total_annual_cost, 2),
            "accrued_liability": round(total_liability, 2),
            "vendor": "Multiple",
            "payment_frequency": "Various",
            "renewal_month": "Various",
            "status": "Summary"
        })
        
        self._export_to_csv_json(benefits, self.comp_dir / "benefits_liability_schedule")
        print(f"✓ Generated {len(benefits)} benefit records")
        return benefits
    
    def generate_payroll_tax_schedule(self, num_quarters=8):
        """Generate payroll tax liability and payment schedule"""
        print(f"Generating payroll tax schedule for {num_quarters} quarters...")
        
        tax_records = []
        tax_id = 1
        start_date = datetime.now() - timedelta(days=90*num_quarters)
        
        for quarter_offset in range(num_quarters):
            quarter_date = start_date + timedelta(days=90*quarter_offset)
            year = quarter_date.year
            quarter = ((quarter_date.month - 1) // 3) + 1
            quarter_str = f"Q{quarter} {year}"
            
            # Calculate quarterly payroll
            quarterly_gross_payroll = (self.total_annual_payroll / 4) * random.uniform(0.95, 1.05)
            
            # Federal taxes
            federal_income_tax_withheld = quarterly_gross_payroll * random.uniform(0.18, 0.22)
            social_security_employer = quarterly_gross_payroll * 0.062  # 6.2%
            social_security_employee = quarterly_gross_payroll * 0.062
            medicare_employer = quarterly_gross_payroll * 0.0145  # 1.45%
            medicare_employee = quarterly_gross_payroll * 0.0145
            additional_medicare = quarterly_gross_payroll * 0.009 * 0.25  # 0.9% on wages > $200k
            futa = quarterly_gross_payroll * 0.006  # 0.6% on first $7k per employee
            
            # State taxes (Washington state - no income tax, but has other taxes)
            suta = quarterly_gross_payroll * 0.027  # State unemployment ~2.7%
            workers_comp = quarterly_gross_payroll * random.uniform(0.02, 0.04)
            
            # Totals
            total_employer_taxes = (social_security_employer + medicare_employer + 
                                   futa + suta + workers_comp)
            total_employee_withholdings = (federal_income_tax_withheld + 
                                          social_security_employee + 
                                          medicare_employee + additional_medicare)
            total_tax_liability = total_employer_taxes + total_employee_withholdings
            
            # Payment dates
            payment_date = quarter_date + timedelta(days=random.randint(95, 105))
            
            tax_records.append({
                "tax_id": f"TAX-{tax_id:06d}",
                "quarter": quarter_str,
                "year": year,
                "quarter_num": quarter,
                "gross_payroll": round(quarterly_gross_payroll, 2),
                # Federal withholdings
                "federal_income_tax_withheld": round(federal_income_tax_withheld, 2),
                # FICA - Employer portion
                "social_security_employer": round(social_security_employer, 2),
                "medicare_employer": round(medicare_employer, 2),
                # FICA - Employee portion (withheld)
                "social_security_employee": round(social_security_employee, 2),
                "medicare_employee": round(medicare_employee, 2),
                "additional_medicare_tax": round(additional_medicare, 2),
                # Federal unemployment
                "futa_tax": round(futa, 2),
                # State taxes
                "suta_tax": round(suta, 2),
                "workers_comp_tax": round(workers_comp, 2),
                # Totals
                "total_employer_taxes": round(total_employer_taxes, 2),
                "total_employee_withholdings": round(total_employee_withholdings, 2),
                "total_tax_liability": round(total_tax_liability, 2),
                "payment_due_date": payment_date.strftime("%Y-%m-%d"),
                "payment_status": "Paid" if quarter_offset < num_quarters - 1 else "Pending",
                "filing_form": "Form 941" if quarter < 4 else "Form 941 + 940"
            })
            tax_id += 1
        
        self._export_to_csv_json(tax_records, self.comp_dir / "payroll_tax_schedule")
        print(f"✓ Generated {len(tax_records)} payroll tax records")
        return tax_records
    
    def generate_stock_compensation_schedule(self):
        """Generate equity/stock compensation schedule (if applicable)"""
        print("Generating stock compensation schedule...")
        
        # For a private company, this might be stock options or restricted stock
        grants = []
        grant_id = 1
        
        # Executive and senior leadership typically get equity
        exec_employees = [
            {"name": "Sarah Chen", "title": "CEO", "dept": "Executive Leadership"},
            {"name": "Michael Rodriguez", "title": "CFO", "dept": "Executive Leadership"},
            {"name": "Jennifer Park", "title": "VP HR", "dept": "Human Resources"},
            {"name": "David Martinez", "title": "VP Sales", "dept": "Sales & Marketing"},
            {"name": "Emily Thompson", "title": "VP Product", "dept": "Product Development"},
        ]
        
        # Plus some other senior staff
        num_other_grants = 25
        
        grant_types = ["Stock Options", "Restricted Stock Units (RSUs)", "Performance Shares"]
        
        for emp in exec_employees:
            grant_date = datetime.now() - timedelta(days=random.randint(180, 1800))
            vesting_start = grant_date + timedelta(days=365)  # 1-year cliff
            vesting_end = vesting_start + timedelta(days=3*365)  # 4-year total
            
            # Executive grants
            shares_granted = random.randint(15000, 50000)
            strike_price = random.uniform(5.00, 15.00)
            fair_value_at_grant = strike_price * random.uniform(1.1, 1.5)
            current_fair_value = fair_value_at_grant * random.uniform(1.2, 2.5)
            
            months_since_grant = (datetime.now() - grant_date).days / 30
            vesting_months = 48
            vested_shares = int(shares_granted * min(max(months_since_grant - 12, 0) / 36, 1.0))
            unvested_shares = shares_granted - vested_shares
            
            # Expense recognition (straight-line over vesting period)
            total_grant_value = shares_granted * fair_value_at_grant
            monthly_expense = total_grant_value / vesting_months
            total_expense_recognized = monthly_expense * min(months_since_grant, vesting_months)
            remaining_expense = max(total_grant_value - total_expense_recognized, 0)
            
            grants.append({
                "grant_id": f"EQT-{grant_id:05d}",
                "employee_name": emp["name"],
                "title": emp["title"],
                "department": emp["dept"],
                "grant_type": random.choice(grant_types),
                "grant_date": grant_date.strftime("%Y-%m-%d"),
                "vesting_start_date": vesting_start.strftime("%Y-%m-%d"),
                "vesting_end_date": vesting_end.strftime("%Y-%m-%d"),
                "vesting_schedule": "25% after 1yr, then monthly over 3yrs",
                "shares_granted": shares_granted,
                "strike_price": round(strike_price, 2),
                "fair_value_at_grant": round(fair_value_at_grant, 2),
                "current_fair_value": round(current_fair_value, 2),
                "vested_shares": vested_shares,
                "unvested_shares": unvested_shares,
                "exercised_shares": 0,
                "total_grant_value": round(total_grant_value, 2),
                "expense_recognized_to_date": round(total_expense_recognized, 2),
                "remaining_expense_to_recognize": round(remaining_expense, 2),
                "current_intrinsic_value": round((current_fair_value - strike_price) * vested_shares, 2),
                "status": "Active"
            })
            grant_id += 1
        
        # Add grants for other senior employees
        for i in range(num_other_grants):
            grant_date = datetime.now() - timedelta(days=random.randint(180, 1800))
            vesting_start = grant_date + timedelta(days=365)
            vesting_end = vesting_start + timedelta(days=3*365)
            
            shares_granted = random.randint(1000, 10000)
            strike_price = random.uniform(5.00, 15.00)
            fair_value_at_grant = strike_price * random.uniform(1.1, 1.5)
            current_fair_value = fair_value_at_grant * random.uniform(1.2, 2.5)
            
            months_since_grant = (datetime.now() - grant_date).days / 30
            vesting_months = 48
            vested_shares = int(shares_granted * min(max(months_since_grant - 12, 0) / 36, 1.0))
            unvested_shares = shares_granted - vested_shares
            
            total_grant_value = shares_granted * fair_value_at_grant
            monthly_expense = total_grant_value / vesting_months
            total_expense_recognized = monthly_expense * min(months_since_grant, vesting_months)
            remaining_expense = max(total_grant_value - total_expense_recognized, 0)
            
            grants.append({
                "grant_id": f"EQT-{grant_id:05d}",
                "employee_name": f"Employee {i+6}",
                "title": random.choice(["Director", "Senior Manager", "Principal Engineer"]),
                "department": random.choice(DEPARTMENTS),
                "grant_type": random.choice(grant_types),
                "grant_date": grant_date.strftime("%Y-%m-%d"),
                "vesting_start_date": vesting_start.strftime("%Y-%m-%d"),
                "vesting_end_date": vesting_end.strftime("%Y-%m-%d"),
                "vesting_schedule": "25% after 1yr, then monthly over 3yrs",
                "shares_granted": shares_granted,
                "strike_price": round(strike_price, 2),
                "fair_value_at_grant": round(fair_value_at_grant, 2),
                "current_fair_value": round(current_fair_value, 2),
                "vested_shares": vested_shares,
                "unvested_shares": unvested_shares,
                "exercised_shares": 0,
                "total_grant_value": round(total_grant_value, 2),
                "expense_recognized_to_date": round(total_expense_recognized, 2),
                "remaining_expense_to_recognize": round(remaining_expense, 2),
                "current_intrinsic_value": round((current_fair_value - strike_price) * vested_shares, 2),
                "status": "Active"
            })
            grant_id += 1
        
        self._export_to_csv_json(grants, self.comp_dir / "stock_compensation_schedule")
        print(f"✓ Generated {len(grants)} stock compensation grants")
        return grants
    
    def generate_workers_comp_claims(self, num_years=3):
        """Generate workers compensation claims and costs"""
        print(f"Generating workers comp claims for {num_years} years...")
        
        claims = []
        claim_id = 1
        start_date = datetime.now() - timedelta(days=365*num_years)
        
        injury_types = [
            {"type": "Repetitive Strain Injury", "severity": "Minor", "avg_cost": 3500},
            {"type": "Slip and Fall", "severity": "Moderate", "avg_cost": 8500},
            {"type": "Equipment Injury", "severity": "Moderate", "avg_cost": 12000},
            {"type": "Lifting Injury", "severity": "Moderate", "avg_cost": 9500},
            {"type": "Laceration", "severity": "Minor", "avg_cost": 2500},
            {"type": "Fracture", "severity": "Serious", "avg_cost": 25000},
            {"type": "Crush Injury", "severity": "Serious", "avg_cost": 45000},
            {"type": "Chemical Exposure", "severity": "Moderate", "avg_cost": 15000},
        ]
        
        # Generate 2-5 claims per quarter
        num_quarters = num_years * 4
        
        for quarter_idx in range(num_quarters):
            num_claims_this_quarter = random.randint(2, 5)
            
            for _ in range(num_claims_this_quarter):
                incident_date = start_date + timedelta(days=90*quarter_idx + random.randint(0, 89))
                injury = random.choice(injury_types)
                
                # Claim details
                medical_costs = injury["avg_cost"] * random.uniform(0.7, 1.3)
                lost_wages = random.uniform(2000, 15000) if injury["severity"] != "Minor" else 0
                rehabilitation_costs = random.uniform(1000, 5000) if injury["severity"] == "Serious" else 0
                admin_costs = 500
                
                total_cost = medical_costs + lost_wages + rehabilitation_costs + admin_costs
                
                # Days away from work
                if injury["severity"] == "Minor":
                    days_away = random.randint(0, 3)
                elif injury["severity"] == "Moderate":
                    days_away = random.randint(3, 21)
                else:
                    days_away = random.randint(21, 120)
                
                # Claim status
                days_since_incident = (datetime.now() - incident_date).days
                if days_since_incident > 180:
                    status = random.choice(["Closed", "Closed", "Closed", "Settled"])
                else:
                    status = random.choice(["Open", "Under Review"])
                
                claims.append({
                    "claim_id": f"WC-{claim_id:05d}",
                    "incident_date": incident_date.strftime("%Y-%m-%d"),
                    "report_date": (incident_date + timedelta(days=random.randint(0, 2))).strftime("%Y-%m-%d"),
                    "employee_dept": random.choice(DEPARTMENTS),
                    "injury_type": injury["type"],
                    "severity": injury["severity"],
                    "body_part": random.choice(["Hand/Wrist", "Back", "Shoulder", "Knee", "Foot/Ankle", "Head"]),
                    "days_away_from_work": days_away,
                    "medical_costs": round(medical_costs, 2),
                    "lost_wages_paid": round(lost_wages, 2),
                    "rehabilitation_costs": round(rehabilitation_costs, 2),
                    "administrative_costs": round(admin_costs, 2),
                    "total_claim_cost": round(total_cost, 2),
                    "reserve_amount": round(total_cost * 1.1, 2) if status == "Open" else 0,
                    "claim_status": status,
                    "incident_description": f"{injury['type']} while performing work duties",
                    "return_to_work_date": (incident_date + timedelta(days=days_away)).strftime("%Y-%m-%d") if days_away > 0 else "",
                    "restrictions": "Light duty" if days_away > 7 else "None"
                })
                claim_id += 1
        
        self._export_to_csv_json(claims, self.comp_dir / "workers_comp_claims")
        print(f"✓ Generated {len(claims)} workers comp claims")
        return claims
    
    def generate_compensation_summary_memo(self):
        """Generate a financial summary memo about compensation"""
        print("Generating compensation financial summary memo...")
        
        if not self.use_ai:
            print("⚠️  AI not available, skipping memo generation")
            return None
        
        # Calculate summary statistics
        total_annual_payroll = self.total_employees * self.avg_salary
        total_payroll_taxes = total_annual_payroll * 0.11  # ~11% employer payroll taxes
        total_benefits = self.total_employees * 12 * 1100  # ~$1,100/mo per employee
        total_comp_cost = total_annual_payroll + total_payroll_taxes + total_benefits
        
        prompt = f"""Generate a concise financial memo (300-400 words) analyzing Robotix's compensation costs and liabilities.

Company Context:
- Total Employees: {self.total_employees}
- Annual Payroll: ${total_annual_payroll:,.0f}
- Annual Payroll Taxes: ${total_payroll_taxes:,.0f}
- Annual Benefits Costs: ${total_benefits:,.0f}
- Total Compensation Cost: ${total_comp_cost:,.0f}

The memo should cover:
1. Overview of total compensation costs as a percentage of revenue (~42M)
2. Key liability balances (accrued wages, bonuses, benefits, taxes)
3. Trends and risks
4. Recommendations for finance team

Format as a professional memo with:
- TO: CFO Michael Rodriguez
- FROM: Finance Team
- DATE: {datetime.now().strftime('%B %d, %Y')}
- RE: Compensation Costs and Liabilities Analysis

Use markdown formatting. Be specific with numbers but keep it concise."""

        try:
            response = self.llm.invoke(prompt)
            memo_content = response.content
            
            # Save memo
            memo_path = self.comp_dir / "compensation_financial_analysis.md"
            with open(memo_path, 'w') as f:
                f.write(memo_content)
            
            print(f"✓ Generated compensation financial analysis memo")
            return memo_content
        except Exception as e:
            print(f"⚠️  Error generating memo: {e}")
            return None
    
    def _get_benefit_vendor(self, benefit_type):
        """Map benefit types to vendors"""
        vendor_map = {
            "Health Insurance": "Premera Blue Cross",
            "Dental Insurance": "Delta Dental",
            "Vision Insurance": "VSP Vision Care",
            "401(k) Employer Match": "Fidelity Investments",
            "Life Insurance": "MetLife",
            "Short-Term Disability": "MetLife",
            "Long-Term Disability": "MetLife",
            "Flexible Spending Account (FSA)": "WageWorks",
            "Employee Assistance Program (EAP)": "ComPsych",
            "Tuition Reimbursement": "Internal",
            "Commuter Benefits": "WageWorks",
            "Gym Membership Subsidy": "Various Providers"
        }
        return vendor_map.get(benefit_type, "Various")
    
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
    print("=" * 70)
    print("Finance Compensation Data Generator")
    print("=" * 70)
    
    generator = FinanceCompensationGenerator()
    
    # Generate all compensation data (doubled parameters)
    generator.generate_payroll_liability_ledger(num_months=48)
    generator.generate_compensation_accruals(num_quarters=16)
    generator.generate_benefits_liability_schedule()
    generator.generate_payroll_tax_schedule(num_quarters=16)
    generator.generate_stock_compensation_schedule()
    generator.generate_workers_comp_claims(num_years=6)
    generator.generate_compensation_summary_memo()
    
    print("\n" + "=" * 70)
    print("✓ Finance compensation data generation complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()

