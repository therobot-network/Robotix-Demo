#!/usr/bin/env python3
"""
Financial & Marketing Data Generator
Creates invoices, budget reports, P&L statements, campaigns, feedback forms, and lead tracking
AI-FIRST approach for Robotix robotics company
"""

import csv
import json
import random
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from company_data import COMPANY, DEPARTMENTS, EMPLOYEES

# Load environment variables from project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
env_path = os.path.join(project_root, ".env")
load_dotenv(env_path)

# AI Integration
try:
    from langchain_anthropic import ChatAnthropic

    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    print("⚠️  LangChain not installed. Run: pip install langchain langchain-anthropic")


class FinancialMarketingGenerator:

    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = data_dir
        self.use_ai = use_ai and AI_AVAILABLE
        self.generated_docs = []

        # Load existing data for reference
        self.orders = self._load_json(os.path.join(data_dir, "orders.json"))
        self.customers = self._load_json(os.path.join(data_dir, "customers.json"))
        self.products = self._load_json(os.path.join(data_dir, "products.json"))

        # Initialize AI model if available
        if self.use_ai:
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key:
                self.llm = ChatAnthropic(
                    model="claude-3-5-sonnet-20241022", temperature=0.7, max_tokens=8000
                )
                print("✅ AI content generation enabled (Claude 3.5 Sonnet)")
            else:
                self.use_ai = False
                print("⚠️  ANTHROPIC_API_KEY not found. Set it for AI generation.")

    def _load_json(self, filepath):
        """Load JSON data from file"""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Could not load {filepath}: {e}")
            return []

    def _get_timestamp(self):
        """Get formatted timestamp"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _print_progress_bar(self, current, total, label="Progress", width=40):
        """Print a progress bar"""
        percent = current / total
        filled = int(width * percent)
        bar = "█" * filled + "░" * (width - filled)
        print(
            f"   {label}: [{bar}] {int(percent * 100)}% ({current}/{total})", end="\r"
        )
        if current == total:
            print()

    def _generate_ai_content(self, doc_type, context, word_count="800-1500"):
        """Generate content using AI"""
        if not self.use_ai:
            return (
                f"<p>AI generation not available. {doc_type} content would go here.</p>"
            )

        try:
            prompt = f"""Generate a comprehensive, realistic {doc_type} document for Robotix.

Company Context:
{context}

