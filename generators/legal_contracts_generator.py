#!/usr/bin/env python3
"""
Legal & Contracts Data Generator
Generates: contracts, litigation, compliance, risk assessments
Uses AI for legal language and terms
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
from company_data import EMPLOYEES, get_random_date, format_date

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
    print("⚠️  LangChain not installed. Run: pip install langchain langchain-anthropic")


class LegalContractsGenerator:
    
    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = Path(data_dir)
        self.legal_dir = self.data_dir / "hr-legal" / "legal"
        self.use_ai = use_ai and AI_AVAILABLE
        
        # Initialize AI model if available
        if self.use_ai:
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key:
                self.llm = ChatAnthropic(
                    model="claude-3-5-sonnet-20241022",
                    temperature=0.7,
                    max_tokens=4000
                )
                print("✅ AI content generation enabled (Claude 3.5 Sonnet)")
            else:
                self.use_ai = False
                print("⚠️  ANTHROPIC_API_KEY not found. Using programmatic generation.")
        
        # Ensure directories exist
        (self.legal_dir / "contracts").mkdir(parents=True, exist_ok=True)
        (self.legal_dir / "litigation").mkdir(parents=True, exist_ok=True)
        (self.legal_dir / "compliance").mkdir(parents=True, exist_ok=True)
        
    def _generate_ai_content(self, content_type, context, word_count="200-400"):
        """Generate content using AI"""
        if not self.use_ai:
            return "AI generation not available."
        
        try:
            prompt = f"""Generate realistic {content_type} for a robotics company (Robotix).

Context:
{context}

Requirements:
- Professional legal/business tone
- Specific and realistic details
- {word_count} words
- No markdown formatting, just plain text

