#!/usr/bin/env python3
"""
Product Extended Data Generator
Generates: releases, bugs, features, user metrics, feedback
Uses AI for bug descriptions, feature specs, user feedback
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


class ProductExtendedGenerator:
    
    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = Path(data_dir)
        self.product_dir = self.data_dir / "product"
        self.use_ai = use_ai and AI_AVAILABLE
        
        # Initialize AI
        if self.use_ai:
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key:
                self.llm = ChatAnthropic(
                    model="claude-3-5-sonnet-20241022",
                    temperature=0.7,
                    max_tokens=3000
                )
                print("✅ AI content generation enabled")
            else:
                self.use_ai = False
                print("⚠️  ANTHROPIC_API_KEY not found.")
        
        # Ensure directories
        (self.product_dir / "releases").mkdir(parents=True, exist_ok=True)
        (self.product_dir / "bugs").mkdir(parents=True, exist_ok=True)
        (self.product_dir / "features").mkdir(parents=True, exist_ok=True)
        (self.product_dir / "user_metrics").mkdir(parents=True, exist_ok=True)
        (self.product_dir / "feedback").mkdir(parents=True, exist_ok=True)
    
    def _generate_ai_content(self, content_type, context, word_count="100-200"):
        """Generate content using AI"""
        if not self.use_ai:
            return "AI generation not available."
        
        try:
            prompt = f"""Generate realistic {content_type} for Robotix (robotics/automation company).

Context:
{context}

Requirements:
- Technical but clear language
- Specific and realistic
- {word_count} words
- Plain text only

