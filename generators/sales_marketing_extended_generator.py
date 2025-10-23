#!/usr/bin/env python3
"""
Sales & Marketing Extended Data Generator
Generates: pipeline, quotes, forecasts, engagement metrics, lead scoring
Uses AI for customer notes, email content, campaign messaging
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
from company_data import EMPLOYEES, get_random_date

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


class SalesMarketingExtendedGenerator:
    
    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = Path(data_dir)
        self.sales_dir = self.data_dir / "sales-marketing" / "sales"
        self.marketing_dir = self.data_dir / "sales-marketing" / "marketing"
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
        
        # Ensure directories
        (self.sales_dir / "pipeline").mkdir(parents=True, exist_ok=True)
        (self.sales_dir / "quotes").mkdir(parents=True, exist_ok=True)
        (self.sales_dir / "forecasts").mkdir(parents=True, exist_ok=True)
        (self.sales_dir / "quotas").mkdir(parents=True, exist_ok=True)
        (self.marketing_dir / "engagement").mkdir(parents=True, exist_ok=True)
        (self.marketing_dir / "lead_scoring").mkdir(parents=True, exist_ok=True)
        (self.marketing_dir / "email_campaigns").mkdir(parents=True, exist_ok=True)
    
    def _generate_ai_content(self, content_type, context, word_count="80-120"):
        """Generate content using AI"""
        if not self.use_ai:
            return "AI generation not available."
        
        try:
            prompt = f"""Generate realistic {content_type} for Robotix (robotics company).

Context:
{context}

Requirements:
- Professional business tone
- Specific and realistic
- {word_count} words
- Plain text only

