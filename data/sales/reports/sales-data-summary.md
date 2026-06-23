# Robotix Technologies — Sales Data Summary

**Company:** Robotix Technologies (fictional IT-led enterprise technology &
robotics/automation company)
**HQ:** Bothell, Washington
**Report generated:** 2026-06-23
**Status:** All data is 100% synthetic.

This report summarizes the four sales CSV datasets so the underlying CSV files
can be retired. It consolidates the active pipeline, quarterly forecasts, rep
quota attainment, and outbound quotes. All figures below were computed directly
from the source CSVs (no estimates). Sales coverage is provided by three reps:
**Chris Patel**, **David Martinez**, and **Jessica Martinez**.

> The source files retained as raw data are `customers/customers.csv` (kept by
> design) and the four files summarized here:
> `pipeline/sales_pipeline.csv`, `forecasts/sales_forecasts.csv`,
> `quotas/quota_attainment.csv`, `quotes/sales_quotes.csv`.

---

## 1. Sales Pipeline

Source: `pipeline/sales_pipeline.csv` — **200 opportunities**.

- **Total pipeline value:** **$214,012,588.92**
- **Total weighted (probability-adjusted) value:** **$92,585,226.70**
- **Average deal size:** $1,070,062.94
- **Average opportunity age:** 190.3 days
- **Created-date range:** 2024-10-22 → 2025-10-21
- **Expected-close range:** 2025-01-06 → 2026-02-15
- **Win rate (Closed Won ÷ closed):** **62.7%** (32 won vs. 19 lost)

### Pipeline by stage

| Stage | Opps | Total Value ($) | Weighted Value ($) | Avg Prob % |
|---|---:|---:|---:|---:|
| Prospecting | 33 | 38,802,762 | 3,880,276 | 10 |
| Qualification | 27 | 31,114,936 | 6,222,987 | 20 |
| Needs Analysis | 30 | 34,420,737 | 13,768,295 | 40 |
| Proposal | 34 | 35,821,423 | 21,492,854 | 60 |
| Negotiation | 25 | 18,695,652 | 14,956,521 | 80 |
| Closed Won | 32 | 32,264,293 | 32,264,293 | 100 |
| Closed Lost | 19 | 22,892,786 | 0 | 0 |

### Owner, source, and product distribution

- **By owner:** Chris Patel 77, David Martinez 65, Jessica Martinez 58
- **By lead source:** Partner 45, Trade Show 44, Referral 42, Website 39, Cold Call 30
- **Product interest:** Industrial Robot System 47, Control Software License 46,
  Mobile Robot Platform 39, Collaborative Robot 34, Vision System 34
- **Competitors cited:** KUKA 51, FANUC 40, Universal Robots 37, ABB Robotics 30

### Representative opportunities

| Opp ID | Account | Stage | Prob % | Amount ($) | Owner | Product Interest |
|---|---|---|---:|---:|---|---|
| OPP-000001 | Company 3130 | Closed Lost | 0 | 1,576,068 | David Martinez | Control Software License |
| OPP-000002 | Company 7578 | Proposal | 60 | 1,017,696 | David Martinez | Industrial Robot System |
| OPP-000003 | Company 4619 | Needs Analysis | 40 | 1,183,603 | Chris Patel | Mobile Robot Platform |
| OPP-000004 | Company 4928 | Prospecting | 10 | 280,482 | Jessica Martinez | Collaborative Robot |
| OPP-000005 | Company 5725 | Proposal | 60 | 177,980 | Chris Patel | Mobile Robot Platform |
| OPP-000006 | Company 2181 | Needs Analysis | 40 | 1,034,126 | David Martinez | Mobile Robot Platform |

---

## 2. Forecasts

Source: `forecasts/sales_forecasts.csv` — **24 quarterly forecast records**
spanning **Q4 2023 → Q4 2024** (plus Q1–Q3 2025), across regions
International, Central, East, and West.

- **Total forecast amount:** **$16,302,625.59**
- **Total actual amount:** **$16,151,811.48**
- **Overall attainment (actual ÷ forecast):** **99.1%**
- **Average per-record attainment:** 101.2%
- **Total pipeline value referenced:** $50,175,145.07 (weighted $22,578,815.29)
- **Forecast category mix:** Pipeline 10, Commit 8, Best Case 6
- **Confidence mix:** High 9, Medium 7, Low 8

### Forecast vs. actual by region

