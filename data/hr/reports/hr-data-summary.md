# Robotix Technologies — HR Data Summary

**Company:** Robotix Technologies (fictional, IT-led enterprise technology and robotics/automation company)
**HQ:** Bothell, Washington · **Founded:** 1998 · **Email domain:** robotix.com
**Report date:** 2026-06-23
**Status:** All data is 100% synthetic.

## Overview

This report summarizes the seven HR analytics CSV extracts under `data/hr/` so the source
files can be archived. Every figure below was computed directly from the source CSVs
(via pandas) — no values are estimated. The raw employee roster (`employees/employees.csv`)
is retained separately and is not summarized here.

| Dataset | File | Rows |
|---|---|---|
| Headcount (monthly, by dept) | `headcount/historical_headcount.csv` | 360 |
| Attrition records | `attrition/attrition_records.csv` | 80 |
| Compensation analysis | `compensation/compensation_analysis.csv` | 80 |
| Diversity — current | `diversity/diversity_current.csv` | 30 |
| Diversity — trends | `diversity/diversity_trends.csv` | 12 |
| Recruiting pipeline | `recruiting/recruiting_pipeline.csv` | 120 |
| Training records | `training/training_records.csv` | 300 |

---

## 1. Headcount Trends

Monthly headcount across **10 departments**, spanning **2022-11 → 2025-09** (35 months).

- **Starting total (2022-11):** 233 headcount · 228.29 FTE
- **Latest total (2025-09):** 279 headcount · 273.93 FTE
- **Net growth over the period:** +46 headcount (**+19.7%**)
- **Contractors:** 0 reported across all months (all employees are FTE-tracked)

Latest-month headcount by department (2025-09):

| Department | Headcount | FTE |
|---|---:|---:|
| Product Development | 67 | 65.81 |
| Manufacturing | 46 | 45.63 |
| Sales & Marketing | 40 | 39.28 |
| Customer Service | 28 | 27.65 |
| IT & Systems | 26 | 25.76 |
| Finance | 20 | 19.36 |
| Quality Assurance | 18 | 17.91 |
| Legal & Compliance | 17 | 16.16 |
| Executive Leadership | 11 | 10.56 |
| Human Resources | 6 | 5.81 |

Product Development is the largest function (~24% of headcount), followed by Manufacturing.

---

## 2. Attrition

**80 attrition records** with termination dates from **2020-10-22 → 2025-10-19**.

- **Voluntary vs. involuntary:** 45 voluntary (56.3%) · 35 involuntary (43.8%)
- **Average tenure at exit:** 22.8 months
- **Regrettable departures:** 30 of 80 (37.5%)
- **Exit interview completed:** 42 of 80 (52.5%)
- **Eligible for rehire:** 56 of 80 (70.0%)
- **Average notice period:** 7.1 days

**Top termination reasons:** Voluntary – Better Opportunity (12), End of Contract (11),
Voluntary – Relocation (10), Involuntary – Position Eliminated (10), Voluntary – Retirement (9).

**Highest-attrition departments:** Human Resources (11), then Quality Assurance,
Executive Leadership, Sales & Marketing, and Customer Service (9 each).

Representative records:

| ID | Department | Level | Tenure (mo) | Type | Reason | Regrettable |
|---|---|---|---:|---|---|---|
| ATR-00001 | Manufacturing | VP | 10.8 | Voluntary | Better Opportunity | No |
| ATR-00002 | IT & Systems | Entry | 21.1 | Voluntary | Better Opportunity | No |
| ATR-00003 | Manufacturing | Senior | 26.4 | Involuntary | End of Contract | No |
| ATR-00004 | Legal & Compliance | Mid | 10.1 | Voluntary | Relocation | Yes |

---

## 3. Compensation Analysis

**80 department × job-level cohorts** covering 10 departments and 8 job levels
(Entry, Mid, Senior, Lead, Manager, Director, VP, Executive), totaling 658 employee slots.

- **Headcount-weighted average base salary:** ~$152,765
- **Headcount-weighted average total comp:** ~$175,981
- **Salary range across cohorts:** $52,492.61 (min) → $352,236.26 (max)
- **Average market percentile:** 54.2 (positioned slightly above market median)

Weighted average base salary by job level:

| Job Level | Wtd. Avg Base | Slots |
|---|---:|---:|
| Entry | $64,448 | 72 |
| Mid | $86,044 | 68 |
| Senior | $108,977 | 73 |
| Lead | $134,511 | 98 |
| Manager | $126,152 | 68 |
| Director | $166,353 | 90 |
| VP | $208,895 | 106 |
| Executive | $279,494 | 83 |

Sample cohort rows (Product Development):