Requirements:
- Professional business tone appropriate for {doc_type}
- Realistic, specific details, metrics, and financial data
- Well-structured with clear sections using HTML tags (h2, h3, p, ul, li, strong, em, table)
- {word_count} words
- Include concrete examples and actionable information
- Use proper HTML formatting (but NO <h1> tag - that's added separately)
- Make it feel authentic and comprehensive for a robotics company

Generate ONLY the HTML content body (no document headers, no <html> or <body> tags)."""

            response = self.llm.invoke(prompt)
            content = response.content.strip()
            content = content.replace("<h1>", "<h2>").replace("</h1>", "</h2>")
            return content
        except Exception as e:
            print(f"   ⚠️  AI generation failed for {doc_type}: {str(e)}")
            return (
                f"<p>Content generation failed. {doc_type} content would go here.</p>"
            )

    # ===== FINANCIAL DATA =====

    def generate_invoices(self, num_invoices=200):
        """Generate invoices tied to existing orders"""
        print(f"[{self._get_timestamp()}] Generating {num_invoices} invoices...")
        invoices = []

        # Sample orders that have been delivered/completed
        completed_orders = [
            o for o in self.orders if o["order_status"] in ["Delivered", "Completed"]
        ]
        sampled_orders = random.sample(
            completed_orders, min(num_invoices, len(completed_orders))
        )

        for i, order in enumerate(sampled_orders):
            # Invoice date is 1-5 days after order date
            order_date = datetime.strptime(order["order_date"], "%Y-%m-%d")
            invoice_date = order_date + timedelta(days=random.randint(1, 5))

            # Payment status and date
            payment_status = random.choice(
                ["Paid", "Paid", "Paid", "Pending", "Overdue"]
            )
            if payment_status == "Paid":
                days_to_pay = random.randint(1, 30)
                payment_date = invoice_date + timedelta(days=days_to_pay)
            else:
                payment_date = None

            invoice = {
                "invoice_id": f"INV-{2024}{str(i+1).zfill(4)}",
                "customer_id": order["customer_id"],
                "order_id": order["order_id"],
                "invoice_date": invoice_date.strftime("%Y-%m-%d"),
                "due_date": (invoice_date + timedelta(days=30)).strftime("%Y-%m-%d"),
                "subtotal": order["subtotal"],
                "tax": order["tax"],
                "shipping": order["shipping"],
                "total": order["total"],
                "payment_status": payment_status,
                "payment_date": (
                    payment_date.strftime("%Y-%m-%d") if payment_date else None
                ),
                "payment_method": order["payment_method"],
                "notes": random.choice(
                    [
                        "Thank you for your business",
                        "Payment received - thank you",
                        "Net 30 payment terms",
                        "Contact accounting for questions",
                        "",
                    ]
                ),
            }
            invoices.append(invoice)

            if (i + 1) % 20 == 0:
                self._print_progress_bar(i + 1, num_invoices, "Generating invoices")

        self._print_progress_bar(num_invoices, num_invoices, "Generating invoices")

        # Export to CSV and JSON
        self._export_to_csv_json(invoices, "invoices")
        print(f"  ✓ Generated {len(invoices)} invoices")
        return invoices

    def generate_budget_reports(self, num_reports=5):
        """Generate quarterly budget reports in HTML"""
        print(
            f"[{self._get_timestamp()}] Generating {num_reports} quarterly budget reports..."
        )

        os.makedirs(
            os.path.join(self.data_dir, "html_documents/financial"), exist_ok=True
        )

        quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024", "Q1 2025"]

        for i, quarter in enumerate(quarters[:num_reports]):
            context = f"""
Company: {COMPANY['name']}
Industry: {COMPANY['industry']}
Revenue: {COMPANY['revenue']}
Employees: {COMPANY['employees']}

Generate a quarterly budget report for {quarter} showing:
- Revenue by product category (Industrial Robots, Collaborative Robots, Mobile Robots, Software)
- Expenses by department: {', '.join(DEPARTMENTS)}
- Budget vs actual comparisons
- Variance analysis
- Use realistic numbers that align with a $42M annual revenue company
- Include detailed HTML tables with financial data
"""

            content = self._generate_ai_content(
                f"Quarterly Budget Report - {quarter}", context
            )

            doc = {
                "title": f"Budget Report - {quarter}",
                "category": "Financial",
                "type": "Budget Report",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "author": "Michael Rodriguez, CFO",
                "content": content,
            }

            self.generated_docs.append(doc)
            self._save_html_document(doc, "financial")

            self._print_progress_bar(i + 1, num_reports, "Generating budget reports")

        print(f"  ✓ Generated {num_reports} budget reports")
        return self.generated_docs

    def generate_pl_statements(self, num_statements=3):
        """Generate annual P&L statements in Markdown"""
        print(
            f"[{self._get_timestamp()}] Generating {num_statements} P&L statements..."
        )

        os.makedirs(
            os.path.join(self.data_dir, "unstructured/financial"), exist_ok=True
        )

        years = [2022, 2023, 2024]

        for i, year in enumerate(years[:num_statements]):
            context = f"""
Company: {COMPANY['name']}
Industry: {COMPANY['industry']}
Current Revenue: {COMPANY['revenue']}

Generate an annual Profit & Loss statement for {year} showing:
- Revenue breakdown by product categories
- Cost of Goods Sold
- Operating expenses by department
- EBITDA, Operating Income, Net Income
- Year-over-year growth metrics
- Key performance indicators
- Use realistic numbers (2024 = $42M, scale backwards for previous years)
- Format in Markdown with tables and charts data (as code blocks for visualization)
- Include executive summary with key insights
"""

            if self.use_ai:
                try:
                    prompt = f"""Generate a comprehensive annual Profit & Loss statement in Markdown format.

{context}

Requirements:
- Professional financial document format
- Use Markdown tables for all financial data
- Include sections: Executive Summary, Revenue Analysis, Cost Analysis, Profitability Metrics, YoY Comparison
- Add chart data as code blocks (e.g., for bar charts, line charts)
- 1000-1500 words
- Realistic financial metrics and analysis
- Professional financial terminology

Generate ONLY Markdown content (no HTML, no other formats)."""

                    response = self.llm.invoke(prompt)
                    content = response.content.strip()
                except Exception as e:
                    print(f"   ⚠️  AI generation failed: {e}")
                    content = f"# P&L Statement - {year}\n\nContent generation failed."
            else:
                content = f"# P&L Statement - {year}\n\nAI generation not available."

            filename = f"PL-Statement-{year}.md"
            filepath = os.path.join(self.data_dir, "unstructured/financial", filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            self._print_progress_bar(i + 1, num_statements, "Generating P&L statements")

        print(f"  ✓ Generated {num_statements} P&L statements")

    # ===== MARKETING DATA =====

    def generate_campaigns(self, num_campaigns=50):
        """Generate marketing campaign data"""
        print(
            f"[{self._get_timestamp()}] Generating {num_campaigns} marketing campaigns..."
        )

        campaign_types = [
            "Email",
            "Social Media",
            "Trade Show",
            "Webinar",
            "Content Marketing",
            "PPC",
            "Direct Mail",
        ]
        target_audiences = [
            "Manufacturing Companies",
            "Automotive Industry",
            "Electronics Assembly",
            "Warehousing & Logistics",
            "Food & Beverage",
            "System Integrators",
            "SMB Manufacturers",
            "Enterprise Manufacturers",
        ]
        statuses = ["Planned", "Active", "Completed", "On Hold"]

        campaigns = []

        for i in range(num_campaigns):
            start_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 700))
            duration = random.randint(30, 180)
            end_date = start_date + timedelta(days=duration)

            budget = random.randint(5000, 100000)
            # ROI between -20% to 300%
            roi = random.uniform(-0.2, 3.0)
            revenue = budget * (1 + roi)

            leads = random.randint(50, 5000)
            conversions = int(leads * random.uniform(0.01, 0.15))

            campaign = {
                "campaign_id": f"CAMP-{2024}{str(i+1).zfill(3)}",
                "campaign_name": f"{random.choice(campaign_types)} - {random.choice(['Q1', 'Q2', 'Q3', 'Q4'])} {random.choice([2023, 2024])}",
                "campaign_type": random.choice(campaign_types),
                "target_audience": random.choice(target_audiences),
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "budget": round(budget, 2),
                "actual_spend": round(budget * random.uniform(0.85, 1.05), 2),
                "leads_generated": leads,
                "conversions": conversions,
                "conversion_rate": (
                    round(conversions / leads * 100, 2) if leads > 0 else 0
                ),
                "revenue_generated": round(revenue, 2),
                "roi": round(roi * 100, 2),
                "status": random.choice(statuses),
                "owner": random.choice(
                    [e["name"] for e in EMPLOYEES if "Marketing" in e["dept"]]
                ),
                "notes": random.choice(
                    [
                        "Exceeded expectations",
                        "Need to optimize messaging",
                        "Strong engagement metrics",
                        "Budget increased mid-campaign",
                        "",
                    ]
                ),
            }
            campaigns.append(campaign)

            if (i + 1) % 10 == 0:
                self._print_progress_bar(i + 1, num_campaigns, "Generating campaigns")

        self._print_progress_bar(num_campaigns, num_campaigns, "Generating campaigns")

        # Export to CSV and JSON
        self._export_to_csv_json(campaigns, "marketing_campaigns")
        print(f"  ✓ Generated {len(campaigns)} marketing campaigns")
        return campaigns

    def generate_customer_feedback_forms(self, num_forms=3):
        """Generate customer feedback survey templates in HTML"""
        print(
            f"[{self._get_timestamp()}] Generating {num_forms} customer feedback forms..."
        )

        os.makedirs(
            os.path.join(self.data_dir, "html_documents/marketing"), exist_ok=True
        )

        survey_types = [
            "Product Satisfaction Survey",
            "Customer Service Experience Survey",
            "Post-Purchase Feedback Form",
        ]

        for i, survey_type in enumerate(survey_types[:num_forms]):
            context = f"""
Company: {COMPANY['name']}
Industry: {COMPANY['industry']}
Products: Industrial robots, collaborative robots, mobile robots, automation software

Generate a {survey_type} HTML form with:
- Professional survey design
- 10-15 questions (mix of rating scales, multiple choice, and open-ended)
- Include sample responses (2-3 examples showing variety of feedback)
- Questions about product quality, service, likelihood to recommend, etc.
- Use proper HTML form elements (input, select, textarea, etc.)
- Include a results summary section showing sample aggregate data
- Make it realistic and comprehensive for a robotics company
"""

            content = self._generate_ai_content(survey_type, context, "600-1000")

            doc = {
                "title": survey_type,
                "category": "Marketing",
                "type": "Survey Template",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "author": "Chris Patel, Marketing Manager",
                "content": content,
            }

            self.generated_docs.append(doc)
            self._save_html_document(doc, "marketing")

            self._print_progress_bar(i + 1, num_forms, "Generating feedback forms")

        print(f"  ✓ Generated {num_forms} customer feedback forms")

    def generate_lead_tracking_reports(self, num_reports=10):
        """Generate lead tracking reports in Markdown"""
        print(
            f"[{self._get_timestamp()}] Generating {num_reports} lead tracking reports..."
        )

        os.makedirs(
            os.path.join(self.data_dir, "unstructured/marketing"), exist_ok=True
        )

        channels = [
            "Website",
            "Trade Shows",
            "Email Campaigns",
            "Social Media",
            "Referrals",
            "Direct Sales",
            "Webinars",
            "Content Downloads",
        ]

        for i in range(num_reports):
            month = (datetime.now() - timedelta(days=30 * i)).strftime("%B %Y")
            channel = channels[i % len(channels)]

            context = f"""
Company: {COMPANY['name']}
Industry: {COMPANY['industry']}
Report: Lead Tracking Report - {channel} - {month}

Generate a lead tracking report showing:
- Lead volume from {channel}
- Lead quality metrics (MQL, SQL conversion rates)
- Source breakdown
- Geographic distribution
- Industry breakdown
- Conversion rates through the funnel
- Top performing campaigns/tactics
- Recommendations for optimization
- Use realistic metrics for a robotics B2B company
- Include markdown tables with data
- Show trends and insights
"""

            if self.use_ai:
                try:
                    prompt = f"""Generate a comprehensive lead tracking report in Markdown format.

{context}

Requirements:
- Professional marketing analytics format
- Use Markdown tables for all metrics
- Include sections: Executive Summary, Lead Volume Analysis, Conversion Metrics, Channel Performance, Recommendations
- 800-1200 words
- Realistic B2B marketing metrics
- Data-driven insights

Generate ONLY Markdown content."""

                    response = self.llm.invoke(prompt)
                    content = response.content.strip()
                except Exception as e:
                    print(f"   ⚠️  AI generation failed: {e}")
                    content = f"# Lead Tracking Report - {channel} - {month}\n\nContent generation failed."
            else:
                content = f"# Lead Tracking Report - {channel} - {month}\n\nAI generation not available."

            filename = f"Lead-Tracking-{channel.replace(' ', '-')}-{month.replace(' ', '-')}.md"
            filepath = os.path.join(self.data_dir, "unstructured/marketing", filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            self._print_progress_bar(
                i + 1, num_reports, "Generating lead tracking reports"
            )

        print(f"  ✓ Generated {num_reports} lead tracking reports")

    # ===== UTILITY METHODS =====

    def _export_to_csv_json(self, data, filename):
        """Export data to both CSV and JSON"""
        if not data:
            return

        # Export to JSON
        json_path = os.path.join(self.data_dir, f"{filename}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        # Export to CSV
        csv_path = os.path.join(self.data_dir, f"{filename}.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def _save_html_document(self, doc, category):
        """Save HTML document to file"""
        filename = doc["title"].lower().replace(" ", "-").replace("&", "and") + ".html"
        filepath = os.path.join(self.data_dir, f"html_documents/{category}", filename)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{doc['title']} - Robotix</title>
</head>
<body>
    <h1>{doc['title']}</h1>
    <p><strong>Category:</strong> {doc['category']} | <strong>Type:</strong> {doc['type']} | <strong>Date:</strong> {doc['date']} | <strong>Author:</strong> {doc['author']}</p>
    <hr>
    {doc['content']}
</body>
</html>"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)


def main():
    """Main execution function"""
    print("=" * 70)
    print("Financial & Marketing Data Generator".center(70))
    print("=" * 70)
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Determine data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(project_dir, "data")

    gen = FinancialMarketingGenerator(data_dir=data_dir)

    overall_start = time.time()

    try:
        # Generate Financial Data
        print("\n" + "=" * 70)
        print("💰 GENERATING FINANCIAL DATA".center(70))
        print("=" * 70)
        invoices = gen.generate_invoices(200)
        gen.generate_budget_reports(5)
        gen.generate_pl_statements(3)

        # Generate Marketing Data
        print("\n" + "=" * 70)
        print("📢 GENERATING MARKETING DATA".center(70))
        print("=" * 70)
        campaigns = gen.generate_campaigns(50)
        gen.generate_customer_feedback_forms(3)
        gen.generate_lead_tracking_reports(10)

        # Summary
        total_time = time.time() - overall_start
        print("\n" + "=" * 70)
        print("✅ GENERATION COMPLETE".center(70))
        print("=" * 70)
        print(f"⏰ Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Total Time: {total_time:.1f} seconds")
        print()
        print("📊 Generated Files:")
        print(f"   - Invoices: 200 records (CSV/JSON)")
        print(f"   - Budget Reports: 5 HTML documents")
        print(f"   - P&L Statements: 3 Markdown files")
        print(f"   - Marketing Campaigns: 50 records (CSV/JSON)")
        print(f"   - Customer Feedback Forms: 3 HTML documents")
        print(f"   - Lead Tracking Reports: 10 Markdown files")
        print("\n" + "=" * 70)

        return 0

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys

    sys.exit(main())