| Region | Forecast ($) | Actual ($) | Avg Attainment % |
|---|---:|---:|---:|
| Central | 7,336,869 | 6,906,339 | 96.0 |
| East | 5,806,098 | 6,182,537 | 108.1 |
| International | 1,941,479 | 1,857,326 | 97.5 |
| West | 1,218,179 | 1,205,609 | 104.2 |

### Representative forecast rows

| Quarter | Rep | Region | Forecast ($) | Actual ($) | Attain % | Confidence |
|---|---|---|---:|---:|---:|---|
| Q4 2023 | David Martinez | International | 569,165 | 556,382 | 97.8 | High |
| Q4 2023 | Chris Patel | Central | 365,865 | 281,139 | 76.8 | High |
| Q4 2023 | Jessica Martinez | Central | 601,239 | 663,871 | 110.4 | Medium |
| Q1 2024 | David Martinez | Central | 529,406 | 530,623 | 100.2 | Medium |
| Q1 2024 | Chris Patel | Central | 1,064,372 | 983,095 | 92.4 | Medium |
| Q1 2024 | Jessica Martinez | International | 828,587 | 704,510 | 85.0 | High |

---

## 3. Quota Attainment (by Rep)

Source: `quotas/quota_attainment.csv` — **18 rep-quarter records** across
quarters Q2 2024 → Q3 2025 and teams Channel, Enterprise, and SMB.

- **Total quota:** **$13,557,581.06**
- **Total actual revenue:** **$14,052,637.48**
- **Overall attainment:** **103.7%** (avg per-record 104.0%)
- **Total deals closed:** 408
- **Total commission earned:** $856,074.52
- **Performance ratings:** Exceeds 7, Meets 6, Below 5

### Attainment by rep (all quarters combined)

| Rep | Quota ($) | Actual ($) | Avg Attain % | Deals | Commission ($) |
|---|---:|---:|---:|---:|---:|
| Chris Patel | 4,626,461 | 4,768,741 | 102.4 | 129 | 271,480 |
| David Martinez | 4,429,547 | 4,512,463 | 101.2 | 142 | 296,231 |
| Jessica Martinez | 4,501,574 | 4,771,433 | 108.4 | 137 | 288,364 |

Jessica Martinez leads on average attainment (108.4%); David Martinez closed the
most deals (142) and earned the most commission ($296,231). All three reps
collectively beat quota.

---

## 4. Quotes

Source: `quotes/sales_quotes.csv` — **150 quotes** issued 2024-10-24 → 2025-10-21.

- **Total quoted value:** **$39,330,443.63**
- **Total subtotal (pre-discount):** $40,151,066.37
- **Total discounts given:** $3,733,988.89
- **Average quote total:** $262,202.96
- **Average discount:** 9.4%
- **Average delivery lead time:** 9.7 weeks
- **Quote acceptance rate (Accepted ÷ decided):** **62.5%** (40 accepted vs. 24 rejected)

### Status breakdown

| Status | Count |
|---|---:|
| Sent | 40 |
| Accepted | 40 |
| Rejected | 24 |
| Viewed | 19 |
| Expired | 14 |
| Draft | 13 |

### Other distributions

- **Payment terms:** Net 45 (45), Net 60 (40), 50% Upfront (35), Net 30 (30)
- **By owner:** David Martinez 57, Chris Patel 49, Jessica Martinez 44

### Representative quotes

| Quote ID | Customer | Date | Subtotal ($) | Disc % | Total ($) | Status |
|---|---|---|---:|---:|---:|---|
| QUO-000001 | Company 6994 | 2025-08-04 | 400,173 | 0 | 432,187 | Rejected |
| QUO-000002 | Company 2356 | 2025-10-03 | 72,075 | 10 | 70,057 | Sent |
| QUO-000003 | Company 3229 | 2025-10-18 | 377,668 | 20 | 326,305 | Expired |
| QUO-000004 | Company 8466 | 2025-02-02 | 259,638 | 15 | 238,348 | Rejected |
| QUO-000005 | Company 3195 | 2025-03-21 | 209,853 | 5 | 215,309 | Sent |
| QUO-000006 | Company 4372 | 2025-04-12 | 307,319 | 15 | 282,119 | Sent |

---

## Notes

- Quote totals include tax, which is why some totals exceed subtotal when the
  discount is small or zero.
- Pipeline weighted value reflects per-stage probability; Closed Won is weighted
  at 100% and Closed Lost at 0%.
- Forecast and quota datasets cover overlapping but distinct time windows;
  forecast revenue and quota actuals are measured independently and are not
  expected to reconcile exactly.
- All names, companies, and figures are synthetic and for demonstration only.
