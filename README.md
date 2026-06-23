# Robotix Technologies — Synthetic Enterprise Corpus

A single-company synthetic dataset for **Robotix Technologies**, a fictional,
**IT-led enterprise technology company** that also designs and builds robotics &
automation products. The corpus spans every major department of one company —
**IT** (the core), Product/Robotics, Finance, HR, Legal, Sales, and Marketing —
as a realistic mix of internal documents and public-facing content.

All data is 100% synthetic. No real people, companies, credentials, or PII.

See [data/company-profile.md](data/company-profile.md) for the canonical company
identity (names, domains, contacts, IT stack) that every document is written
against.

## The Company

| | |
|---|---|
| **Name** | Robotix Technologies |
| **Primary focus** | Enterprise IT & Technology (IT-led) |
| **Also** | Robotics & Automation products |
| **Founded** | 1998 · **HQ:** Bothell, Washington |
| **Size** | ~290 employees · ~$42M revenue (2024) |
| **Domain / IT** | robotix.com · help.robotix.com · RobotixDesk · Okta · M365 · CrowdStrike · GlobalProtect |
| **Tagline** | "Automate Your Future" |

## Structure — one folder per department

```
data/
├── company-profile.md          # Canonical company identity (the source of truth)
├── it/            ★ CORE       # Internal IT service desk: 78 KB articles, FAQs,
│                               #   troubleshooting (HTML); policies, runbooks,
│                               #   service catalog & SLAs, onboarding, escalation,
│                               #   glossary, environment reference (PDF)
├── product/                    # Robotics & Automation division: product catalog
│                               #   & specs/user guides (HTML), releases, bugs,
│                               #   features, feedback, support, meetings, projects
├── finance/                    # P&L statements, budgets, AR/AP, cash flow, debt,
│                               #   vendors, payroll & compensation accounting
├── hr/                         # Employees, headcount, attrition, diversity,
│                               #   recruiting, training, benefits, policies
├── legal/                      # Contracts, compliance, IP, litigation, policies
├── sales/                      # Pipeline, forecasts, quotas, quotes, customers,
│                               #   lead tracking
└── marketing/                  # Campaigns, engagement, lead scoring, NPS, forms
```

## What's inside

Document-first: information lives mostly in **Markdown** and **PDF** narrative
reports and **HTML** web content, with only a handful of raw CSV registries.

| Type | Count | Use |
|------|-------|-----|
| HTML | 149 | Public-facing & web content (IT KB articles, product specs/guides, forms) |
| PDF  | 93  | Formal documents (IT policies/runbooks/catalog, financial & departmental reports) |
| MD   | 49  | Internal reports, memos, meeting notes, statements, project briefs |
| CSV  | 3   | Core machine-readable registries only: employees, products, customers |

There are **no JSON files**. The bulk of the structured data that used to live in
CSV/JSON has been rolled up into narrative Markdown **data-summary reports** (one
or more per department, e.g. `*/reports/*-summary.md`) — each with figures
computed from the underlying data — and rendered to PDF alongside. Only three
core entity tables remain as CSV:

- [data/hr/employees/employees.csv](data/hr/employees/employees.csv)
- [data/product/specs/products.csv](data/product/specs/products.csv)
- [data/sales/customers/customers.csv](data/sales/customers/customers.csv)

## Suggested uses

- Knowledge base & RAG demos over a single coherent company (IT-heavy)
- Help desk / chatbot knowledge base seeding (the `it/` department)
- Multi-department search, retrieval, and summarization testing
- Enterprise document QA across formats (HTML + PDF + Markdown)

## License

Synthetic data, free to use for any purpose.
