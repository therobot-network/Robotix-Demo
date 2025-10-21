#!/usr/bin/env python3
"""
Additional Documents Generator
Generates supplementary documents to boost Tier 1 completeness:
- NPS trends from surveys (Marketing)
- Inventory turnover memos (Finance)

AI-FIRST approach for Robotix robotics company
"""

import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from company_data import COMPANY, EMPLOYEES

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


class AdditionalDocumentsGenerator:

    def __init__(self, data_dir="../data", use_ai=True):
        self.data_dir = data_dir
        self.use_ai = use_ai and AI_AVAILABLE
        self.generated_docs = []

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

    def _generate_ai_content(self, doc_type, context, word_count="800-1200"):
        """Generate content using AI"""
        if not self.use_ai:
            return f"# {doc_type}\n\nAI generation not available. {doc_type} content would go here."

        try:
            prompt = f"""Generate a comprehensive, realistic {doc_type} document for Robotix.

Company Context:
{context}

Requirements:
- Professional business tone appropriate for {doc_type}
- Realistic, specific details, metrics, and data
- Well-structured with clear sections
- {word_count} words
- Include concrete examples and actionable information
- Use Markdown formatting with tables where appropriate
- Make it feel authentic and comprehensive for a robotics company

Generate ONLY Markdown content (no HTML, no other formats)."""

            response = self.llm.invoke(prompt)
            content = response.content.strip()
            return content
        except Exception as e:
            print(f"   ⚠️  AI generation failed for {doc_type}: {str(e)}")
            return f"# {doc_type}\n\nContent generation failed. {doc_type} content would go here."

    def _file_exists(self, filepath):
        """Check if a file already exists"""
        return os.path.exists(filepath)

    # ===== MARKETING DOCUMENTS =====

    def generate_nps_trend_reports(self, num_reports=4):
        """Generate NPS trends from customer surveys"""
        print(
            f"[{self._get_timestamp()}] Generating {num_reports} NPS trend reports..."
        )

        output_dir = os.path.join(self.data_dir, "sales-marketing/memos")
        os.makedirs(output_dir, exist_ok=True)

        quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
        marketing_manager = next(
            (e for e in EMPLOYEES if "Marketing Manager" in e["title"]), EMPLOYEES[0]
        )

        generated_count = 0

        for i, quarter in enumerate(quarters[:num_reports]):
            filename = (
                f"NPS-Trends-and-Customer-Satisfaction---{quarter.replace(' ', '-')}.md"
            )
            filepath = os.path.join(output_dir, filename)

            # Skip if already exists
            if self._file_exists(filepath):
                print(f"  ⊘ Skipping {filename} (already exists)")
                continue

            # Determine NPS trend direction
            base_nps = 45 + (i * 3)  # Increasing trend
            previous_nps = base_nps - 3 if i > 0 else 42

            context = f"""
Company: {COMPANY['name']}
Industry: {COMPANY['industry']}
Revenue: {COMPANY['revenue']}
Report Period: {quarter}
Author: {marketing_manager['name']}, {marketing_manager['title']}

Generate a comprehensive NPS (Net Promoter Score) trends and customer satisfaction report for {quarter} showing:

Executive Summary:
- Overall NPS score: {base_nps} (up from {previous_nps} in previous quarter)
- Survey response rate and sample size (500-800 customer responses)
- Key drivers of satisfaction and dissatisfaction
- Strategic recommendations

Detailed Metrics:
- NPS breakdown by customer segment (Enterprise vs SMB)
- NPS by product category (Industrial Robots, Collaborative Robots, Mobile Robots, Software)
- NPS by customer lifecycle stage (new customers, existing, long-term)
- Promoters, Passives, Detractors percentages and counts
- Comparison to industry benchmark (industry average ~40 for B2B robotics)

Survey Methodology:
- Survey distribution method (post-purchase, quarterly check-ins, support ticket closure)
- Response rates by segment
- Survey questions (likelihood to recommend 0-10 scale, reasons, improvements)

Satisfaction Drivers Analysis:
- Top positive factors: product quality, reliability, customer support, ease of integration
- Top negative factors: pricing concerns, delivery times, software complexity, training needs
- Specific customer feedback quotes (anonymized)
- Service touchpoint ratings (sales process, implementation, support, documentation)

Trends and Insights:
- Quarter-over-quarter changes
- Correlation between NPS and customer behavior (repeat purchases, referrals)
- Industry-specific satisfaction patterns (automotive vs logistics vs manufacturing)
- Impact of recent initiatives (improved support response times, new training programs)

Customer Verbatim Feedback:
- Include 5-8 representative customer quotes showing variety of sentiment
- Themes from open-ended responses
- Feature requests and improvement suggestions

Action Items and Recommendations:
- Initiatives to convert Passives to Promoters
- Address specific Detractor concerns
- Product improvement priorities based on feedback
- Process improvements for customer experience
- Training and documentation enhancements

Competitive Context:
- How our NPS compares to key competitors
- Market positioning based on customer sentiment

Use realistic B2B robotics metrics, include markdown tables with data, and show data-driven insights.
"""

            content = self._generate_ai_content(
                f"NPS Trends Report - {quarter}", context, "1200-1500"
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            generated_count += 1
            self.generated_docs.append(
                {
                    "type": "NPS Trends Report",
                    "quarter": quarter,
                    "filename": filename,
                    "path": filepath,
                }
            )

            self._print_progress_bar(i + 1, num_reports, "Generating NPS reports")

        print(
            f"  ✓ Generated {generated_count} new NPS trend reports (skipped {num_reports - generated_count} existing)"
        )
        return generated_count

    # ===== FINANCE DOCUMENTS =====

    def generate_inventory_turnover_memos(self, num_memos=4):
        """Generate inventory turnover analysis memos"""
        print(
            f"[{self._get_timestamp()}] Generating {num_memos} inventory turnover memos..."
        )

        output_dir = os.path.join(self.data_dir, "finance/memos")
        os.makedirs(output_dir, exist_ok=True)

        quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
        cfo = next(
            (
                e
                for e in EMPLOYEES
                if "CFO" in e["title"] or "Chief Financial Officer" in e["title"]
            ),
            EMPLOYEES[0],
        )

        generated_count = 0

        for i, quarter in enumerate(quarters[:num_memos]):
            filename = f"Inventory-Turnover-Analysis---{quarter.replace(' ', '-')}.md"
            filepath = os.path.join(output_dir, filename)

            # Skip if already exists
            if self._file_exists(filepath):
                print(f"  ⊘ Skipping {filename} (already exists)")
                continue

            # Determine turnover metrics
            turnover_ratio = round(3.2 + (i * 0.15), 2)  # Improving trend
            days_inventory = round(365 / turnover_ratio, 1)

            context = f"""
Company: {COMPANY['name']}
Industry: {COMPANY['industry']}
Revenue: {COMPANY['revenue']}
Report Period: {quarter}
Author: {cfo['name']}, {cfo['title']}

Generate a comprehensive inventory turnover analysis memo for {quarter} showing:

Executive Summary:
- Overall inventory turnover ratio: {turnover_ratio}x (industry benchmark: 3.5-4.0x for robotics)
- Days inventory outstanding (DIO): {days_inventory} days
- Total inventory value: $6-8M across all categories
- Key insights and recommendations
- Working capital impact

Inventory Turnover by Category:
- Industrial Robots: turnover, average inventory value, DOI
- Collaborative Robots: turnover, average inventory value, DOI
- Mobile Robots: turnover, average inventory value, DOI
- Components & Accessories: turnover, average inventory value, DOI
- Software licenses: N/A (digital products)

Detailed Analysis:
- Raw materials inventory (motors, controllers, sensors, frames): turnover and value
- Work-in-progress (WIP) inventory: assembly stage, value, aging
- Finished goods inventory: ready for shipment, value by product line
- Slow-moving inventory identification (items >180 days)
- Fast-moving products (high turnover items)

Inventory Metrics:
- Beginning inventory value
- Purchases/production additions
- Cost of goods sold (COGS)
- Ending inventory value
- Average inventory calculation
- Turnover ratio calculation methodology

Location Analysis:
- Minneapolis Manufacturing Facility: inventory levels and turnover
- Portland Distribution Center: inventory levels and turnover
- Inter-location transfers and optimization opportunities

Quarter-over-Quarter Comparison:
- Trend analysis vs previous quarters
- Seasonal patterns (Q4 typically higher due to year-end purchasing)
- Impact of new product launches on inventory levels
- Supply chain improvements or challenges

Cash Flow Impact:
- Cash tied up in inventory
- Working capital efficiency
- Comparison to accounts receivable days (DSO)
- Cash conversion cycle analysis
- Impact on company liquidity

Risk Factors:
- Obsolescence risk (technology changes, product updates)
- Overstocking vs stockout risk balance
- Supply chain disruption considerations
- Customer demand forecast accuracy

Recommendations:
- Inventory optimization opportunities
- Reduce slow-moving inventory (clearance sales, bundling)
- Improve demand forecasting
- Vendor lead time negotiations
- Just-in-time (JIT) opportunities for certain components
- Target turnover ratio for next quarter
- Working capital release potential

Action Items:
- Specific product lines requiring attention
- Process improvements for inventory management
- System enhancements for better tracking
- Cross-functional coordination with sales, production, procurement

Include realistic financial metrics, markdown tables with detailed data, and CFO-level strategic analysis.
"""

            content = self._generate_ai_content(
                f"Inventory Turnover Analysis - {quarter}", context, "1200-1500"
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            generated_count += 1
            self.generated_docs.append(
                {
                    "type": "Inventory Turnover Memo",
                    "quarter": quarter,
                    "filename": filename,
                    "path": filepath,
                }
            )

            self._print_progress_bar(i + 1, num_memos, "Generating inventory memos")

        print(
            f"  ✓ Generated {generated_count} new inventory turnover memos (skipped {num_memos - generated_count} existing)"
        )
        return generated_count

    def get_summary(self):
        """Return summary of generated documents"""
        return {
            "total_generated": len(self.generated_docs),
            "by_type": {
                "NPS Trends Reports": len(
                    [d for d in self.generated_docs if d["type"] == "NPS Trends Report"]
                ),
                "Inventory Turnover Memos": len(
                    [
                        d
                        for d in self.generated_docs
                        if d["type"] == "Inventory Turnover Memo"
                    ]
                ),
            },
            "documents": self.generated_docs,
        }


def main():
    """Main execution function"""
    print("=" * 70)
    print("Additional Documents Generator".center(70))
    print("=" * 70)
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Determine data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(project_dir, "data")

    gen = AdditionalDocumentsGenerator(data_dir=data_dir)

    overall_start = time.time()

    try:
        # Generate Marketing Documents
        print("\n" + "=" * 70)
        print("📊 GENERATING MARKETING DOCUMENTS".center(70))
        print("=" * 70)
        nps_count = gen.generate_nps_trend_reports(4)

        # Generate Finance Documents
        print("\n" + "=" * 70)
        print("💰 GENERATING FINANCE DOCUMENTS".center(70))
        print("=" * 70)
        inventory_count = gen.generate_inventory_turnover_memos(4)

        # Summary
        total_time = time.time() - overall_start
        summary = gen.get_summary()

        print("\n" + "=" * 70)
        print("✅ GENERATION COMPLETE".center(70))
        print("=" * 70)
        print(f"⏰ Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Total Time: {total_time:.1f} seconds")
        print()
        print("📊 Generated Files:")
        print(
            f"   - NPS Trends Reports: {summary['by_type']['NPS Trends Reports']} new documents"
        )
        print(
            f"   - Inventory Turnover Memos: {summary['by_type']['Inventory Turnover Memos']} new documents"
        )
        print(f"   - Total New Documents: {summary['total_generated']}")
        print()
        print("📁 File Locations:")
        print(f"   - Marketing: data/sales-marketing/memos/")
        print(f"   - Finance: data/finance/memos/")
        print("\n" + "=" * 70)
        print("🎯 Tier 1 Completeness Impact")
        print("=" * 70)
        print("   - Added NPS trends from surveys to Marketing")
        print("   - Added Inventory turnover analysis to Finance")
        print("   - Expected boost to Tier 1 completeness: ~90%")
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