| Department | Level | Count | Avg Base | Median | Avg Total Comp | Mkt %ile |
|---|---|---:|---:|---:|---:|---:|
| Product Development | Entry | 8 | $64,380 | $65,491 | $76,442 | 40 |
| Product Development | Mid | 5 | $85,833 | $86,311 | $96,886 | 60 |
| Product Development | Senior | 2 | $107,014 | $106,789 | $122,816 | 50 |
| Product Development | Lead | 15 | $137,696 | $136,895 | $164,916 | 40 |

---

## 4. Diversity

### Current snapshot

**30 department × job-category × gender** rows across all 10 departments. Reported counts:

- **Total reported:** 256 employees
- **Male:** 163 (63.7%)
- **Female:** 93 (36.3%)
- **Non-binary:** 0 reported

Sample rows:

| Department | Job Category | Gender | Count | % |
|---|---|---|---:|---:|
| Executive Leadership | Individual Contributor | Male | 33 | 67.3 |
| Executive Leadership | Manager | Female | 15 | 30.6 |
| Human Resources | Individual Contributor | Male | 11 | 47.8 |
| Human Resources | Executive | Female | 8 | 34.8 |

### Trends (Q4 2022 → Q3 2025)

12 quarterly snapshots tracking representation metrics company-wide.

| Quarter | Total | Female % | URM % | Female Leadership % |
|---|---:|---:|---:|---:|
| Q4 2022 | 259 | 37.8 | 20.9 | 28.6 |
| Q4 2023 | 286 | 35.2 | 20.5 | 34.4 |
| Q4 2024 | 276 | 37.3 | 21.1 | 29.8 |
| Q2 2025 | 274 | 36.5 | 21.2 | 33.7 |
| Q3 2025 | 247 | 35.5 | 22.3 | 28.6 |

Female representation has held roughly in the **34–38%** band, underrepresented-minority
share in the **18–22%** range, and female leadership in the **28–34%** range over the period —
relatively flat with quarter-to-quarter fluctuation.

---

## 5. Recruiting Pipeline

**120 requisitions** posted **2025-04-26 → 2025-10-19**.

- **Status:** 86 Open (71.7%) · 34 Closed (28.3%)
- **Total applicants:** 10,376 (avg **86.5 per req**)
- **Total offers extended:** 20
- **Average days-to-hire (12 filled reqs):** 65.9 days
- **Average days open:** 86.1 days

**Sourcing channels:** LinkedIn (23), Recruiter (23), Career Fair (21), Indeed (21),
Company Website (17), Referral (15).
**Priority mix:** Low (43), Medium (39), High (38).

Sample requisitions:

| Req ID | Title | Department | Status | Applicants | Offers | Days Open | Source |
|---|---|---|---|---:|---:|---:|---|
| REQ-00001 | Sales Manager | Legal & Compliance | Open | 140 | 0 | 126 | Company Website |
| REQ-00002 | Sales Manager | Executive Leadership | Closed | 131 | 0 | 57 | Career Fair |
| REQ-00003 | Production Supervisor | Manufacturing | Open | 132 | 0 | 20 | Career Fair |
| REQ-00004 | Financial Analyst | Human Resources | Open | 121 | 0 | 137 | LinkedIn |

---

## 6. Training & Development

**300 training records** dated **2023-10-23 → 2025-10-21**.

- **Status:** 251 Completed · 29 In Progress · 20 Scheduled → **completion rate 83.7%**
- **Total training spend:** $596,811.37 (avg **$1,989.37 per record**)
- **Total training hours:** 4,722 (avg 15.7 hrs per record)
- **Average score (completed):** 85.0
- **Certifications earned:** 69 of 300 (23.0%)
- **Mandatory courses:** 34 (11.3%); the remaining 266 are elective/development

**Training types:** Onboarding (39), Leadership Development (38), Industry Certification (36),
Project Management (36), Compliance Training (34), Safety Training (33), Technical Skills (30),
Communication Skills (29), Software Tools (25).
**Delivery methods:** Virtual (93), Hybrid (75), Self-Paced Online (66), In-Person (66).

Sample records:

| ID | Course | Type | Hours | Cost | Status | Score | Mandatory |
|---|---|---|---:|---:|---|---:|---|
| TRN-000001 | Robotics Certification | Industry Certification | 40 | $4,511.12 | Completed | 91.8 | No |
| TRN-000002 | OSHA Safety | Compliance Training | 24 | $1,291.39 | Completed | 82.6 | Yes |
| TRN-000003 | Scrum Master Training | Project Management | 24 | $4,488.48 | Completed | 71.7 | No |
| TRN-000004 | Robotics Certification | Industry Certification | 2 | $158.80 | Completed | 89.4 | No |

---

*Generated from synthetic HR CSV extracts. Figures computed directly from source files.*
