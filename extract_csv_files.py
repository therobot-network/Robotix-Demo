#!/usr/bin/env python3
"""
Script to extract only CSV files from nested subfolders in the data directory
and copy them into new dev-prefixed folders with "-csv" suffix.

The script handles the following meta-topics:
- finance → dev-65f70496-finance-csv
- hr-legal → dev-65f70496-hr-legal-csv
- product → dev-65f70496-product-csv
- sales-marketing → dev-65f70496-sales-marketing-csv

Only CSV files are copied from subfolders into the new target folders.
Files are prefixed with their original subfolder name to avoid conflicts.
"""

import os
import shutil
from pathlib import Path
import argparse


def extract_csv_files_from_meta_topic(meta_topic_path, target_folder_name, data_dir):
    """
    Extract CSV files from a single meta-topic folder and copy them to the target folder.

    Args:
        meta_topic_path (Path): Path to the source meta-topic folder
        target_folder_name (str): Name of the target folder to create
        data_dir (Path): Path to the data directory where target folder will be created
    """
    meta_topic_path = Path(meta_topic_path)
    target_path = data_dir / target_folder_name

    if not meta_topic_path.exists() or not meta_topic_path.is_dir():
        print(f"❌ Meta-topic folder does not exist: {meta_topic_path}")
        return

    # Create target directory if it doesn't exist
    target_path.mkdir(exist_ok=True)

    print(f"\n📁 Processing meta-topic: {meta_topic_path.name}")
    print(f"📂 Target folder: {target_folder_name}")

    csv_files_copied = 0

    # Find all CSV files in the meta-topic folder (including nested files)
    csv_files = list(meta_topic_path.rglob("*.csv"))

    if not csv_files:
        print("  ❌ No CSV files found in this meta-topic")
        return

    print(f"  🔍 Found {len(csv_files)} CSV file(s)")

    # Process each CSV file
    for csv_file in csv_files:
        # Get the relative path from the meta-topic root
        relative_path = csv_file.relative_to(meta_topic_path)

        # Create new filename with subfolder prefix
        if len(relative_path.parts) > 1:
            # File is in a subfolder, use subfolder name as prefix
            subfolder_parts = relative_path.parts[:-1]  # All parts except filename
            subfolder_prefix = "_".join(subfolder_parts)
            new_filename = f"{subfolder_prefix}_{relative_path.name}"
        else:
            # File is directly in meta-topic root
            new_filename = relative_path.name

        new_file_path = target_path / new_filename

        # Handle filename conflicts
        counter = 1
        original_new_file_path = new_file_path
        while new_file_path.exists():
            stem = original_new_file_path.stem
            suffix = original_new_file_path.suffix
            new_file_path = target_path / f"{stem}_{counter}{suffix}"
            counter += 1

        try:
            # Copy the CSV file
            shutil.copy2(str(csv_file), str(new_file_path))
            print(f"    ✅ Copied: {csv_file.name} → {new_file_path.name}")
            csv_files_copied += 1
        except Exception as e:
            print(f"    ❌ Error copying {csv_file.name}: {e}")

    print(f"  📊 Total CSV files copied: {csv_files_copied}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract CSV files from data folder structure"
    )
    parser.add_argument(
        "--data-dir",
        default="/Users/joeyguedalia/Desktop/Work/Robotix-Demo/data",
        help="Path to the data directory",
    )
    parser.add_argument(
        "--meta-topic",
        choices=["finance", "hr-legal", "product", "sales-marketing"],
        help="Process only a specific meta-topic folder",
    )

    args = parser.parse_args()

    data_dir = Path(args.data_dir)

    if not data_dir.exists():
        print(f"❌ Data directory does not exist: {data_dir}")
        return

    # Define the meta-topic folders and their corresponding target folders
    meta_topic_mappings = {
        "finance": "dev-65f70496-finance-csv",
        "hr-legal": "dev-65f70496-hr-legal-csv",
        "product": "dev-65f70496-product-csv",
        "sales-marketing": "dev-65f70496-sales-marketing-csv",
    }

    if args.meta_topic:
        # Process only the specified meta-topic
        meta_topic_mappings = {args.meta_topic: meta_topic_mappings[args.meta_topic]}

    print("🚀 Starting CSV file extraction process...")
    print(f"📂 Data directory: {data_dir}")
    print("📋 Target folders:")
    for source, target in meta_topic_mappings.items():
        print(f"   • {source} → {target}")

    total_meta_topics_processed = 0

    for meta_topic, target_folder in meta_topic_mappings.items():
        meta_topic_path = data_dir / meta_topic

        if meta_topic_path.exists():
            extract_csv_files_from_meta_topic(meta_topic_path, target_folder, data_dir)
            total_meta_topics_processed += 1
        else:
            print(f"⚠️  Meta-topic folder does not exist: {meta_topic}")

    print(
        f"\n✅ CSV extraction complete! Processed {total_meta_topics_processed} meta-topic folders."
    )
    print("\n📋 Summary:")
    print(
        "   • Only CSV files have been copied from subfolders to new dev-prefixed-csv folders"
    )
    print(
        "   • Files are prefixed with their original subfolder name to avoid conflicts"
    )
    print("   • Original folder structure remains unchanged")

    # Show final folder structure
    print(f"\n📁 New CSV folders created in {data_dir}:")
    for target_folder in meta_topic_mappings.values():
        target_path = data_dir / target_folder
        if target_path.exists():
            csv_count = len(list(target_path.glob("*.csv")))
            print(f"   📂 {target_folder} ({csv_count} CSV files)")


if __name__ == "__main__":
    main()
