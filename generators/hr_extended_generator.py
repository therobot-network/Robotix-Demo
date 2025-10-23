#!/usr/bin/env python3
"""
HR Extended Data Generator
Generates: historical headcount, attrition, hiring/recruiting, training, diversity
"""

import json
import csv
import random
import os
from datetime import datetime, timedelta
from pathlib import Path
import sys
from dotenv import load_dotenv

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


class HRExtendedGenerator:
    
    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = Path(data_dir)
        self.hr_dir = self.data_dir / "hr-legal" / "hr"
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
        (self.hr_dir / "headcount").mkdir(parents=True, exist_ok=True)
        (self.hr_dir / "attrition").mkdir(parents=True, exist_ok=True)
        (self.hr_dir / "recruiting").mkdir(parents=True, exist_ok=True)
        (self.hr_dir / "training").mkdir(parents=True, exist_ok=True)
        (self.hr_dir / "diversity").mkdir(parents=True, exist_ok=True)
        
        self.job_levels = ["Entry", "Mid", "Senior", "Lead", "Manager", "Director", "VP", "Executive"]
        self.training_types = [
            "Technical Skills", "Leadership Development", "Compliance Training",
            "Safety Training", "Software Tools", "Communication Skills",
            "Project Management", "Industry Certification", "Onboarding"
        ]
    
    def _generate_ai_content(self, content_type, context, word_count="60-100"):
        """Generate content using AI"""
        if not self.use_ai:
            return "AI generation not available."
        
        try:
            prompt = f"""Generate realistic {content_type} for Robotix HR.

Context:
{context}

Requirements:
- Professional HR tone
- Specific and realistic
- {word_count} words
- Plain text only

Generate:"""

            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            return f"{content_type} content"
        
    def generate_historical_headcount(self, num_months=36):
        """Generate monthly headcount history by department"""
        print(f"Generating historical headcount for {num_months} months...")
        
        headcount_records = []
        start_date = datetime.now() - timedelta(days=30*num_months)
        
        # Starting headcount by department (3 years ago) - use actual DEPARTMENTS
        dept_headcount = {}
        for dept in DEPARTMENTS:
            # Assign realistic headcount based on department
            if "Executive" in dept:
                dept_headcount[dept] = 5
            elif "Human Resources" in dept or "HR" in dept:
                dept_headcount[dept] = 8
            elif "Sales" in dept or "Marketing" in dept:
                dept_headcount[dept] = 35
            elif "Product" in dept or "Development" in dept or "Engineering" in dept:
                dept_headcount[dept] = 55
            elif "Manufacturing" in dept or "Operations" in dept:
                dept_headcount[dept] = 45
            elif "Finance" in dept or "Accounting" in dept:
                dept_headcount[dept] = 12
            elif "Customer" in dept or "Support" in dept or "Service" in dept:
                dept_headcount[dept] = 25
            elif "Quality" in dept:
                dept_headcount[dept] = 18
            else:
                dept_headcount[dept] = 15
        
        for month_offset in range(num_months):
            month_date = start_date + timedelta(days=30*month_offset)
            month_str = month_date.strftime("%Y-%m")
            
            for dept in DEPARTMENTS:
                # Simulate growth/changes over time
                change = 0
                if random.random() > 0.7:  # 30% chance of change each month
                    change = random.choice([-1, -1, 0, 1, 1, 2])  # Slight bias toward growth
                
                dept_headcount[dept] = max(1, dept_headcount[dept] + change)
                
                # Calculate FTE (some part-time)
                fte = dept_headcount[dept] * random.uniform(0.95, 1.0)
                
                headcount_records.append({
                    "month": month_str,
                    "department": dept,
                    "headcount": dept_headcount[dept],
                    "fte": round(fte, 2),
                    "contractors": random.randint(0, 3) if dept in ["Engineering", "Operations"] else 0,
                    "month_change": change,
                    "month_change_pct": round((change / (dept_headcount[dept] - change) * 100), 2) if (dept_headcount[dept] - change) > 0 else 0
                })
        
        self._export_to_csv_json(headcount_records, self.hr_dir / "headcount" / "historical_headcount")
        print(f"✓ Generated {len(headcount_records)} headcount records")
        return headcount_records
    
    def generate_attrition_records(self, num_records=80):
        """Generate employee attrition/turnover records"""
        print(f"Generating {num_records} attrition records...")
        
        attrition_records = []
        
        termination_reasons = [
            "Voluntary - Better Opportunity",
            "Voluntary - Relocation",
            "Voluntary - Career Change",
            "Voluntary - Retirement",
            "Voluntary - Personal Reasons",
            "Involuntary - Performance",
            "Involuntary - Restructuring",
            "Involuntary - Position Eliminated",
            "End of Contract"
        ]
        
        for i in range(num_records):
            hire_date = datetime.now() - timedelta(days=random.randint(90, 2190))  # 3 months to 6 years
            term_date = hire_date + timedelta(days=random.randint(90, 1825))
            
            if term_date > datetime.now():
                term_date = datetime.now() - timedelta(days=random.randint(1, 180))
            
            tenure_days = (term_date - hire_date).days
            dept = random.choice(DEPARTMENTS)
            
            # Voluntary vs involuntary affects patterns
            reason = random.choice(termination_reasons)
            is_voluntary = "Voluntary" in reason
            is_regrettable = is_voluntary and random.random() > 0.4  # 60% of voluntary are regrettable
            
            attrition_records.append({
                "attrition_id": f"ATR-{i+1:05d}",
                "employee_id": f"EMP{random.randint(1000, 9999)}",
                "department": dept,
                "job_level": random.choice(self.job_levels),
                "hire_date": hire_date.strftime("%Y-%m-%d"),
                "termination_date": term_date.strftime("%Y-%m-%d"),
                "tenure_months": round(tenure_days / 30, 1),
                "termination_type": "Voluntary" if is_voluntary else "Involuntary",
                "termination_reason": reason,
                "regrettable": "Yes" if is_regrettable else "No",
                "exit_interview_completed": "Yes" if is_voluntary and random.random() > 0.2 else "No",
                "eligible_for_rehire": "Yes" if (is_voluntary or "Contract" in reason) else "No",
                "notice_period_days": random.choice([0, 14, 30]) if is_voluntary else 0,
                "quarter": f"Q{((term_date.month-1)//3)+1} {term_date.year}"
            })
        
        self._export_to_csv_json(attrition_records, self.hr_dir / "attrition" / "attrition_records")
        print(f"✓ Generated {len(attrition_records)} attrition records")
        return attrition_records
    
    def generate_recruiting_pipeline(self, num_records=120):
        """Generate recruiting pipeline and open positions"""
        print(f"Generating {num_records} recruiting records...")
        
        recruiting_records = []
        
        job_titles = [
            "Software Engineer", "Senior Software Engineer", "Robotics Engineer",
            "Sales Representative", "Account Executive", "Sales Manager",
            "Marketing Specialist", "Marketing Manager", "Content Writer",
            "Operations Manager", "Production Supervisor", "Quality Engineer",
            "Financial Analyst", "Accountant", "HR Coordinator",
            "Customer Support Specialist", "Technical Support Engineer"
        ]
        
        stages = ["Sourcing", "Screening", "Phone Interview", "Technical Interview", 
                 "Final Interview", "Offer", "Accepted", "Rejected", "Withdrawn"]
        
        for i in range(num_records):
            posted_date = datetime.now() - timedelta(days=random.randint(1, 180))
            current_stage = random.choice(stages)
            
            # Calculate days in process
            if current_stage == "Accepted":
                days_to_hire = random.randint(30, 90)
            elif current_stage in ["Rejected", "Withdrawn"]:
                days_to_hire = random.randint(7, 60)
            else:
                days_to_hire = (datetime.now() - posted_date).days
            
            num_applicants = random.randint(15, 150)
            num_screened = int(num_applicants * random.uniform(0.3, 0.6))
            num_interviewed = int(num_screened * random.uniform(0.2, 0.5))
            
            recruiting_records.append({
                "req_id": f"REQ-{i+1:05d}",
                "job_title": random.choice(job_titles),
                "department": random.choice(DEPARTMENTS),
                "job_level": random.choice(self.job_levels),
                "posted_date": posted_date.strftime("%Y-%m-%d"),
                "status": "Closed" if current_stage in ["Accepted", "Rejected", "Withdrawn"] else "Open",
                "current_stage": current_stage,
                "num_applicants": num_applicants,
                "num_screened": num_screened,
                "num_phone_interviews": num_interviewed,
                "num_onsite_interviews": int(num_interviewed * 0.6),
                "num_offers": 1 if current_stage in ["Offer", "Accepted"] else 0,
                "days_to_hire": days_to_hire if current_stage == "Accepted" else None,
                "days_open": (datetime.now() - posted_date).days,
                "source": random.choice(["LinkedIn", "Indeed", "Referral", "Company Website", "Recruiter", "Career Fair"]),
                "hiring_manager": random.choice([e["name"] for e in EMPLOYEES if "Human Resources" in e["dept"] or "HR" in e["dept"] or "Manager" in e["title"]])[:20],
                "priority": random.choice(["High", "Medium", "Low"])
            })
        
        self._export_to_csv_json(recruiting_records, self.hr_dir / "recruiting" / "recruiting_pipeline")
        print(f"✓ Generated {len(recruiting_records)} recruiting records")
        return recruiting_records
    
    def generate_training_records(self, num_records=300):
        """Generate employee training records"""
        print(f"Generating {num_records} training records...")
        
        training_records = []
        
        training_courses = {
            "Technical Skills": ["Advanced Python", "Robot Programming", "CAD Design", "PLC Programming", "Data Analysis"],
            "Leadership Development": ["Manager Training 101", "Executive Leadership", "Team Building", "Conflict Resolution"],
            "Compliance Training": ["OSHA Safety", "Anti-Harassment", "Data Privacy", "Ethics Training"],
            "Safety Training": ["Equipment Safety", "First Aid/CPR", "Emergency Procedures", "Hazmat Handling"],
            "Software Tools": ["Salesforce Basics", "Excel Advanced", "Project Management Software", "ERP Training"],
            "Communication Skills": ["Presentation Skills", "Technical Writing", "Customer Communication"],
            "Project Management": ["Agile Methodology", "PMP Certification Prep", "Scrum Master Training"],
            "Industry Certification": ["Robotics Certification", "Quality Management", "Six Sigma Green Belt"]
        }
        
        for i in range(num_records):
            training_type = random.choice(self.training_types)
            course_name = random.choice(training_courses.get(training_type, ["General Training"]))
            
            training_date = datetime.now() - timedelta(days=random.randint(1, 730))
            duration_hours = random.choice([2, 4, 8, 16, 24, 40])
            cost = duration_hours * random.uniform(50, 200)
            
            completed = random.random() > 0.15  # 85% completion rate
            
            training_records.append({
                "training_id": f"TRN-{i+1:06d}",
                "employee_name": random.choice(EMPLOYEES)["name"],
                "course_name": course_name,
                "training_type": training_type,
                "training_date": training_date.strftime("%Y-%m-%d"),
                "duration_hours": duration_hours,
                "cost": round(cost, 2),
                "provider": random.choice(["Internal", "LinkedIn Learning", "Coursera", "Industry Association", "External Vendor"]),
                "delivery_method": random.choice(["In-Person", "Virtual", "Self-Paced Online", "Hybrid"]),
                "status": "Completed" if completed else random.choice(["In Progress", "Scheduled"]),
                "completion_date": (training_date + timedelta(days=duration_hours)).strftime("%Y-%m-%d") if completed else None,
                "score": round(random.uniform(70, 100), 1) if completed else None,
                "certification_earned": "Yes" if completed and random.random() > 0.7 else "No",
                "mandatory": "Yes" if training_type == "Compliance Training" else "No"
            })
        
        self._export_to_csv_json(training_records, self.hr_dir / "training" / "training_records")
        print(f"✓ Generated {len(training_records)} training records")
        return training_records
    
    def generate_diversity_records(self):
        """Generate diversity and demographic data"""
        print("Generating diversity records...")
        
        # Current snapshot
        diversity_current = []
        
        gender_dist = {"Male": 0.62, "Female": 0.36, "Non-binary": 0.02}
        ethnicity_dist = {
            "White": 0.58,
            "Asian": 0.22,
            "Hispanic/Latino": 0.11,
            "Black/African American": 0.06,
            "Other": 0.03
        }
        
        for dept in DEPARTMENTS:
            dept_size = random.randint(8, 55)
            
            for gender, pct in gender_dist.items():
                count = int(dept_size * pct * random.uniform(0.8, 1.2))
                
                diversity_current.append({
                    "department": dept,
                    "job_level_category": random.choice(["Individual Contributor", "Manager", "Executive"]),
                    "gender": gender,
                    "count": count,
                    "percentage": round((count / dept_size) * 100, 1)
                })
        
        self._export_to_csv_json(diversity_current, self.hr_dir / "diversity" / "diversity_current")
        
        # Historical diversity trends
        diversity_trends = []
        start_date = datetime.now() - timedelta(days=365*3)  # 3 years
        
        for quarter_offset in range(12):  # 12 quarters
            quarter_date = start_date + timedelta(days=91*quarter_offset)
            quarter_str = f"Q{((quarter_date.month-1)//3)+1} {quarter_date.year}"
            
            total_employees = random.randint(220, 290)
            
            diversity_trends.append({
                "quarter": quarter_str,
                "total_employees": total_employees,
                "female_pct": round(random.uniform(34, 38), 1),
                "male_pct": round(random.uniform(60, 64), 1),
                "underrepresented_minority_pct": round(random.uniform(18, 24), 1),
                "veterans_pct": round(random.uniform(3, 6), 1),
                "employees_with_disabilities_pct": round(random.uniform(2, 4), 1),
                "female_leadership_pct": round(random.uniform(28, 35), 1),
                "minority_leadership_pct": round(random.uniform(15, 22), 1)
            })
        
        self._export_to_csv_json(diversity_trends, self.hr_dir / "diversity" / "diversity_trends")
        print(f"✓ Generated diversity records")
        return diversity_current, diversity_trends
    
    def generate_compensation_analysis(self):
        """Generate compensation analysis by level and department"""
        print("Generating compensation analysis...")
        
        comp_records = []
        
        base_salaries = {
            "Entry": 65000,
            "Mid": 85000,
            "Senior": 110000,
            "Lead": 135000,
            "Manager": 125000,
            "Director": 165000,
            "VP": 210000,
            "Executive": 280000
        }
        
        for dept in DEPARTMENTS:
            for level in self.job_levels:
                count = random.randint(2, 15)
                base = base_salaries[level]
                
                # Department multipliers
                dept_mult = 1.0
                if dept == "Engineering":
                    dept_mult = 1.15
                elif dept == "Sales":
                    dept_mult = 1.10
                elif dept == "Executive":
                    dept_mult = 1.25
                
                avg_salary = base * dept_mult * random.uniform(0.95, 1.05)
                min_salary = avg_salary * 0.85
                max_salary = avg_salary * 1.20
                
                comp_records.append({
                    "department": dept,
                    "job_level": level,
                    "employee_count": count,
                    "avg_base_salary": round(avg_salary, 2),
                    "min_salary": round(min_salary, 2),
                    "max_salary": round(max_salary, 2),
                    "median_salary": round(avg_salary * random.uniform(0.98, 1.02), 2),
                    "avg_bonus_pct": round(random.uniform(5, 20), 1),
                    "avg_total_comp": round(avg_salary * random.uniform(1.08, 1.22), 2),
                    "market_percentile": random.choice([40, 50, 55, 60, 65])
                })
        
        self._export_to_csv_json(comp_records, self.hr_dir / "compensation_analysis")
        print(f"✓ Generated {len(comp_records)} compensation records")
        return comp_records
    
    def _export_to_csv_json(self, data, base_filename):
        """Export data to both CSV and JSON formats"""
        if not data:
            return
        
        csv_path = f"{base_filename}.csv"
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        json_path = f"{base_filename}.json"
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)


def main():
    print("=" * 60)
    print("HR Extended Data Generator")
    print("=" * 60)
    
    generator = HRExtendedGenerator()
    
    generator.generate_historical_headcount(num_months=36)
    generator.generate_attrition_records(num_records=80)
    generator.generate_recruiting_pipeline(num_records=120)
    generator.generate_training_records(num_records=300)
    generator.generate_diversity_records()
    generator.generate_compensation_analysis()
    
    print("\n" + "=" * 60)
    print("✓ HR extended data generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

