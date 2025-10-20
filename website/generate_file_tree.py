#!/usr/bin/env python3
"""
Generate a complete file tree JSON for the Demo Files page
"""
import json
import os
from pathlib import Path

def build_file_tree(root_path):
    """Build a hierarchical file tree structure"""
    tree = {
        "name": os.path.basename(root_path),
        "type": "directory",
        "path": "",
        "children": []
    }
    
    def add_to_tree(current_path, parent_node, base_path):
        try:
            items = sorted(os.listdir(current_path))
        except PermissionError:
            return
            
        for item in items:
            if item.startswith('.'):
                continue
                
            item_path = os.path.join(current_path, item)
            relative_path = os.path.relpath(item_path, base_path)
            
            if os.path.isdir(item_path):
                dir_node = {
                    "name": item,
                    "type": "directory",
                    "path": relative_path,
                    "children": []
                }
                parent_node["children"].append(dir_node)
                add_to_tree(item_path, dir_node, base_path)
            else:
                # Get file extension and size
                ext = os.path.splitext(item)[1].lower()
                size = os.path.getsize(item_path)
                
                file_node = {
                    "name": item,
                    "type": "file",
                    "path": relative_path,
                    "extension": ext,
                    "size": size
                }
                parent_node["children"].append(file_node)
    
    add_to_tree(root_path, tree, root_path)
    return tree

def main():
    # Build the file tree for the data directory
    data_dir = Path(__file__).parent / "public" / "data"
    
    if not data_dir.exists():
        print(f"Error: {data_dir} does not exist")
        return
    
    print(f"Generating file tree for: {data_dir}")
    tree = build_file_tree(str(data_dir))
    
    # Save to JSON file
    output_file = Path(__file__).parent / "src" / "data" / "file_tree.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(tree, f, indent=2)
    
    # Count files
    def count_files(node):
        if node["type"] == "file":
            return 1
        return sum(count_files(child) for child in node.get("children", []))
    
    file_count = count_files(tree)
    print(f"✓ Generated file tree with {file_count} files")
    print(f"✓ Saved to: {output_file}")

if __name__ == "__main__":
    main()

