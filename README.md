# Robotix Enterprise Synthetic Dataset

A comprehensive AI-generated synthetic enterprise dataset for **Robotix**, a fictional robotics manufacturer. Goes beyond traditional datasets like AdventureWorks by combining **structured data** (CSV/JSON) + **internal documents** (Markdown) + **website content** (HTML).

## Why This Dataset is Different

**Standard datasets (AdventureWorks, Northwind, Chinook):**
- ❌ Only structured database tables (employees, orders, products)
- ❌ No website or documentation content
- ❌ No internal memos or meeting notes
- ❌ Template-based, repetitive content

**This dataset:**
- ✅ Structured backend data (2,700+ records across 6 tables)
- ✅ Internal documents (17 memos, meetings, project docs)
- ✅ Website content (45+ HTML pages: HR policies, legal docs, product documentation)
- ✅ All AI-generated with realistic business language (no templates)

**Perfect for:**
- GPT/LLM Knowledge Base & RAG Demos (indexes database + docs + website)
- Search and Retrieval System Testing
- Enterprise AI Assistant Development
- Analytics and BI Demonstrations
- Multi-source Data Integration Testing

## AI-First Approach

All content is generated using Claude 3.5 Sonnet - no hardcoded templates.

**Benefits:**
- Realistic, varied content every time
- Contextually appropriate for robotics industry
- Dynamic and authentic business language
- ~70% less code than template-based approaches

## Generated Data

### Structured Data (CSV/JSON)
- **Employees**: 20 employees across 10 departments
- **Products**: 20+ robotics products (Industrial Robots, Collaborative Robots, Mobile Robots, Components, Software)
- **Customers**: 500 B2B and individual customers
- **Sales Orders**: 1,000+ orders with enterprise pricing
- **Support Tickets**: 200+ technical support interactions

### Unstructured Data (Markdown) - AI-Generated
- **Internal Memos** (9): Sales performance, product launches, policy updates, manufacturing improvements, sustainability, customer feedback, security, partnerships, wellness
- **Meeting Notes** (4): Product planning, sales strategy, manufacturing investment, customer advisory
- **Project Documentation** (4): E-commerce platform, robot development, facility expansion, AI maintenance platform

### HTML Documents - AI-Generated
- **HR Documents** (3): Employee Handbook, Remote Work Policy, Benefits Overview
- **Product Documentation** (40+): Technical specs and user guides for all robot models
- **Legal Documents** (2): Privacy Policy, Warranty and Return Policy

## Quick Start

### 1. Installation

```bash
cd demoSite
pip install -r requirements.txt
```

**Requirements:**
- Python 3.8+
- langchain, langchain-anthropic, anthropic, python-dotenv

### 2. Set Up API Key

```bash
# Create .env file
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env

# Or export directly
export ANTHROPIC_API_KEY="your-api-key-here"
```

Get your API key from: https://console.anthropic.com/

### 3. Generate Dataset

```bash
cd generators
python3 main.py
```

Generation takes 5-15 minutes (50+ AI API calls).

### 4. Output Structure

```
data/
├── employees.csv / employees.json
├── products.csv / products.json
├── customers.csv / customers.json
├── orders.csv / orders.json
├── order_items.csv / order_items.json
├── support_tickets.csv / support_tickets.json
├── metadata.json
├── unstructured/
│   ├── memos/
│   ├── meetings/
│   └── projects/
└── html_documents/
    ├── hr/
    ├── product/
    └── legal/
```

## Fictional Company: Robotix

- **Industry**: Robotics & Automation
- **Founded**: 1998
- **Headquarters**: Bothell, Washington
- **Employees**: 290
- **Revenue**: $42M (2024)
- **Tagline**: "Automate Your Future"

**Product Lines:**
- Industrial Robots (6-axis articulated arms, welding robots)
- Collaborative Robots (cobots for human-robot collaboration)
- Mobile Robots (AGVs, AMRs for material handling)
- Components (sensors, grippers, vision systems)
- Software (control systems, fleet management, AI platforms)

