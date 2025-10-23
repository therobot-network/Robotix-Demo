#!/bin/bash

# Generate All Extended Data
# Fills data gaps for comprehensive analytics

cd "$(dirname "$0")"

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Robotix - Extended Data Generation                       ║"
echo "║  Generating comprehensive datasets for analytics           ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is required but not found"
    exit 1
fi

# Check for required packages
python3 -c "import langchain_anthropic" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Warning: langchain_anthropic not installed"
    echo "   AI generation will be disabled"
    echo "   Install with: pip install langchain langchain-anthropic"
    echo ""
fi

# Check for .env file
if [ ! -f ../.env ]; then
    echo "⚠️  Warning: .env file not found in project root"
    echo "   AI generation requires ANTHROPIC_API_KEY"
    echo ""
fi

# Run the master generator
echo "Starting data generation..."
echo ""

python3 generate_all_extended_data.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Extended data generation complete"
    echo ""
    echo "Next steps:"
    echo "  1. Review generated data in ../data/ directories"
    echo "  2. Run website with: cd ../website && npm run dev"
    echo "  3. Test analytics queries in the customer portal"
    echo ""
else
    echo ""
    echo "❌ Generation failed. Check error messages above."
    exit 1
fi