Generate:"""

            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            return f"{content_type} content"
    
    def generate_sales_pipeline(self, num_opportunities=200):
        """Generate sales pipeline/CRM opportunities"""
        print(f"Generating {num_opportunities} pipeline opportunities...")
        
        opportunities = []
        
        stages = [
            "Prospecting",
            "Qualification",
            "Needs Analysis",
            "Proposal",
            "Negotiation",
            "Closed Won",
            "Closed Lost"
        ]
        
        stage_probabilities = {
            "Prospecting": 10,
            "Qualification": 20,
            "Needs Analysis": 40,
            "Proposal": 60,
            "Negotiation": 80,
            "Closed Won": 100,
            "Closed Lost": 0
        }
        
        products = [
            "Industrial Robot System",
            "Collaborative Robot",
            "Mobile Robot Platform",
            "Vision System",
            "Control Software License"
        ]
        
        for i in range(num_opportunities):
            stage = random.choice(stages)
            created_date = datetime.now() - timedelta(days=random.randint(1, 365))
            
            # Deal value
            deal_value = random.uniform(25000, 2000000)
            probability = stage_probabilities[stage]
            weighted_value = deal_value * (probability / 100)
            
            # Expected close date
            if stage in ["Closed Won", "Closed Lost"]:
                expected_close = created_date + timedelta(days=random.randint(30, 180))
                actual_close = expected_close
            else:
                days_out = {"Prospecting": 90, "Qualification": 75, "Needs Analysis": 60, 
                           "Proposal": 45, "Negotiation": 30}.get(stage, 60)
                expected_close = datetime.now() + timedelta(days=random.randint(0, days_out))
                actual_close = None
            
            # Generate AI notes for some opportunities
            if self.use_ai and random.random() > 0.70:
                context = f"Stage: {stage}\nProduct: {random.choice(products)}\nValue: ${deal_value:,.0f}"
                notes = self._generate_ai_content("sales opportunity notes and next steps", context, "60-100")
            else:
                notes = f"{stage} stage opportunity"
            
            opportunities.append({
                "opportunity_id": f"OPP-{i+1:06d}",
                "account_name": f"Company {random.randint(1000, 9999)}",
                "opportunity_name": f"{random.choice(products)} - {random.randint(100, 999)}",
                "stage": stage,
                "probability_pct": probability,
                "amount": round(deal_value, 2),
                "weighted_amount": round(weighted_value, 2),
                "created_date": created_date.strftime("%Y-%m-%d"),
                "expected_close_date": expected_close.strftime("%Y-%m-%d"),
                "actual_close_date": actual_close.strftime("%Y-%m-%d") if actual_close else None,
                "age_days": (datetime.now() - created_date).days,
                "lead_source": random.choice(["Website", "Referral", "Cold Call", "Trade Show", "Partner"]),
                "owner": random.choice([e["name"] for e in EMPLOYEES if "Sales" in e["dept"]]),
                "product_interest": random.choice(products),
                "competitor": random.choice(["None", "ABB Robotics", "FANUC", "KUKA", "Universal Robots"]),
                "next_step": "Follow up meeting" if stage not in ["Closed Won", "Closed Lost"] else None,
                "notes": notes[:200]
            })
        
        self._export_to_csv_json(opportunities, self.sales_dir / "pipeline" / "sales_pipeline")
        print(f"✓ Generated {len(opportunities)} pipeline opportunities")
        return opportunities
    
    def generate_quotes(self, num_quotes=150):
        """Generate sales quotes"""
        print(f"Generating {num_quotes} sales quotes...")
        
        quotes = []
        
        for i in range(num_quotes):
            quote_date = datetime.now() - timedelta(days=random.randint(1, 365))
            valid_until = quote_date + timedelta(days=random.choice([30, 45, 60, 90]))
            
            # Quote amount
            amount = random.uniform(15000, 500000)
            discount_pct = random.choice([0, 5, 10, 15, 20])
            discount = amount * (discount_pct / 100)
            final_amount = amount - discount
            
            status = random.choices(
                ["Draft", "Sent", "Viewed", "Accepted", "Rejected", "Expired"],
                weights=[0.10, 0.20, 0.15, 0.30, 0.15, 0.10]
            )[0]
            
            quotes.append({
                "quote_id": f"QUO-{i+1:06d}",
                "opportunity_id": f"OPP-{random.randint(1, 200):06d}",
                "customer_name": f"Company {random.randint(1000, 9999)}",
                "quote_date": quote_date.strftime("%Y-%m-%d"),
                "valid_until": valid_until.strftime("%Y-%m-%d"),
                "subtotal": round(amount, 2),
                "discount_pct": discount_pct,
                "discount_amount": round(discount, 2),
                "tax": round(final_amount * 0.08, 2),
                "total": round(final_amount * 1.08, 2),
                "status": status,
                "payment_terms": random.choice(["Net 30", "Net 45", "Net 60", "50% Upfront"]),
                "delivery_time_weeks": random.choice([4, 6, 8, 12, 16]),
                "owner": random.choice([e["name"] for e in EMPLOYEES if "Sales" in e["dept"]]),
                "revision_number": random.randint(1, 3),
                "follow_up_date": (quote_date + timedelta(days=7)).strftime("%Y-%m-%d") if status == "Sent" else None
            })
        
        self._export_to_csv_json(quotes, self.sales_dir / "quotes" / "sales_quotes")
        print(f"✓ Generated {len(quotes)} sales quotes")
        return quotes
    
    def generate_sales_forecasts(self, num_quarters=8):
        """Generate quarterly sales forecasts"""
        print(f"Generating sales forecasts for {num_quarters} quarters...")
        
        forecasts = []
        
        sales_reps = [e for e in EMPLOYEES if "Sales" in e["dept"]]
        start_date = datetime.now() - timedelta(days=91*num_quarters)
        
        for quarter_offset in range(num_quarters):
            quarter_date = start_date + timedelta(days=91*quarter_offset)
            quarter_str = f"Q{((quarter_date.month-1)//3)+1} {quarter_date.year}"
            
            for rep in sales_reps:
                # Forecast vs actual
                forecast = random.uniform(300000, 1200000)
                
                if quarter_date < datetime.now() - timedelta(days=91):
                    # Historical - has actuals
                    actual = forecast * random.uniform(0.75, 1.25)
                    attainment = (actual / forecast) * 100
                else:
                    # Future - no actuals yet
                    actual = None
                    attainment = None
                
                pipeline_value = forecast * random.uniform(2.0, 4.0)
                weighted_pipeline = pipeline_value * 0.45
                
                forecasts.append({
                    "quarter": quarter_str,
                    "sales_rep": rep["name"],
                    "region": random.choice(["West", "East", "Central", "International"]),
                    "forecast_amount": round(forecast, 2),
                    "actual_amount": round(actual, 2) if actual else None,
                    "attainment_pct": round(attainment, 1) if attainment else None,
                    "pipeline_value": round(pipeline_value, 2),
                    "weighted_pipeline": round(weighted_pipeline, 2),
                    "num_opportunities": random.randint(15, 45),
                    "avg_deal_size": round(forecast / random.randint(15, 25), 2),
                    "forecast_category": random.choice(["Commit", "Best Case", "Pipeline"]),
                    "confidence_level": random.choice(["High", "Medium", "Low"])
                })
        
        self._export_to_csv_json(forecasts, self.sales_dir / "forecasts" / "sales_forecasts")
        print(f"✓ Generated {len(forecasts)} forecast records")
        return forecasts
    
    def generate_quota_attainment(self, num_quarters=8):
        """Generate quota attainment tracking"""
        print(f"Generating quota attainment for {num_quarters} quarters...")
        
        quota_records = []
        
        sales_reps = [e for e in EMPLOYEES if "Sales" in e["dept"]]
        start_date = datetime.now() - timedelta(days=91*num_quarters)
        
        for quarter_offset in range(num_quarters):
            quarter_date = start_date + timedelta(days=91*quarter_offset)
            quarter_str = f"Q{((quarter_date.month-1)//3)+1} {quarter_date.year}"
            
            # Only generate for past quarters
            if quarter_date >= datetime.now() - timedelta(days=91):
                continue
            
            for rep in sales_reps:
                quota = random.uniform(400000, 1000000)
                actual = quota * random.uniform(0.60, 1.40)
                attainment = (actual / quota) * 100
                
                quota_records.append({
                    "quarter": quarter_str,
                    "sales_rep": rep["name"],
                    "team": random.choice(["Enterprise", "SMB", "Channel"]),
                    "quota": round(quota, 2),
                    "actual_revenue": round(actual, 2),
                    "attainment_pct": round(attainment, 1),
                    "deals_closed": random.randint(8, 35),
                    "avg_deal_size": round(actual / random.randint(8, 25), 2),
                    "commission_earned": round(actual * random.uniform(0.03, 0.08), 2),
                    "rank": random.randint(1, len(sales_reps)),
                    "performance_rating": "Exceeds" if attainment > 110 else "Meets" if attainment > 90 else "Below"
                })
        
        self._export_to_csv_json(quota_records, self.sales_dir / "quotas" / "quota_attainment")
        print(f"✓ Generated {len(quota_records)} quota records")
        return quota_records
    
    def generate_marketing_engagement(self, num_months=24):
        """Generate marketing engagement metrics - separate by channel"""
        print(f"Generating marketing engagement for {num_months} months...")
        
        email_records = []
        website_records = []
        social_records = []
        
        start_date = datetime.now() - timedelta(days=30*num_months)
        
        for month_offset in range(num_months):
            month_date = start_date + timedelta(days=30*month_offset)
            month_str = month_date.strftime("%Y-%m")
            
            # Email metrics
            sent = random.randint(15000, 35000)
            opens = int(sent * random.uniform(0.18, 0.28))
            clicks = int(opens * random.uniform(0.12, 0.25))
            conversions = int(clicks * random.uniform(0.03, 0.08))
            
            email_records.append({
                "month": month_str,
                "emails_sent": sent,
                "unique_opens": opens,
                "open_rate_pct": round((opens/sent)*100, 1),
                "clicks": clicks,
                "click_rate_pct": round((clicks/sent)*100, 1),
                "conversions": conversions,
                "conversion_rate_pct": round((conversions/sent)*100, 2),
                "unsubscribes": random.randint(50, 200),
                "bounce_rate_pct": round(random.uniform(1, 4), 1)
            })
            
            # Website metrics
            visits = random.randint(25000, 60000)
            unique = int(visits * random.uniform(0.65, 0.85))
            
            website_records.append({
                "month": month_str,
                "total_visits": visits,
                "unique_visitors": unique,
                "page_views": int(visits * random.uniform(2.5, 4.5)),
                "avg_session_duration_minutes": round(random.uniform(2.5, 6.5), 1),
                "bounce_rate_pct": round(random.uniform(35, 55), 1),
                "conversions": random.randint(150, 450),
                "conversion_rate_pct": round(random.uniform(0.5, 1.5), 2),
                "leads_generated": random.randint(120, 380)
            })
            
            # Social Media metrics
            followers = random.randint(8000, 15000)
            
            social_records.append({
                "month": month_str,
                "followers": followers,
                "posts": random.randint(15, 40),
                "impressions": random.randint(50000, 150000),
                "engagements": random.randint(1500, 5000),
                "engagement_rate_pct": round(random.uniform(1.5, 4.5), 1),
                "clicks": random.randint(400, 1200),
                "conversions": random.randint(10, 50),
                "leads_generated": random.randint(25, 100)
            })
        
        # Export each channel separately
        self._export_to_csv_json(email_records, self.marketing_dir / "engagement" / "email_engagement")
        self._export_to_csv_json(website_records, self.marketing_dir / "engagement" / "website_engagement")
        self._export_to_csv_json(social_records, self.marketing_dir / "engagement" / "social_media_engagement")
        
        total_records = len(email_records) + len(website_records) + len(social_records)
        print(f"✓ Generated {total_records} engagement records across 3 channels")
        return email_records, website_records, social_records
    
    def generate_lead_scoring(self, num_leads=500):
        """Generate lead scoring data"""
        print(f"Generating {num_leads} lead scores...")
        
        lead_scores = []
        
        for i in range(num_leads):
            # Scoring factors
            email_engagement = random.randint(0, 30)
            website_visits = random.randint(0, 25)
            content_downloads = random.randint(0, 20)
            demo_request = random.choice([0, 25])
            title_score = random.choice([5, 10, 15, 20])
            company_size_score = random.choice([5, 10, 15, 20])
            industry_fit = random.choice([0, 10, 20])
            
            total_score = (email_engagement + website_visits + content_downloads + 
                          demo_request + title_score + company_size_score + industry_fit)
            
            # Grade based on score
            if total_score >= 80:
                grade = "A"
            elif total_score >= 60:
                grade = "B"
            elif total_score >= 40:
                grade = "C"
            else:
                grade = "D"
            
            status = random.choices(
                ["New", "Working", "Qualified", "Unqualified", "Converted"],
                weights=[0.20, 0.25, 0.20, 0.15, 0.20]
            )[0]
            
            lead_scores.append({
                "lead_id": f"LEAD-{i+1:06d}",
                "company_name": f"Company {random.randint(1000, 9999)}",
                "created_date": (datetime.now() - timedelta(days=random.randint(1, 180))).strftime("%Y-%m-%d"),
                "lead_source": random.choice(["Website", "Trade Show", "Referral", "Cold Call", "Content Download"]),
                "email_engagement_score": email_engagement,
                "website_score": website_visits,
                "content_score": content_downloads,
                "demo_score": demo_request,
                "demographic_score": title_score + company_size_score + industry_fit,
                "total_score": total_score,
                "grade": grade,
                "status": status,
                "last_activity_date": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
                "assigned_to": random.choice([e["name"] for e in EMPLOYEES if "Sales" in e["dept"] or "Marketing" in e["dept"]]),
                "lifecycle_stage": random.choice(["Subscriber", "Lead", "MQL", "SQL", "Opportunity"])
            })
        
        self._export_to_csv_json(lead_scores, self.marketing_dir / "lead_scoring" / "lead_scores")
        print(f"✓ Generated {len(lead_scores)} lead scores")
        return lead_scores
    
    def _export_to_csv_json(self, data, base_filename):
        """Export data to both CSV and JSON"""
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
    print("Sales & Marketing Extended Data Generator")
    print("=" * 60)
    
    generator = SalesMarketingExtendedGenerator(use_ai=True)
    
    generator.generate_sales_pipeline(num_opportunities=200)
    generator.generate_quotes(num_quotes=150)
    generator.generate_sales_forecasts(num_quarters=8)
    generator.generate_quota_attainment(num_quarters=6)
    generator.generate_marketing_engagement(num_months=24)
    generator.generate_lead_scoring(num_leads=500)
    
    print("\n" + "=" * 60)
    print("✓ Sales & marketing extended data generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