Generate:"""

            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            return f"{content_type} content"
    
    def generate_product_releases(self, num_releases=20):
        """Generate software/product release history"""
        print(f"Generating {num_releases} product releases...")
        
        releases = []
        
        products = [
            "RobotOS Control Suite",
            "Fleet Management Platform",
            "Predictive Maintenance AI",
            "Simulation & Programming Tool",
            "Vision System Pro"
        ]
        
        release_types = ["Major", "Minor", "Patch", "Hotfix"]
        
        start_date = datetime.now() - timedelta(days=730)  # 2 years ago
        
        for i in range(num_releases):
            product = random.choice(products)
            release_type = random.choices(release_types, weights=[0.15, 0.35, 0.35, 0.15])[0]
            
            release_date = start_date + timedelta(days=random.randint(0, 730))
            
            # Version numbering
            major = random.randint(1, 5)
            minor = random.randint(0, 15)
            patch = random.randint(0, 20)
            version = f"{major}.{minor}.{patch}"
            
            # Features and bugs
            num_features = random.randint(3, 15) if release_type in ["Major", "Minor"] else random.randint(0, 3)
            num_bugs_fixed = random.randint(5, 30)
            
            # Generate AI release notes for major releases
            if self.use_ai and release_type in ["Major", "Minor"] and random.random() > 0.5:
                context = f"Product: {product}\nVersion: {version}\nType: {release_type}\n{num_features} new features, {num_bugs_fixed} bugs fixed"
                release_notes = self._generate_ai_content("product release notes highlighting key features", context, "150-250")
            else:
                release_notes = f"{release_type} release with {num_features} features and {num_bugs_fixed} bug fixes"
            
            releases.append({
                "release_id": f"REL-{i+1:04d}",
                "product_name": product,
                "version": version,
                "release_type": release_type,
                "release_date": release_date.strftime("%Y-%m-%d"),
                "num_features": num_features,
                "num_bugs_fixed": num_bugs_fixed,
                "num_breaking_changes": random.randint(0, 3) if release_type == "Major" else 0,
                "release_notes": release_notes[:300],
                "status": "Released",
                "adoption_rate_pct": round(random.uniform(65, 98), 1),
                "rollback_required": "Yes" if random.random() < 0.05 else "No"
            })
        
        # Sort by date
        releases.sort(key=lambda x: x["release_date"])
        
        self._export_to_csv_json(releases, self.product_dir / "releases" / "release_history")
        print(f"✓ Generated {len(releases)} product releases")
        return releases
    
    def generate_bug_records(self, num_bugs=250):
        """Generate bug tracking records"""
        print(f"Generating {num_bugs} bug records...")
        
        bugs = []
        
        products = [
            "RobotOS Control Suite",
            "Fleet Management Platform",
            "Predictive Maintenance AI",
            "Simulation Tool",
            "Vision System Pro"
        ]
        
        bug_categories = [
            "UI/UX Issue",
            "Performance",
            "Data Integrity",
            "Integration",
            "Security",
            "Crash/Stability",
            "Feature Malfunction",
            "Documentation"
        ]
        
        for i in range(num_bugs):
            created_date = datetime.now() - timedelta(days=random.randint(1, 730))
            priority = random.choices(["Critical", "High", "Medium", "Low"], weights=[0.05, 0.20, 0.50, 0.25])[0]
            status = random.choices(
                ["Open", "In Progress", "Fixed", "Closed", "Wont Fix"],
                weights=[0.15, 0.20, 0.25, 0.35, 0.05]
            )[0]
            
            category = random.choice(bug_categories)
            
            # Resolution time based on priority and status
            if status in ["Fixed", "Closed"]:
                if priority == "Critical":
                    days_to_fix = random.randint(1, 5)
                elif priority == "High":
                    days_to_fix = random.randint(3, 15)
                else:
                    days_to_fix = random.randint(7, 60)
                resolved_date = created_date + timedelta(days=days_to_fix)
            else:
                resolved_date = None
                days_to_fix = (datetime.now() - created_date).days
            
            # Generate AI bug description for some bugs
            if self.use_ai and random.random() > 0.7:  # 30% get AI descriptions
                context = f"Product: {random.choice(products)}\nCategory: {category}\nPriority: {priority}"
                description = self._generate_ai_content("bug report description and steps to reproduce", context, "80-120")
            else:
                description = f"{category} issue in {random.choice(products)}"
            
            bugs.append({
                "bug_id": f"BUG-{i+1:06d}",
                "product_name": random.choice(products),
                "title": f"{category} - {random.choice(['Error', 'Issue', 'Problem', 'Defect'])} #{i+1}",
                "description": description[:250],
                "category": category,
                "priority": priority,
                "severity": random.choice(["Critical", "Major", "Minor", "Trivial"]),
                "status": status,
                "created_date": created_date.strftime("%Y-%m-%d"),
                "resolved_date": resolved_date.strftime("%Y-%m-%d") if resolved_date else None,
                "days_to_fix": days_to_fix if resolved_date else None,
                "assigned_to": random.choice([e["name"] for e in EMPLOYEES if "Product" in e["dept"] or "Development" in e["dept"]]),
                "reported_by": random.choice(["Customer", "Customer", "QA", "Engineering", "Support"]),
                "reproducible": random.choice(["Yes", "Yes", "Sometimes", "No"]),
                "version_affected": f"{random.randint(1,5)}.{random.randint(0,15)}.{random.randint(0,20)}",
                "fix_version": f"{random.randint(1,5)}.{random.randint(0,15)}.{random.randint(0,20)}" if resolved_date else None
            })
        
        self._export_to_csv_json(bugs, self.product_dir / "bugs" / "bug_tracker")
        print(f"✓ Generated {len(bugs)} bug records")
        return bugs
    
    def generate_feature_adoption(self, num_features=40):
        """Generate feature adoption metrics"""
        print(f"Generating {num_features} feature adoption records...")
        
        features = []
        
        products = [
            "RobotOS Control Suite",
            "Fleet Management Platform",
            "Predictive Maintenance AI",
            "Simulation Tool"
        ]
        
        feature_types = [
            "Core Functionality",
            "Advanced Tool",
            "Integration",
            "Reporting",
            "Automation",
            "Collaboration",
            "Analytics"
        ]
        
        for i in range(num_features):
            product = random.choice(products)
            feature_type = random.choice(feature_types)
            release_date = datetime.now() - timedelta(days=random.randint(30, 730))
            
            # Adoption grows over time
            days_since_release = (datetime.now() - release_date).days
            max_adoption = random.uniform(40, 95)
            current_adoption = min(max_adoption, (days_since_release / 180) * max_adoption)
            
            monthly_active_users = random.randint(100, 5000)
            users_adopted = int(monthly_active_users * (current_adoption / 100))
            
            features.append({
                "feature_id": f"FTR-{i+1:04d}",
                "product_name": product,
                "feature_name": f"{feature_type} Feature {i+1}",
                "feature_type": feature_type,
                "release_date": release_date.strftime("%Y-%m-%d"),
                "days_since_release": days_since_release,
                "adoption_rate_pct": round(current_adoption, 1),
                "monthly_active_users": monthly_active_users,
                "users_adopted_count": users_adopted,
                "usage_frequency": random.choice(["Daily", "Weekly", "Monthly", "Occasional"]),
                "avg_session_time_minutes": round(random.uniform(5, 45), 1),
                "customer_satisfaction": round(random.uniform(3.5, 5.0), 1),
                "support_tickets_count": random.randint(0, 25)
            })
        
        self._export_to_csv_json(features, self.product_dir / "features" / "feature_adoption")
        print(f"✓ Generated {len(features)} feature records")
        return features
    
    def generate_user_metrics(self, num_months=24):
        """Generate monthly user metrics"""
        print(f"Generating user metrics for {num_months} months...")
        
        metrics = []
        
        products = ["RobotOS Control Suite", "Fleet Management Platform", "Predictive Maintenance AI"]
        
        start_date = datetime.now() - timedelta(days=30*num_months)
        
        for product in products:
            # Starting metrics
            mau = random.randint(2000, 5000)
            
            for month_offset in range(num_months):
                month_date = start_date + timedelta(days=30*month_offset)
                month_str = month_date.strftime("%Y-%m")
                
                # Simulate growth
                growth = random.uniform(-0.05, 0.15)
                mau = int(mau * (1 + growth))
                
                dau = int(mau * random.uniform(0.25, 0.40))
                wau = int(mau * random.uniform(0.50, 0.70))
                
                new_users = int(mau * random.uniform(0.08, 0.15))
                churned_users = int(mau * random.uniform(0.03, 0.10))
                
                metrics.append({
                    "month": month_str,
                    "product_name": product,
                    "monthly_active_users": mau,
                    "daily_active_users_avg": dau,
                    "weekly_active_users_avg": wau,
                    "new_users": new_users,
                    "churned_users": churned_users,
                    "retention_rate_pct": round(((mau - churned_users) / mau) * 100, 1),
                    "avg_sessions_per_user": round(random.uniform(8, 25), 1),
                    "avg_session_duration_minutes": round(random.uniform(15, 45), 1),
                    "feature_adoption_rate_pct": round(random.uniform(55, 85), 1),
                    "nps_score": random.randint(35, 75)
                })
        
        self._export_to_csv_json(metrics, self.product_dir / "user_metrics" / "monthly_user_metrics")
        print(f"✓ Generated {len(metrics)} user metric records")
        return metrics
    
    def generate_customer_feedback(self, num_feedback=150):
        """Generate customer feedback and feature requests"""
        print(f"Generating {num_feedback} customer feedback records...")
        
        feedback_records = []
        
        feedback_types = ["Feature Request", "Bug Report", "Usability Feedback", "Performance Issue", "Compliment"]
        products = ["RobotOS Control Suite", "Fleet Management Platform", "Predictive Maintenance AI", "Vision System Pro"]
        
        for i in range(num_feedback):
            feedback_type = random.choice(feedback_types)
            submitted_date = datetime.now() - timedelta(days=random.randint(1, 365))
            
            status = random.choices(
                ["New", "Under Review", "Planned", "In Development", "Completed", "Declined"],
                weights=[0.20, 0.15, 0.20, 0.15, 0.20, 0.10]
            )[0]
            
            votes = random.randint(0, 150)
            priority = "High" if votes > 50 else "Medium" if votes > 20 else "Low"
            
            # Generate AI feedback for some records
            if self.use_ai and random.random() > 0.65:
                context = f"Type: {feedback_type}\nProduct: {random.choice(products)}\nVotes: {votes}"
                feedback_text = self._generate_ai_content("customer feedback or feature request", context, "60-100")
            else:
                feedback_text = f"{feedback_type} for {random.choice(products)}"
            
            feedback_records.append({
                "feedback_id": f"FB-{i+1:05d}",
                "product_name": random.choice(products),
                "feedback_type": feedback_type,
                "title": f"{feedback_type} #{i+1}",
                "description": feedback_text[:200],
                "submitted_date": submitted_date.strftime("%Y-%m-%d"),
                "submitted_by": random.choice(["Customer Portal", "Email", "Support Ticket", "Sales Rep"]),
                "customer_segment": random.choice(["Enterprise", "SMB", "Startup"]),
                "status": status,
                "priority": priority,
                "votes": votes,
                "assigned_to": random.choice([e["name"] for e in EMPLOYEES if "Product" in e["dept"] or "Development" in e["dept"]]) if status not in ["New", "Declined"] else None,
                "target_release": f"{random.randint(2,6)}.{random.randint(0,5)}.0" if status in ["Planned", "In Development"] else None,
                "sentiment": random.choice(["Positive", "Neutral", "Negative"])
            })
        
        self._export_to_csv_json(feedback_records, self.product_dir / "feedback" / "customer_feedback")
        print(f"✓ Generated {len(feedback_records)} feedback records")
        return feedback_records
    
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
    print("Product Extended Data Generator")
    print("=" * 60)
    
    generator = ProductExtendedGenerator(use_ai=True)
    
    generator.generate_product_releases(num_releases=20)
    generator.generate_bug_records(num_bugs=250)
    generator.generate_feature_adoption(num_features=40)
    generator.generate_user_metrics(num_months=24)
    generator.generate_customer_feedback(num_feedback=150)
    
    print("\n" + "=" * 60)
    print("✓ Product extended data generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

