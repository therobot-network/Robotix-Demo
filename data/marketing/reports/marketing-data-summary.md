# Robotix Technologies — Marketing Data Summary

**Company:** Robotix Technologies (fictional IT-led enterprise technology & robotics/automation company)
**HQ:** Bothell, Washington
**Report generated:** 2026-06-23
**Status:** All data is 100% synthetic.

This report summarizes the marketing data corpus prior to archival of the source CSV files. It
covers paid/owned campaign performance, channel engagement (email, social, website), and the
lead-scoring model output. All figures below were computed directly from the source CSVs.

**Source files**

| Dataset | File | Rows (excl. header) |
|---|---|---|
| Campaigns | `campaigns/marketing_campaigns.csv` | 50 |
| Email engagement | `engagement/email_engagement.csv` | 24 |
| Social media engagement | `engagement/social_media_engagement.csv` | 24 |
| Website engagement | `engagement/website_engagement.csv` | 24 |
| Lead scoring | `lead_scoring/lead_scores.csv` | 500 |

---

## Headline Figures

- **Total marketing spend:** $2,401,680.94 (against a planned budget of $2,521,170)
- **Total leads generated (campaigns):** 124,096
- **Total revenue generated:** $6,071,263.04 — an overall portfolio ROI of **152.8%**
- **Leads scored:** 500, with an average total score of **86.2**

---

## Campaigns (Spend, Leads, ROI)

50 campaigns spanning **2023-01-24 → 2025-05-01** across seven channel types.

| Metric | Value |
|---|---|
| Total budget | $2,521,170 |
| Total actual spend | $2,401,680.94 |
| Total leads generated | 124,096 |
| Total conversions | 9,775 |
| Total revenue generated | $6,071,263.04 |
| Average ROI (per campaign) | 136.24% |
| Average conversion rate | 7.80% |
| Overall portfolio ROI | 152.79% |

**Status mix:** Planned 20, Active 12, On Hold 10, Completed 8.

### Spend & leads by campaign type

| Campaign type | Campaigns | Spend ($) | Leads | Revenue ($) |
|---|---:|---:|---:|---:|
| Social Media | 14 | 711,057 | 41,731 | 1,402,426 |
| Email | 11 | 537,679 | 28,117 | 1,593,935 |
| Webinar | 6 | 387,723 | 11,763 | 1,037,361 |
| PPC | 6 | 218,068 | 15,140 | 579,151 |
| Trade Show | 5 | 217,621 | 10,668 | 476,836 |
| Content Marketing | 4 | 181,753 | 7,217 | 553,599 |
| Direct Mail | 4 | 147,780 | 9,460 | 427,955 |

### Top campaigns by ROI

| Campaign ID | Name | Type | Spend ($) | Leads | Revenue ($) | ROI (%) |
|---|---|---|---:|---:|---:|---:|
| CAMP-2024009 | Webinar - Q2 2024 | Webinar | 87,405.51 | 3,597 | 365,674.10 | 298.15 |
| CAMP-2024047 | Content Marketing - Q4 2024 | Email | 27,621.89 | 4,698 | 113,730.87 | 294.47 |
| CAMP-2024046 | Trade Show - Q1 2023 | Email | 77,531.52 | 1,349 | 291,433.14 | 282.46 |

---

## Email Engagement

24 monthly records, **2023-11 → 2025-09**.

| Metric | Value |
|---|---|
| Total emails sent | 601,067 |
| Average open rate | 23.42% |
| Average click rate | 4.53% |
| Average conversion rate | 0.25% |
| Average bounce rate | 2.35% |
| Total conversions | 1,495 |
| Total unsubscribes | 3,352 |

### Representative rows

| Month | Emails sent | Unique opens | Open rate % | Clicks | Click rate % | Conversions | Unsubs | Bounce % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2023-11 | 32,675 | 6,688 | 20.5 | 1,297 | 4.0 | 93 | 112 | 2.8 |
| 2023-12 | 20,813 | 5,231 | 25.1 | 673 | 3.2 | 29 | 132 | 2.2 |
| 2024-01 | 20,601 | 3,963 | 19.2 | 925 | 4.5 | 38 | 196 | 2.8 |

---

## Social Media Engagement

24 monthly records, **2023-11 → 2025-09**.

| Metric | Value |
|---|---|
| Followers (start → end) | 12,701 → 12,074 |
| Total posts | 687 |
| Total impressions | 2,321,946 |
| Total engagements | 76,209 |
| Average engagement rate | 2.92% |
| Total leads generated | 1,498 |
| Total conversions | 726 |

### Representative rows

| Month | Followers | Posts | Impressions | Engagements | Eng. rate % | Clicks | Conversions | Leads |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2023-11 | 12,701 | 24 | 131,545 | 3,459 | 1.9 | 453 | 48 | 97 |
| 2023-12 | 12,931 | 33 | 139,863 | 3,091 | 2.7 | 520 | 37 | 43 |
| 2024-01 | 10,681 | 20 | 93,973 | 2,507 | 3.3 | 1,124 | 29 | 30 |

---

## Website Engagement

24 monthly records, **2023-11 → 2025-09**.

| Metric | Value |
|---|---|
| Total visits | 974,060 |
| Total unique visitors | 717,167 |
| Total page views | 3,640,085 |
| Average session duration | 3.73 min |
| Average bounce rate | 45.91% |
| Average conversion rate | 1.04% |
| Total conversions | 7,476 |
| Total leads generated | 6,141 |

### Representative rows

| Month | Visits | Unique | Page views | Avg session (min) | Bounce % | Conversions | Conv. rate % | Leads |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2023-11 | 42,115 | 29,301 | 164,626 | 2.6 | 53.7 | 225 | 0.63 | 279 |
| 2023-12 | 30,044 | 21,668 | 130,073 | 2.5 | 39.4 | 427 | 1.49 | 376 |
| 2024-01 | 39,991 | 31,409 | 173,474 | 4.1 | 43.9 | 201 | 0.52 | 226 |

---

## Lead Scoring (Distribution & Grades)

500 scored leads created **2025-04-25 → 2025-10-21**. Total score ranges **35–147**, averaging **86.19**.

### Grade distribution

| Grade | Leads | Share |
|---|---:|---:|
| A | 318 | 63.6% |
| B | 122 | 24.4% |
| C | 54 | 10.8% |
| D | 6 | 1.2% |

### Average score by component

| Component | Avg score |
|---|---:|
| Demographic | 34.84 |
| Email engagement | 15.09 |
| Demo | 13.60 |
| Website | 12.43 |
| Content | 10.23 |
| **Total** | **86.19** |

### Lead source distribution

| Source | Leads |
|---|---:|
| Referral | 122 |
| Content Download | 105 |
| Website | 94 |
| Trade Show | 92 |
| Cold Call | 87 |

**Status mix:** Working 118, New 110, Qualified 100, Converted 99, Unqualified 73.
**Lifecycle stage mix:** Lead 113, Subscriber 108, Opportunity 100, MQL 93, SQL 86.

### Representative rows

| Lead ID | Company | Source | Total score | Grade | Status | Lifecycle |
|---|---|---|---:|---|---|---|
| LEAD-000001 | Company 2075 | Referral | 74 | B | New | Opportunity |
| LEAD-000002 | Company 2366 | Content Download | 107 | A | New | MQL |
| LEAD-000003 | Company 8732 | Website | 88 | A | Converted | SQL |

---

*End of report. Source CSVs may be archived after this summary is reviewed.*
