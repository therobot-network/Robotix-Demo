#!/bin/bash
# Update Demo Files
# This script copies all data files to the public directory and regenerates the file tree

set -e

echo "🔄 Updating demo files..."

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

# Create data directory in public if it doesn't exist
mkdir -p "$SCRIPT_DIR/public/data"

# Copy all data files
echo "📦 Copying data files..."
rsync -av --delete "$PROJECT_ROOT/data/" "$SCRIPT_DIR/public/data/"

# Generate file tree
echo "🌳 Generating file tree..."
python3 "$SCRIPT_DIR/generate_file_tree.py"

echo "✅ Demo files updated successfully!"

