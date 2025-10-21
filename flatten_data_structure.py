#!/usr/bin/env python3
"""
Script to flatten the data folder structure by copying all files from nested subfolders
into new dev-prefixed meta-topic folders.

The script handles the following meta-topics:
- finance → dev-65f70496-finance
- hr-legal → dev-65f70496-hr-legal
- product → dev-65f70496-product
- sales-marketing → dev-65f70496-sales-marketing

Files are copied from subfolders (like finance/invoices/, finance/memos/)
into the new dev-prefixed folders with flattened structure.

To avoid filename conflicts, files are prefixed with their original subfolder name.
"""

import os
import shutil
from pathlib import Path
import argparse


def flatten_meta_topic_folder(meta_topic_path, target_folder_path):
    """
    Flatten a single meta-topic folder by copying all files from subfolders to the target dev-prefixed folder.

    Args:
        meta_topic_path (Path): Path to the source meta-topic folder
        target_folder_path (Path): Path to the target dev-prefixed folder
    """
    meta_topic_path = Path(meta_topic_path)
    target_folder_path = Path(target_folder_path)

    if not meta_topic_path.exists() or not meta_topic_path.is_dir():
        print(f"❌ Meta-topic folder does not exist: {meta_topic_path}")
        return

    # Create target folder if it doesn't exist
    target_folder_path.mkdir(parents=True, exist_ok=True)

    print(
        f"\n📁 Processing meta-topic: {meta_topic_path.name} → {target_folder_path.name}"
    )
    files_copied = 0

    # Find all subfolders (excluding the root)
    subfolders = [item for item in meta_topic_path.iterdir() if item.is_dir()]

    if not subfolders:
        print("  ✅ No subfolders found")
        return

    # Process each subfolder
    for subfolder in subfolders:
        print(f"  📂 Processing subfolder: {subfolder.name}")

        # Find all files in the subfolder (including nested files)
        for file_path in subfolder.rglob("*"):
            if file_path.is_file():
                # Create new filename with subfolder prefix
                relative_path = file_path.relative_to(subfolder)

                # If file is in nested subfolders, include the path structure
                if len(relative_path.parts) > 1:
                    # Join parent directories with underscores
                    parent_dirs = "_".join(relative_path.parts[:-1])
                    new_filename = (
                        f"{subfolder.name}_{parent_dirs}_{relative_path.name}"
                    )
                else:
                    new_filename = f"{subfolder.name}_{relative_path.name}"

                new_file_path = target_folder_path / new_filename

                # Handle filename conflicts
                counter = 1
                original_new_file_path = new_file_path
                while new_file_path.exists():
                    stem = original_new_file_path.stem
                    suffix = original_new_file_path.suffix
                    new_file_path = target_folder_path / f"{stem}_{counter}{suffix}"
                    counter += 1

                try:
                    # Copy the file (don't move, preserve original)
                    shutil.copy2(str(file_path), str(new_file_path))
                    print(f"    ✅ Copied: {file_path.name} → {new_file_path.name}")
                    files_copied += 1
                except Exception as e:
                    print(f"    ❌ Error copying {file_path.name}: {e}")

    print(f"   Total files copied: {files_copied}")


def main():
    parser = argparse.ArgumentParser(description="Flatten data folder structure")
    parser.add_argument(
        "--data-dir",
        default="/Users/joeyguedalia/Desktop/Work/Robotix-Demo/data",
        help="Path to the data directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually moving files",
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

    # Define the meta-topic folders and their corresponding dev-prefixed targets
    meta_topic_mapping = {
        "finance": "dev-65f70496-finance",
        "hr-legal": "dev-65f70496-hr-legal",
        "product": "dev-65f70496-product",
        "sales-marketing": "dev-65f70496-sales-marketing",
    }

    if args.meta_topic:
        meta_topic_mapping = {args.meta_topic: meta_topic_mapping[args.meta_topic]}

    print("🚀 Starting data folder flattening process...")
    print(f"📂 Data directory: {data_dir}")

    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be copied")
        # TODO: Implement dry-run logic
        print("❌ Dry-run mode not yet implemented")
        return

    total_meta_topics_processed = 0

    for source_meta_topic, target_folder_name in meta_topic_mapping.items():
        source_meta_topic_path = data_dir / source_meta_topic
        target_folder_path = data_dir / target_folder_name

        if source_meta_topic_path.exists():
            flatten_meta_topic_folder(source_meta_topic_path, target_folder_path)
            total_meta_topics_processed += 1
        else:
            print(f"⚠️  Meta-topic folder does not exist: {source_meta_topic}")

    print(
        f"\n✅ Flattening complete! Processed {total_meta_topics_processed} meta-topic folders."
    )
    print("\n📋 Summary:")
    print("   • All files have been copied from subfolders to new dev-prefixed folders")
    print(
        "   • Files are prefixed with their original subfolder name to avoid conflicts"
    )
    print("   • Original folder structure remains unchanged")


if __name__ == "__main__":
    main()