## Customization

### Adjust Dataset Size

Edit `generators/main.py`:

```python
gen.generate_customer_data(num_customers=1000)  # Default: 500
gen.generate_sales_data(num_orders=5000)        # Default: 1000
gen.generate_support_tickets(num_tickets=500)   # Default: 200
```

### Modify Company Details

Edit `generators/company_data.py`:

```python
COMPANY = {
    "name": "Your Company Name",
    "tagline": "Your Tagline",
    "industry": "Your Industry",
    # ...
}
```

## Technical Details

### AI Generation
- **Model**: Claude 3.5 Sonnet (via LangChain)
- **Temperature**: 0.7
- **Max Tokens**: 8000 for documents, 6000 for unstructured content
- **Cost**: ~$0.50-$2.00 per full dataset generation

### Data Realism
- Employee salaries vary by department and role
- Product pricing realistic for industrial robotics
- Customer mix: 70% B2B companies, 30% individuals
- Order values range from $5K to $500K+
- All dates within 2023-2024 range

## Dataset Statistics

Typical output from a single run:

- **Structured Records**: ~2,700+ records across 6 datasets
- **Unstructured Documents**: 17 markdown documents
- **HTML Documents**: 45+ pages
- **Total Files**: 60+ files
- **Total Size**: ~5-10 MB

## Privacy & Compliance

- All data is 100% synthetic
- No real people or companies
- No PII (Personally Identifiable Information)
- GDPR/CCPA compliant

## Troubleshooting

**"ANTHROPIC_API_KEY not found"**
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

**"AI generation failed"**
- Check API key is valid
- Verify internet connection
- Check Anthropic API status: https://status.anthropic.com

**"ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

**Generation is slow**
- AI generation makes 50+ API calls (normal)
- Total time: 5-15 minutes
- Reduce document count in main.py to speed up

## FAQ

**Q: Can I use this for commercial projects?**
A: Yes, the generated data is completely synthetic and free to use.

**Q: Do I need an API key?**
A: Yes, for AI-generated content. Without it, you'll get placeholder text.

**Q: How much does it cost?**
A: Approximately $0.50-$2.00 per full dataset with Claude 3.5 Sonnet.

**Q: Can I generate without AI?**
A: Structured data works without AI, but documents will be placeholders.

**Q: How realistic is the data?**
A: Very realistic - AI generates contextually appropriate business content for the robotics industry.

**Q: Can I modify the company?**
A: Yes, edit `company_data.py` to change company details, products, employees, etc.

**Q: Is every generation unique?**
A: Yes, AI generates fresh content each time.

## Comparison to Standard Enterprise Datasets

| Feature | AdventureWorks / Northwind | **This Dataset** |
|---------|---------------------------|------------------|
| Structured Data (SQL/CSV) | ✅ Yes | ✅ Yes (2,700+ records) |
| Internal Documents (memos, meetings) | ❌ No | ✅ Yes (17 documents) |
| Website Content (HTML) | ❌ No | ✅ Yes (45+ pages) |
| Product Documentation | ❌ No | ✅ Yes (40+ specs & guides) |
| HR Policies & Legal Docs | ❌ No | ✅ Yes (5 documents) |
| AI-Generated (not templates) | ❌ No | ✅ Yes |
| Industry-Specific | ❌ Generic | ✅ Robotics/Automation |

**Bottom line:** This is the only synthetic dataset that gives you **database + documents + website** in one package - everything a real enterprise GPT knowledge base needs to index.

## What Makes This Different

1. **Complete Enterprise Coverage**: Database tables + internal docs + public website content
2. **AI-First**: Nearly all content generated by Claude (not templates)
3. **Industry-Specific**: Tailored for robotics/automation with technical accuracy
4. **Realistic**: B2B sales cycles, enterprise pricing, technical support workflows
5. **Efficient**: ~70% less code than template-based approaches
6. **Dynamic**: Every generation produces unique, varied content

## License

This synthetic dataset generator is for demonstration purposes. Generated data is free to use for any purpose.