Generate ONLY the requested content:"""

            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            print(f"   ⚠️  AI generation failed: {str(e)}")
            return f"{content_type} content would go here."
    
    def generate_contracts(self, num_contracts=100):
        """Generate contract records with AI-generated terms"""
        print(f"Generating {num_contracts} contract records...")
        
        contracts = []
        
        contract_types = [
            "Non-Disclosure Agreement (NDA)",
            "Master Service Agreement",
            "Software License Agreement",
            "Equipment Purchase Agreement",
            "Consulting Services Agreement",
            "Partnership Agreement",
            "Distribution Agreement",
            "Supply Agreement",
            "Lease Agreement",
            "Employment Agreement"
        ]
        
        client_types = [
            "Manufacturing Company", "Tech Startup", "Automotive Manufacturer",
            "Logistics Company", "Healthcare Provider", "Retail Chain",
            "Government Agency", "University", "Consulting Firm"
        ]
        
        for i in range(num_contracts):
            contract_type = random.choice(contract_types)
            start_date = datetime.now() - timedelta(days=random.randint(30, 1095))
            
            # Contract duration varies by type
            if "NDA" in contract_type:
                duration_months = random.choice([24, 36, 60])
            elif "Employment" in contract_type:
                duration_months = 0  # At-will
            else:
                duration_months = random.choice([12, 24, 36, 48])
            
            end_date = start_date + timedelta(days=30*duration_months) if duration_months > 0 else None
            
            # Contract value
            if "NDA" in contract_type:
                value = 0
            elif "Equipment" in contract_type or "Supply" in contract_type:
                value = random.uniform(50000, 2000000)
            elif "License" in contract_type:
                value = random.uniform(10000, 200000)
            else:
                value = random.uniform(25000, 500000)
            
            status = "Active"
            if end_date and end_date < datetime.now():
                status = random.choice(["Expired", "Renewed", "Terminated"])
            elif end_date and (end_date - datetime.now()).days < 90:
                status = "Expiring Soon"
            
            # Generate AI content for key terms if enabled
            if self.use_ai and random.random() > 0.7:  # Generate for 30% to save API calls
                context = f"Contract Type: {contract_type}\nClient Type: {random.choice(client_types)}\nValue: ${value:,.0f}"
                key_terms = self._generate_ai_content("key contract terms and obligations", context, "100-150")
            else:
                key_terms = f"Standard {contract_type} terms apply"
            
            # Risk clauses
            has_indemnity = random.random() > 0.4
            has_limitation = random.random() > 0.3
            has_termination = random.random() > 0.2
            
            contracts.append({
                "contract_id": f"CTR-{i+1:05d}",
                "contract_type": contract_type,
                "counterparty": f"{random.choice(client_types)} #{random.randint(100, 999)}",
                "effective_date": start_date.strftime("%Y-%m-%d"),
                "expiration_date": end_date.strftime("%Y-%m-%d") if end_date else "At-Will",
                "contract_value": round(value, 2) if value > 0 else 0,
                "auto_renew": random.choice(["Yes", "No"]),
                "notice_period_days": random.choice([30, 60, 90]),
                "status": status,
                "has_indemnity_clause": "Yes" if has_indemnity else "No",
                "has_liability_limitation": "Yes" if has_limitation else "No",
                "has_termination_clause": "Yes" if has_termination else "No",
                "governing_law": random.choice(["Washington", "Delaware", "New York", "California"]),
                "key_terms": key_terms[:200],  # Limit length
                "owner": random.choice([e["name"] for e in EMPLOYEES if "Executive" in e["dept"] or "Finance" in e["dept"] or "Human Resources" in e["dept"]]),
                "risk_level": random.choice(["Low", "Low", "Medium", "Medium", "High"])
            })
            
            if (i + 1) % 10 == 0:
                print(f"   Progress: {i+1}/{num_contracts} contracts generated", end='\r')
        
        print(f"   Progress: {num_contracts}/{num_contracts} contracts generated")
        
        self._export_to_csv_json(contracts, self.legal_dir / "contracts" / "contract_register")
        print(f"✓ Generated {len(contracts)} contract records")
        return contracts
    
    def generate_litigation_records(self, num_cases=25):
        """Generate litigation and legal case records"""
        print(f"Generating {num_cases} litigation records...")
        
        cases = []
        
        case_types = [
            "Employment Dispute",
            "Contract Dispute",
            "Intellectual Property",
            "Product Liability",
            "Regulatory Compliance",
            "Vendor Dispute",
            "Customer Complaint",
            "Patent Infringement"
        ]
        
        for i in range(num_cases):
            case_type = random.choice(case_types)
            filed_date = datetime.now() - timedelta(days=random.randint(30, 900))
            
            # Case status and outcomes
            status_options = ["Active", "Active", "Active", "Settled", "Settled", "Dismissed", "Closed"]
            status = random.choice(status_options)
            
            if status in ["Settled", "Dismissed", "Closed"]:
                closed_date = filed_date + timedelta(days=random.randint(60, 400))
            else:
                closed_date = None
            
            # Legal costs
            monthly_cost = random.uniform(5000, 50000)
            months_active = ((closed_date or datetime.now()) - filed_date).days / 30
            total_cost = monthly_cost * months_active
            
            # Exposure/settlement
            if status == "Settled":
                settlement = random.uniform(10000, 500000)
            else:
                settlement = 0
                
            potential_exposure = random.uniform(50000, 2000000) if status == "Active" else 0
            
            # Generate AI description for some cases
            if self.use_ai and random.random() > 0.6:
                context = f"Case Type: {case_type}\nStatus: {status}\nFiled: {filed_date.strftime('%Y-%m-%d')}"
                description = self._generate_ai_content("legal case description and key issues", context, "80-120")
            else:
                description = f"{case_type} matter filed on {filed_date.strftime('%Y-%m-%d')}"
            
            cases.append({
                "case_id": f"LIT-{i+1:04d}",
                "case_type": case_type,
                "filed_date": filed_date.strftime("%Y-%m-%d"),
                "closed_date": closed_date.strftime("%Y-%m-%d") if closed_date else None,
                "status": status,
                "plaintiff": random.choice(["Robotix", "Third Party"]),
                "description": description[:250],
                "external_counsel": random.choice([
                    "Morrison & Foerster LLP", "Davis Wright Tremaine", 
                    "K&L Gates", "Perkins Coie", "Wilson Sonsini"
                ]),
                "legal_costs_to_date": round(total_cost, 2),
                "settlement_amount": round(settlement, 2) if settlement > 0 else None,
                "potential_exposure": round(potential_exposure, 2) if potential_exposure > 0 else None,
                "insurance_coverage": random.choice(["Yes", "No", "Partial"]),
                "priority": random.choice(["High", "Medium", "Low"]),
                "internal_contact": random.choice([e["name"] for e in EMPLOYEES if "Executive" in e["dept"] or "Human Resources" in e["dept"]])
            })
        
        self._export_to_csv_json(cases, self.legal_dir / "litigation" / "litigation_register")
        print(f"✓ Generated {len(cases)} litigation records")
        return cases
    
    def generate_compliance_records(self, num_records=60):
        """Generate compliance tracking records"""
        print(f"Generating {num_records} compliance records...")
        
        compliance_records = []
        
        compliance_areas = [
            "OSHA Safety Standards",
            "EPA Environmental",
            "ISO 9001 Quality",
            "ISO 14001 Environmental",
            "GDPR Data Privacy",
            "CCPA Data Privacy",
            "Export Control (ITAR/EAR)",
            "SOX Financial Controls",
            "Employment Law",
            "Product Safety (UL/CE)"
        ]
        
        for i in range(num_records):
            area = random.choice(compliance_areas)
            review_date = datetime.now() - timedelta(days=random.randint(1, 365))
            next_review = review_date + timedelta(days=random.choice([90, 180, 365]))
            
            status = random.choices(
                ["Compliant", "Minor Issues", "Action Required", "Under Review"],
                weights=[0.6, 0.25, 0.1, 0.05]
            )[0]
            
            num_findings = 0 if status == "Compliant" else random.randint(1, 8)
            num_critical = random.randint(0, 2) if status == "Action Required" else 0
            
            compliance_records.append({
                "compliance_id": f"CMP-{i+1:05d}",
                "compliance_area": area,
                "regulatory_body": self._get_regulatory_body(area),
                "last_review_date": review_date.strftime("%Y-%m-%d"),
                "next_review_date": next_review.strftime("%Y-%m-%d"),
                "status": status,
                "num_findings": num_findings,
                "num_critical_findings": num_critical,
                "certification_status": random.choice(["Certified", "In Progress", "Renewal Due", "N/A"]),
                "responsible_party": random.choice([e["name"] for e in EMPLOYEES]),
                "last_audit_score": round(random.uniform(75, 100), 1) if status in ["Compliant", "Minor Issues"] else round(random.uniform(60, 85), 1),
                "notes": "Regular compliance monitoring" if status == "Compliant" else "Remediation plan in progress"
            })
        
        self._export_to_csv_json(compliance_records, self.legal_dir / "compliance" / "compliance_register")
        print(f"✓ Generated {len(compliance_records)} compliance records")
        return compliance_records
    
    def generate_ip_portfolio(self):
        """Generate intellectual property portfolio"""
        print("Generating IP portfolio...")
        
        ip_records = []
        
        # Patents
        for i in range(15):
            filed_date = datetime.now() - timedelta(days=random.randint(365, 2190))
            
            ip_records.append({
                "ip_id": f"PAT-{i+1:03d}",
                "ip_type": "Patent",
                "title": f"Robotic System Innovation {i+1}",
                "filing_date": filed_date.strftime("%Y-%m-%d"),
                "grant_date": (filed_date + timedelta(days=random.randint(730, 1095))).strftime("%Y-%m-%d"),
                "expiration_date": (filed_date + timedelta(days=7300)).strftime("%Y-%m-%d"),  # 20 years
                "status": random.choice(["Granted", "Pending", "Abandoned"]),
                "jurisdiction": random.choice(["US", "EU", "JP", "CN", "International (PCT)"]),
                "inventors": ", ".join(random.sample([e["name"] for e in EMPLOYEES if "Product" in e["dept"] or "Development" in e["dept"]], k=random.randint(1, 3))),
                "maintenance_cost_annual": round(random.uniform(1000, 10000), 2),
                "value_estimate": round(random.uniform(50000, 500000), 2)
            })
        
        # Trademarks
        trademarks = ["Robotix", "RoboTech Solutions", "AutoMate Pro", "SmartBot Series"]
        for i, tm in enumerate(trademarks):
            ip_records.append({
                "ip_id": f"TM-{i+1:03d}",
                "ip_type": "Trademark",
                "title": tm,
                "filing_date": (datetime.now() - timedelta(days=random.randint(1095, 3650))).strftime("%Y-%m-%d"),
                "grant_date": (datetime.now() - timedelta(days=random.randint(730, 3285))).strftime("%Y-%m-%d"),
                "expiration_date": (datetime.now() + timedelta(days=random.randint(1825, 3650))).strftime("%Y-%m-%d"),
                "status": "Registered",
                "jurisdiction": "US",
                "inventors": "Robotix Legal Team",
                "maintenance_cost_annual": round(random.uniform(500, 2000), 2),
                "value_estimate": round(random.uniform(100000, 1000000), 2)
            })
        
        self._export_to_csv_json(ip_records, self.legal_dir / "intellectual_property")
        print(f"✓ Generated {len(ip_records)} IP records")
        return ip_records
    
    def _get_regulatory_body(self, area):
        """Get regulatory body for compliance area"""
        mapping = {
            "OSHA Safety Standards": "OSHA",
            "EPA Environmental": "EPA",
            "ISO 9001 Quality": "ISO",
            "ISO 14001 Environmental": "ISO",
            "GDPR Data Privacy": "EU Commission",
            "CCPA Data Privacy": "California AG",
            "Export Control (ITAR/EAR)": "State Dept/Commerce",
            "SOX Financial Controls": "SEC",
            "Employment Law": "DOL/EEOC",
            "Product Safety (UL/CE)": "UL/CE Certification Bodies"
        }
        return mapping.get(area, "Various")
    
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
    print("Legal & Contracts Data Generator")
    print("=" * 60)
    
    generator = LegalContractsGenerator(use_ai=True)
    
    generator.generate_contracts(num_contracts=100)
    generator.generate_litigation_records(num_cases=25)
    generator.generate_compliance_records(num_records=60)
    generator.generate_ip_portfolio()
    
    print("\n" + "=" * 60)
    print("✓ Legal & contracts data generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

