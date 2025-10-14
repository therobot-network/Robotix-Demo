#!/bin/bash
# Generate Financial and Marketing Data
# Run this script to add invoices, campaigns, budget reports, P&L statements, etc.

echo "🚀 Starting Financial & Marketing Data Generation..."
echo ""

# Get the script directory and project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$SCRIPT_DIR"

# Check if .env file exists in project root
if [ ! -f "$PROJECT_ROOT/.env" ] && [ ! -f ".env" ]; then
    echo "⚠️  No .env file found in project root. Make sure ANTHROPIC_API_KEY is set."
    echo "   Create a .env file in $PROJECT_ROOT with: ANTHROPIC_API_KEY=your_api_key_here"
    echo ""
fi

# Check if virtual environment exists
if [ ! -d "../website/.venv" ]; then
    echo "⚠️  No virtual environment found. Creating one..."
    python3 -m venv ../website/.venv
fi

# Activate virtual environment
source ../website/.venv/bin/activate

# Check if dependencies are installed
if ! python3 -c "import langchain_anthropic" 2>/dev/null; then
    echo "📦 Installing required dependencies..."
    pip install langchain langchain-anthropic python-dotenv
fi

# Run the generator
echo ""
echo "🔧 Running Financial & Marketing Data Generator..."
python3 financial_marketing_generator.py

if [ $? -eq 0 ]; then
    echo ""
    echo "📝 Updating metadata.json..."
    python3 update_metadata.py
    
    echo ""
    echo "📄 Updating documents.json..."
    python3 update_documents_json.py
    
    echo ""
    echo "🎉 All done! New data has been generated:"
    echo "   📊 CSV/JSON: invoices.csv/json, marketing_campaigns.csv/json"
    echo "   📄 HTML: 5 budget reports, 3 customer feedback forms"
    echo "   📝 Markdown: 3 P&L statements, 10 lead tracking reports"
    echo ""
    echo "   Check the data/ directory for new files."
else
    echo ""
    echo "❌ Generator failed. Check the error messages above."
fi

# Deactivate virtual environment
deactivate

