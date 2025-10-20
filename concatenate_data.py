#!/usr/bin/env python3
"""
Concatenate all files in the data directory into a single file.
Each file is separated by a header showing the file path.
"""

import os
from pathlib import Path

def concatenate_files(data_dir='data', output_file='concatenated_data.txt'):
    """
    Concatenate all files from data_dir into a single output file.
    
    Args:
        data_dir: Directory to scan for files
        output_file: Output file path
    """
    # Get all files, sorted
    data_path = Path(data_dir)
    files = sorted([f for f in data_path.rglob('*') if f.is_file() and not f.name.startswith('.')])
    
    print(f"Found {len(files)} files to concatenate...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for idx, file_path in enumerate(files, 1):
            print(f"Processing {idx}/{len(files)}: {file_path}")
            
            # Write separator header
            separator = "=" * 80
            outfile.write(f"\n{separator}\n")
            outfile.write(f"FILE: {file_path}\n")
            outfile.write(f"{separator}\n\n")
            
            # Try to read and write file content
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    
                    # Add newline if file doesn't end with one
                    if content and not content.endswith('\n'):
                        outfile.write('\n')
                        
            except UnicodeDecodeError:
                # Handle binary files or encoding issues
                outfile.write(f"[Binary file or encoding error - skipped]\n")
            except Exception as e:
                outfile.write(f"[Error reading file: {e}]\n")
            
            outfile.write("\n")
    
    # Get file size
    file_size = os.path.getsize(output_file)
    file_size_mb = file_size / (1024 * 1024)
    
    print(f"\n✅ Done!")
    print(f"📁 Output file: {output_file}")
    print(f"📊 Total files concatenated: {len(files)}")
    print(f"💾 File size: {file_size:,} bytes ({file_size_mb:.2f} MB)")

if __name__ == "__main__":
    concatenate_files()

