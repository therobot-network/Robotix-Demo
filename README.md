# Robotix Enterprise Synthetic Dataset

A synthetic enterprise dataset for **Robotix**, a fictional robotics and automation
manufacturer. It combines **structured data** (CSV/JSON), **internal documents**
(Markdown), and **public-facing content** (HTML) across the major functions of a
company — finance, HR & legal, product, and sales & marketing.

All data is 100% synthetic. No real people, companies, or PII.

## Fictional Company: Robotix

- **Industry**: Robotics & Automation
- **Founded**: 1998
- **Headquarters**: Bothell, Washington
- **Employees**: 290
- **Revenue**: $42M (2024)
- **Tagline**: "Automate Your Future"

**Product Lines:** Industrial Robots, Collaborative Robots (cobots), Mobile Robots
(AGVs/AMRs), Components (sensors, grippers, vision systems), and Software (control
systems, fleet management, AI platforms).

## What's Inside

~200 files (~7.5 MB) across CSV, JSON, Markdown, and HTML, organized by business domain.

```
data/
├── metadata.json            # Company profile + dataset field schemas
├── finance/                 # AR/AP aging, cash flow, compensation, debt,
│                            #   expenses, invoices, orders, reports,
│                            #   statements, vendors, memos
├── hr-legal/                # Employees, headcount, attrition, diversity,
│                            #   benefits, compensation, recruiting, training,
│                            #   legal (compliance, contracts, litigation),
│                            #   policies, memos
├── product/                 # Bugs, features, feedback, releases, support,
│                            #   user metrics, meetings, projects, memos
├── sales-marketing/         # Leads, customers, campaigns, marketing
│                            #   (engagement, lead scoring), sales (pipeline,
│                            #   forecasts, quotas, quotes), memos
└── public/                  # Public-facing content
    ├── marketing-forms/
    ├── product-guides/
    └── product-specs/
```

Most structured tables ship as both CSV and JSON. Narrative content (memos,
meeting notes, reports, policies) is Markdown, and public-facing material is HTML.

## File Types

| Type | Count | Use |
|------|-------|-----|
| CSV  | 52    | Structured tables for analytics / DB import |
| JSON | 53    | Same structured data, nested/typed form |
| HTML | 56    | Public-facing pages (guides, specs, forms) |
| MD   | 39    | Internal memos, meetings, reports, policies |

## Suggested Uses

- Knowledge base & RAG demos (index structured data + documents + web content)
- Search and retrieval system testing
- Analytics and BI demonstrations
- Multi-source data integration testing

## License

Synthetic data, free to use for any purpose.
