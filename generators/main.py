#!/usr/bin/env python3
"""
Robotix Synthetic Data Generator
Main orchestration script - AI-FIRST approach

This script generates:
1. Structured data (CSV/JSON): employees, products, customers, sales, orders
2. Unstructured data (Markdown): memos, meeting notes, project docs - ALL AI-GENERATED
3. HTML documents (HR, Product specs, Legal) - ALL AI-GENERATED

All content generated using Claude AI for maximum realism and diversity.
Website can be built manually using the generated documents and data.
"""

import sys
import os
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from document_generator import DocumentGenerator
from structured_data_generator import StructuredDataGenerator
from unstructured_data_generator import UnstructuredDataGenerator
from company_data import COMPANY, PRODUCT_CATEGORIES

# Load environment variables from .env file
load_dotenv()


def get_timestamp():
    """Get formatted timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_progress_bar(current, total, label="Progress", width=40):
    """Print a progress bar"""
    percent = current / total
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)
    print(f"   {label}: [{bar}] {int(percent * 100)}% ({current}/{total})", end="\r")
    if current == total:
        print()  # New line when complete


def print_section_header(title, start=True):
    """Print a section header with timestamp"""
    timestamp = get_timestamp()
    if start:
        print(f"\n{'=' * 70}")
        print(f"{title}".center(70))
        print(f"{'=' * 70}")
        print(f"⏰ Started: {timestamp}\n")
    else:
        print(f"\n⏰ Completed: {timestamp}")


def print_header():
    """Print script header"""
    print("=" * 70)
    print(f"Robotix Enterprise Data Generator".center(70))
    print("=" * 70)
    print(f"⏰ Started: {get_timestamp()}")
    print(f"\nCompany: {COMPANY['name']}")
    print(f"Industry: {COMPANY['industry']}")
    print(f"Employees: {COMPANY['employees']}")
    print("\n📊 Structured Data + 📝 Unstructured Data + 📄 HTML Documents")
    print("=" * 70)
    print()


def generate_structured_data():
    """Generate all structured datasets (CSV/JSON)"""
    print_section_header("📊 GENERATING STRUCTURED DATA")
    start_time = time.time()

    # Determine output directory - use project's data folder
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(project_dir, "data")

    gen = StructuredDataGenerator(output_dir=data_dir)

    # Track progress
    total_steps = 5
    current_step = 0

    print(f"[{get_timestamp()}] Generating employee data...")
    gen.generate_employee_data()
    current_step += 1
    print_progress_bar(current_step, total_steps, "Overall Progress")
    print(f"  ✓ {len(gen.data['employees'])} employees\n")

    print(f"[{get_timestamp()}] Generating product catalog...")
    gen.generate_product_data()
    current_step += 1
    print_progress_bar(current_step, total_steps, "Overall Progress")
    print(
        f"  ✓ {len(gen.data['products'])} products across {len(PRODUCT_CATEGORIES)} categories\n"
    )

    print(f"[{get_timestamp()}] Generating customer data...")
    gen.generate_customer_data(num_customers=500)
    current_step += 1
    print_progress_bar(current_step, total_steps, "Overall Progress")
    print(f"  ✓ {len(gen.data['customers'])} customers\n")

    print(f"[{get_timestamp()}] Generating sales and order data...")
    orders, order_items = gen.generate_sales_data(num_orders=1000)
    current_step += 1
    print_progress_bar(current_step, total_steps, "Overall Progress")
    print(f"  ✓ {len(orders)} orders with {len(order_items)} line items\n")

    print(f"[{get_timestamp()}] Generating support tickets...")
    gen.generate_support_tickets(num_tickets=200)
    current_step += 1
    print_progress_bar(current_step, total_steps, "Overall Progress")
    print(f"  ✓ {len(gen.data['support_tickets'])} support tickets\n")

    # Export all data
    print(f"[{get_timestamp()}] Exporting data to CSV and JSON...")
    gen.export_all()

    elapsed = time.time() - start_time
    print_section_header(
        f"📊 STRUCTURED DATA COMPLETE (took {elapsed:.1f}s)", start=False
    )

    return gen.data, data_dir


def generate_unstructured_data():
    """Generate unstructured content (markdown files)"""
    print_section_header("📝 GENERATING UNSTRUCTURED DATA")
    start_time = time.time()

    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    unstructured_dir = os.path.join(project_dir, "data", "unstructured")

    gen = UnstructuredDataGenerator(output_dir=unstructured_dir)
    content = gen.generate_all()

    elapsed = time.time() - start_time
    print_section_header(
        f"📝 UNSTRUCTURED DATA COMPLETE (took {elapsed:.1f}s)", start=False
    )

    return content, unstructured_dir


def generate_html_documents():
    """Generate HTML documents (HR, Product, Legal)"""
    print_section_header("📄 GENERATING HTML DOCUMENTS")
    start_time = time.time()

    gen = DocumentGenerator()

    # Calculate total documents to generate
    total_hr = 3
    total_product_specs = sum(len(products) for products in PRODUCT_CATEGORIES.values())
    robot_categories = ["Industrial Robots", "Collaborative Robots", "Mobile Robots"]
    total_user_guides = sum(len(PRODUCT_CATEGORIES[cat]) for cat in robot_categories)
    total_legal = 2
    total_docs = total_hr + total_product_specs + total_user_guides + total_legal
    current_doc = 0

    # Generate HR documents
    print(f"[{get_timestamp()}] Generating HR Documents...")
    gen.generate_employee_handbook()
    current_doc += 1
    print_progress_bar(current_doc, total_docs, "Document Progress")
    print(f"  ✓ Employee Handbook\n")

    gen.generate_remote_work_policy()
    current_doc += 1
    print_progress_bar(current_doc, total_docs, "Document Progress")
    print(f"  ✓ Remote Work Policy\n")

    gen.generate_benefits_overview()
    current_doc += 1
    print_progress_bar(current_doc, total_docs, "Document Progress")
    print(f"  ✓ Benefits Overview\n")

    # Generate Product documents - NOW FOR ALL PRODUCTS
    print(f"[{get_timestamp()}] Generating Product Technical Specifications...")

    # Track all products we document
    documented_products = []

    for category, product_list in PRODUCT_CATEGORIES.items():
        for product_name in product_list:
            # Generate spec for every product
            gen.generate_product_spec(product_name, category)
            documented_products.append(product_name)
            current_doc += 1
            print_progress_bar(current_doc, total_docs, "Document Progress")
            print(f"  ✓ {product_name} - Technical Spec")

    print(f"\n[{get_timestamp()}] Generating Product User Guides...")
    # Generate user guides for robots only (software/components don't need full guides)
    for category in robot_categories:
        for product_name in PRODUCT_CATEGORIES[category]:
            gen.generate_product_user_guide(product_name)
            current_doc += 1
            print_progress_bar(current_doc, total_docs, "Document Progress")
            print(f"  ✓ {product_name} - User Guide")

    # Generate Legal documents
    print(f"\n[{get_timestamp()}] Generating Legal Documents...")
    gen.generate_privacy_policy()
    current_doc += 1
    print_progress_bar(current_doc, total_docs, "Document Progress")
    print(f"  ✓ Privacy Policy\n")

    gen.generate_warranty_policy()
    current_doc += 1
    print_progress_bar(current_doc, total_docs, "Document Progress")
    print(f"  ✓ Warranty and Return Policy\n")

    documents = gen.get_all_documents()
    print(f"\n✅ Total HTML documents generated: {len(documents)}")

    elapsed = time.time() - start_time
    print_section_header(
        f"📄 HTML DOCUMENTS COMPLETE (took {elapsed:.1f}s)", start=False
    )

    return documents


def save_html_documents(documents):
    """Save HTML documents to data folder"""
    print_section_header("💾 SAVING HTML DOCUMENTS")
    start_time = time.time()

    # Save documents in project's data folder
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(project_dir, "data", "html_documents")

    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(f"{docs_dir}/hr", exist_ok=True)
    os.makedirs(f"{docs_dir}/product", exist_ok=True)
    os.makedirs(f"{docs_dir}/legal", exist_ok=True)

    total_docs = len(documents)
    for idx, doc in enumerate(documents, 1):
        category_path = doc["category"].lower()
        filename = doc["title"].lower().replace(" ", "-").replace("&", "and") + ".html"
        filepath = os.path.join(docs_dir, category_path, filename)

        # Create full HTML document
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

        print_progress_bar(idx, total_docs, "Save Progress")

    print(f"\n  ✓ Saved {len(documents)} HTML documents to {docs_dir}")

    elapsed = time.time() - start_time
    print_section_header(f"💾 SAVING COMPLETE (took {elapsed:.1f}s)", start=False)

    return docs_dir


def print_summary(
    structured_data, unstructured_content, documents, data_dir, docs_dir, total_elapsed
):
    """Print comprehensive generation summary"""
    print("\n" + "=" * 70)
    print("✅ GENERATION COMPLETE".center(70))
    print("=" * 70)
    print(f"⏰ Finished: {get_timestamp()}")
    print(
        f"⏱️  Total Time: {total_elapsed:.1f} seconds ({total_elapsed/60:.1f} minutes)"
    )
    print()

    print("📊 STRUCTURED DATA (CSV/JSON)")
    print(f"   Location: {data_dir}/")
    for dataset_name, dataset in structured_data.items():
        print(f"   - {dataset_name}: {len(dataset)} records")

    print("\n📝 UNSTRUCTURED DATA (Markdown)")
    print(f"   Location: {data_dir}/unstructured/")
    print(f"   - Internal memos: {len(unstructured_content['memos'])}")
    print(f"   - Meeting notes: {len(unstructured_content['meetings'])}")
    print(f"   - Project docs: {len(unstructured_content['projects'])}")

    print("\n📄 HTML DOCUMENTS")
    print(f"   Location: {docs_dir}/")
    print(f"   - HR Documents: {len([d for d in documents if d['category'] == 'HR'])}")
    print(
        f"   - Product Docs: {len([d for d in documents if d['category'] == 'Product'])}"
    )
    print(f"   - Legal Docs: {len([d for d in documents if d['category'] == 'Legal'])}")
    print(f"   - Total: {len(documents)} documents")

    print("\n" + "=" * 70)
    print("📈 DATASET STATISTICS")
    print("=" * 70)

    # Calculate totals
    total_records = sum(len(dataset) for dataset in structured_data.values())
    total_unstructured = sum(len(v) for v in unstructured_content.values())
    total_html = len(documents)
    total_files = (
        total_unstructured + total_html + len(structured_data) * 2
    )  # CSV + JSON

    print(f"   Total Structured Records: {total_records:,}")
    print(f"   Total Unstructured Docs: {total_unstructured}")
    print(f"   Total HTML Pages: {total_html}")
    print(f"   Total Files Generated: {total_files}")

    print("\n" + "=" * 70)
    print("🎉 READY FOR USE")
    print("=" * 70)
    print("\nThis dataset can be used for:")
    print("   1. GPT/LLM knowledge base and RAG demos")
    print("   2. Search and retrieval system testing")
    print("   3. Analytics and BI demonstrations")
    print("   4. Enterprise integration testing")
    print("   5. Data pipeline and ETL development")
    print("\n" + "=" * 70)


def main():
    """Main execution function"""
    overall_start_time = time.time()
    try:
        print_header()

        # Generate structured data (CSV/JSON)
        structured_data, data_dir = generate_structured_data()

        # Generate unstructured data (Markdown)
        unstructured_content, unstructured_dir = generate_unstructured_data()

        # Generate HTML documents
        documents = generate_html_documents()

        # Save HTML documents to files
        docs_dir = save_html_documents(documents)

        # Calculate total elapsed time
        total_elapsed = time.time() - overall_start_time

        # Print comprehensive summary
        print_summary(
            structured_data,
            unstructured_content,
            documents,
            data_dir,
            docs_dir,
            total_elapsed,
        )

        return 0

    except Exception as e:
        print(f"\n❌ Error: {str(e)}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
