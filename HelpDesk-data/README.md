# Summit IT Service Desk — Synthetic Knowledge Base

A large, synthetic IT Help Desk dataset for **Summit IT Services**, a fictional
managed IT services provider and internal service desk. It is designed to be
dropped into a knowledge base, help desk widget, chatbot, or RAG pipeline as
realistic end-user-facing IT support content.

All content is 100% synthetic. No real people, companies, credentials, or PII.

## What's Inside

138 documents in a mix of **HTML** and **PDF**. End-user, web-facing content
(KB articles, FAQs, troubleshooting) is HTML; formal documents (policies,
service catalog, onboarding, runbooks, escalation, reference, glossary) are PDF.

| Content | Count | Format |
|---------|-------|--------|
| KB articles | 78 across 8 categories | HTML |
| FAQs | 7 | HTML |
| Troubleshooting flows | 7 | HTML |
| IT policies | 12 | PDF |
| Service catalog + SLA docs | 13 | PDF |
| Onboarding / offboarding docs | 6 | PDF |
| Internal runbooks | 10 | PDF |
| Escalation docs + glossary | 4 | PDF |
| Environment reference | 1 | PDF |

[kb-index.html](kb-index.html) is a browsable catalog of all 138 documents
(id, title, category, audience, format) with links to each file.

```
HelpDesk-data/
├── reference/               # Environment standards (the "source of truth") — PDF
├── kb-articles/             # End-user how-to & fix-it articles — HTML
│   ├── accounts-access/     #   Passwords, MFA, SSO, account requests
│   ├── email/               #   Outlook, Teams, OneDrive, SharePoint
│   ├── network-vpn/         #   Wi-Fi, GlobalProtect VPN, connectivity
│   ├── hardware/            #   Laptops, monitors, peripherals, RMAs
│   ├── software/            #   Installs, licenses, activation, updates
│   ├── printing/            #   PaperCut, MFPs, scanning
│   ├── mobile/              #   Intune enrollment, BYOD, lost devices
│   └── security/            #   Phishing, malware, safe computing
├── faqs/                    # Frequently asked questions by audience — HTML
├── troubleshooting/         # Step-by-step diagnostic flows — HTML
├── policies/                # IT & security policies — PDF
├── onboarding/              # New hire / offboarding checklists & guides — PDF
├── service-catalog/         # Service offerings, request types, SLA matrix — PDF
├── runbooks/                # Internal procedures for service desk agents — PDF
├── glossary/                # IT terminology — PDF
└── kb-index.html            # Browsable catalog of every document
```

## The Fictional Company: Summit IT Services

- **What they do:** Managed IT services + internal IT service desk
- **Service Desk portal:** https://help.summitit.com
- **Email:** servicedesk@summitit.com · **Phone:** +1 (800) 555-7866
- **ITSM platform:** SummitDesk
- **Core stack:** Okta SSO · Microsoft 365 · GlobalProtect VPN · Microsoft
  Intune / Jamf Pro · CrowdStrike Falcon · 1Password · Slack · Zoom

See [reference/it-environment-standards.pdf](reference/it-environment-standards.pdf)
for the full environment definition that every document is written against.

## Document Format

Each document carries a metadata header (id, category, audience, last updated,
tags) and is self-contained. HTML articles are styled, single-file pages ready
to drop into a help desk widget; PDFs are print-ready formal documents. Start
from [kb-index.html](kb-index.html) to browse everything.

## Suggested Uses

- Help desk widget / chatbot knowledge base
- RAG and semantic-search demos and benchmarks
- ITSM / service desk tool seeding and demos
- Support-content QA and summarization testing

## License

Synthetic data, free to use for any purpose.
