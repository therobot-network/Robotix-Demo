#!/usr/bin/env python3
"""
Script to analyze CSV files using the Grok API and generate analytical reports.

This script:
1. Finds all CSV files in the dev-65f70496-*-csv folders
2. Reads each CSV file and sends it to Grok API for analysis
3. Generates analytical reports with key features, sums, totals, and summaries
4. Saves the reports as markdown files
"""

import os
import pandas as pd
import requests
import json
from pathlib import Path
import argparse
from datetime import datetime
import time
from dotenv import load_dotenv


class GrokCSVAnalyzer:
    def __init__(self, api_key, data_dir):
        self.api_key = api_key
        self.data_dir = Path(data_dir)
        self.grok_api_url = "https://api.x.ai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.reports_dir = self.data_dir / "grok_analysis_reports"
        self.reports_dir.mkdir(exist_ok=True)

    def find_csv_folders(self):
        """Find all dev-65f70496-*-csv folders."""
        csv_folders = []
        for item in self.data_dir.iterdir():
            if (
                item.is_dir()
                and item.name.startswith("dev-65f70496-")
                and item.name.endswith("-csv")
            ):
                csv_folders.append(item)
        return sorted(csv_folders)

    def read_csv_with_preview(self, csv_path, max_rows=50):
        """Read CSV file and create a preview for analysis."""
        try:
            df = pd.read_csv(csv_path)

            # Get basic info
            info = {
                "filename": csv_path.name,
                "total_rows": len(df),
                "total_columns": len(df.columns),
                "columns": df.columns.tolist(),
                "dtypes": df.dtypes.to_dict(),
                "memory_usage": df.memory_usage(deep=True).sum(),
            }

            # Get preview data (first few rows)
            preview_df = df.head(max_rows)

            # Get basic statistics for numeric columns
            numeric_stats = {}
            for col in df.select_dtypes(include=["number"]).columns:
                numeric_stats[col] = {
                    "min": float(df[col].min()) if not pd.isna(df[col].min()) else None,
                    "max": float(df[col].max()) if not pd.isna(df[col].max()) else None,
                    "mean": (
                        float(df[col].mean()) if not pd.isna(df[col].mean()) else None
                    ),
                    "sum": float(df[col].sum()) if not pd.isna(df[col].sum()) else None,
                    "count": int(df[col].count()),
                    "null_count": int(df[col].isnull().sum()),
                }

            # Get value counts for categorical columns (top 10)
            categorical_info = {}
            for col in df.select_dtypes(include=["object"]).columns:
                value_counts = df[col].value_counts().head(10)
                categorical_info[col] = {
                    "unique_count": int(df[col].nunique()),
                    "null_count": int(df[col].isnull().sum()),
                    "top_values": value_counts.to_dict(),
                }

            return {
                "info": info,
                "preview_data": preview_df.to_dict("records"),
                "numeric_stats": numeric_stats,
                "categorical_info": categorical_info,
            }

        except Exception as e:
            print(f"❌ Error reading CSV {csv_path}: {e}")
            return None

    def create_analysis_prompt(self, csv_data):
        """Create a detailed prompt for Grok analysis."""
        prompt = f"""
Please analyze this CSV dataset and provide a comprehensive analytical report. Here's the dataset information:

**Dataset Overview:**
- Filename: {csv_data['info']['filename']}
- Total Rows: {csv_data['info']['total_rows']:,}
- Total Columns: {csv_data['info']['total_columns']}
- Columns: {', '.join(csv_data['info']['columns'])}

**Numeric Statistics:**
{json.dumps(csv_data['numeric_stats'], indent=2) if csv_data['numeric_stats'] else 'No numeric columns found'}

**Categorical Data Info:**
{json.dumps(csv_data['categorical_info'], indent=2) if csv_data['categorical_info'] else 'No categorical columns found'}

**Sample Data (first few rows):**
{json.dumps(csv_data['preview_data'][:5], indent=2)}

Please provide a detailed analytical report in markdown format with the following sections:

# {csv_data['info']['filename']} - Analytical Report

## Dataset Summary
• Brief description of what this dataset represents
• Key metrics (total records, date range if applicable, etc.)

## Key Financial/Business Metrics
• Important totals, sums, and aggregations
• Revenue, costs, quantities, or other business-relevant calculations
• Percentage breakdowns where relevant

## Data Quality Assessment
• Missing data analysis
• Data completeness
• Any potential data quality issues

## Key Insights & Trends
• Notable patterns in the data
• Top performers (customers, products, etc.)
• Distribution analysis
• Time-based trends (if date columns exist)

## Statistical Highlights
• Mean, median, ranges for key numeric fields
• Outliers or unusual values
• Correlation insights (if multiple numeric fields)

## Business Recommendations
• Actionable insights based on the analysis
• Areas that might need attention
• Opportunities identified

Please make the analysis business-focused and provide specific numbers, percentages, and actionable insights. Use bullet points for easy readability.
"""
        return prompt

    def call_grok_api(self, prompt):
        """Call the Grok API to analyze the CSV data."""
        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a skilled data analyst with expertise in business intelligence and CSV data analysis. Provide detailed, actionable insights with specific numbers and clear business value.",
                },
                {"role": "user", "content": prompt},
            ],
            "model": "grok-4-fast-reasoning",
            "stream": False,
            "temperature": 0.1,
        }

        try:
            response = requests.post(
                self.grok_api_url, headers=self.headers, json=payload, timeout=60
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Grok API Error: {response.status_code}")
                print(f"Response: {response.text}")
                return None

        except Exception as e:
            print(f"❌ Error calling Grok API: {e}")
            return None

    def save_report(self, folder_name, csv_filename, report_content):
        """Save the analysis report to a markdown file."""
        report_filename = (
            f"{folder_name}_{csv_filename.replace('.csv', '')}_analysis.md"
        )
        report_path = self.reports_dir / report_filename

        # Add metadata header
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"""---
Generated: {timestamp}
Source CSV: {csv_filename}
Source Folder: {folder_name}
Analyzer: Grok API
---

"""

        try:
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(header + report_content)
            print(f"    ✅ Report saved: {report_filename}")
            return report_path
        except Exception as e:
            print(f"    ❌ Error saving report: {e}")
            return None

    def analyze_csv_file(self, csv_path, folder_name):
        """Analyze a single CSV file."""
        print(f"  📊 Analyzing: {csv_path.name}")

        # Read and prepare CSV data
        csv_data = self.read_csv_with_preview(csv_path)
        if not csv_data:
            return None

        # Create analysis prompt
        prompt = self.create_analysis_prompt(csv_data)

        # Call Grok API
        print(f"    🤖 Calling Grok API...")
        response = self.call_grok_api(prompt)

        if not response:
            return None

        # Extract the analysis content
        try:
            analysis_content = response["choices"][0]["message"]["content"]

            # Save the report
            report_path = self.save_report(folder_name, csv_path.name, analysis_content)
            return report_path

        except Exception as e:
            print(f"    ❌ Error processing Grok response: {e}")
            return None

    def analyze_all_csv_files(self, delay_between_calls=2):
        """Analyze all CSV files in the dev-prefixed folders."""
        csv_folders = self.find_csv_folders()

        if not csv_folders:
            print("❌ No CSV folders found!")
            return

        print(f"🚀 Starting analysis of CSV files from {len(csv_folders)} folders...")
        print(f"📂 Reports will be saved to: {self.reports_dir}")

        total_files_analyzed = 0
        total_reports_generated = 0

        for folder in csv_folders:
            print(f"\n📁 Processing folder: {folder.name}")

            # Find all CSV files in the folder
            csv_files = list(folder.glob("*.csv"))

            if not csv_files:
                print("  ⚠️  No CSV files found in this folder")
                continue

            print(f"  🔍 Found {len(csv_files)} CSV file(s)")

            for csv_file in csv_files:
                total_files_analyzed += 1

                # Analyze the CSV file
                report_path = self.analyze_csv_file(csv_file, folder.name)

                if report_path:
                    total_reports_generated += 1

                # Add delay between API calls to avoid rate limiting
                if delay_between_calls > 0:
                    time.sleep(delay_between_calls)

        print(f"\n✅ Analysis complete!")
        print(f"📊 Files analyzed: {total_files_analyzed}")
        print(f"📄 Reports generated: {total_reports_generated}")
        print(f"📁 Reports saved to: {self.reports_dir}")


def main():
    # Load environment variables from .env file
    load_dotenv()

    parser = argparse.ArgumentParser(description="Analyze CSV files using Grok API")
    parser.add_argument(
        "--api-key", help="Grok API key (or set XAI_API_KEY environment variable)"
    )
    parser.add_argument(
        "--data-dir",
        default="/Users/joeyguedalia/Desktop/Work/Robotix-Demo/data",
        help="Path to the data directory",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=2,
        help="Delay between API calls in seconds (default: 2)",
    )

    args = parser.parse_args()

    # Get API key - try XAI_API_KEY first, then GROK_API_KEY for backward compatibility
    api_key = args.api_key or os.getenv("XAI_API_KEY") or os.getenv("GROK_API_KEY")
    if not api_key:
        print("❌ Error: Grok API key required!")
        print("   Set it via --api-key argument or XAI_API_KEY environment variable")
        return

    # Initialize analyzer
    analyzer = GrokCSVAnalyzer(api_key, args.data_dir)

    # Run analysis
    analyzer.analyze_all_csv_files(delay_between_calls=args.delay)


if __name__ == "__main__":
    main()
