# AR/AP, Cash Flow, Debt & Vendors Summary

_Robotix Technologies — Internal Finance Data Summary_

This report summarizes working-capital aging, the monthly cash-flow trend, the outstanding debt schedule, and vendor spend, drawn from `ar_ap/accounts_receivable_aging.csv`, `ar_ap/accounts_payable_aging.csv`, `cash_flow/monthly_cash_flow.csv`, `debt/debt_schedule.csv`, `vendors/vendor_master.csv`, and `vendors/vendor_spend.csv`. All figures are computed directly from the source files. Data is 100% synthetic.

## Accounts Receivable Aging

The AR aging file lists **75 outstanding invoices** dated 2023-01-14 to 2024-12-28, totaling **$4,739,568.96**. Notably, every open invoice has aged into the **90+ days** bucket and carries a **High** risk rating.

| Aging Bucket | Invoices | Amount |
| --- | --- | --- |
| 90+ days | 75 | $4,739,568.96 |

| Payment Status | Invoices |
| --- | --- |
| Pending | 43 |
| Overdue | 32 |

Total overdue AR is **$4,739,568.96** — the full balance is past due, signaling a collections concern.

### Representative AR Rows

| Invoice | Customer | Amount | Days Overdue | Risk |
| --- | --- | --- | --- | --- |
| INV-20240004 | CUST10100 | $77,176.08 | 774 | High |
| INV-20240007 | CUST10135 | $19,861.20 | 332 | High |

## Accounts Payable Aging

The AP aging file lists **150 open vendor invoices** totaling **$11,971,681.86**. Of these, 94 are Overdue and 56 Scheduled.

| Aging Bucket | Invoices | Amount |
| --- | --- | --- |
| 0-30 days | 46 | $3,544,923.86 |
| 31-60 days | 35 | $2,931,235.84 |
| 61-90 days | 36 | $2,721,198.52 |
| 90+ days | 33 | $2,774,323.64 |

### Top AP by Category

| Category | Amount |
| --- | --- |
| Software Vendor | $2,790,707.66 |
| Logistics Provider | $1,892,595.25 |
| Component Supplier | $1,815,342.75 |
| Facility Services | $1,646,247.92 |
| Professional Services | $997,651.80 |

### Top Vendors by Payable Balance

| Vendor | Balance |
| --- | --- |
| DataGuard Security | $1,114,390.01 |
| Atlas Logistics | $1,056,054.26 |
| Innovation Labs | $997,651.80 |
| Premier Insurance Group | $945,250.29 |
| Strategic Advisors LLC | $871,976.52 |

## Monthly Cash Flow

The cash-flow file covers **24 months, 2023-11 through 2025-09**.

| Metric | Value |
| --- | --- |
| Beginning cash (first month) | $8,500,000.00 |
| Ending cash (last month) | $23,678,103.31 |
| Total revenue collected | $91,624,941.40 |
| Total operating expenses paid | $(77,216,515.59) |
| Total operating cash flow | $17,571,220.32 |
| Total investing cash flow | $(1,927,375.81) |
| Total capital expenditures | $(2,132,232.93) |
| Total financing cash flow | $(465,741.19) |
| Net cash change (cumulative) | $15,178,103.32 |
| Average days cash on hand | 155.3 |
| Ending cash range | $9,211,242.49 – $23,678,103.31 |

Cash position grew strongly over the period — ending cash rose ~178% from the opening balance, driven by $17.6M of cumulative operating cash flow against modest investing and financing outflows.

### Representative Cash-Flow Rows

| Month | Beginning Cash | Operating CF | Ending Cash | Days Cash |
| --- | --- | --- | --- | --- |
| 2023-11 | $8,500,000.00 | $761,702.71 | $9,211,242.49 | 83.7 |
| 2023-12 | $9,211,242.49 | $833,878.03 | $9,945,243.09 | 95.5 |

## Debt Schedule

Three active facilities are outstanding (a SUMMARY row in the file restates the totals below).

| Loan | Type | Lender | Outstanding | Rate | Monthly Pmt | Maturity |
| --- | --- | --- | --- | --- | --- | --- |
| LOAN-001 | Term Loan | First National Bank | $3,200,000 | 5.25% | $47,500 | 2027-03-15 |
| LOC-001 | Line of Credit | Pacific Business Bank | $800,000 | 6.75% | $0 | 2025-01-10 |
| LOAN-002 | Equipment Financing | Industrial Equipment Finance | $650,000 | 4.95% | $18,500 | 2028-06-01 |

| Metric | Value |
| --- | --- |
| Original principal (active) | $8,200,000 |
| Total outstanding balance | $4,650,000 |
| Total monthly payment | $66,000 |
| Interest-rate range | 4.95% – 6.75% |
| Weighted-average rate (by balance) | 5.47% |

## Vendors

The vendor master lists **15 vendors** across 9 categories (Component Supplier and Software Vendor each have 3). Vendor spend is tracked monthly over **2023-11 to 2025-09** across **360 rows**.

| Metric | Value |
| --- | --- |
| Total vendor spend | $25,392,930.29 |
| Total invoices | 1,654 |
| Average on-time payment rate | 92.7% |

### Top Vendors by Total Spend

| Vendor | Total Spend |
| --- | --- |
| Industrial Sensors Co | $4,933,950.85 |
| TechMotion Systems | $4,786,019.31 |
| Precision Components Inc | $4,538,936.19 |
| Atlas Logistics | $1,372,489.76 |
| Global Freight Services | $1,279,673.12 |
| BuildRight Construction | $963,027.94 |
| Bright Marketing Group | $911,821.73 |
| Innovation Labs | $889,306.14 |

### Spend by Category

| Category | Total Spend |
| --- | --- |
| Component Supplier | $14,258,906.35 |
| Logistics Provider | $2,652,162.88 |
| Software Vendor | $2,435,962.44 |
| Facility Services | $1,747,431.94 |
| Marketing Agency | $911,821.73 |
| Professional Services | $889,306.14 |
| Equipment Supplier | $866,686.55 |
| Consulting | $849,483.35 |
| Insurance Provider | $781,168.91 |

Component suppliers dominate vendor spend (~56% of the total), reflecting the company's robotics manufacturing supply chain.

## Headline Figures

- **Total AP outstanding: $11,971,681.86** (150 invoices; 94 overdue).
- **Total AR outstanding: $4,739,568.96** (all 90+ days / High risk).
- **Total debt outstanding: $4,650,000** at a 5.47% weighted-average rate.
- **Total vendor spend (24 months): $25,392,930.29.**
