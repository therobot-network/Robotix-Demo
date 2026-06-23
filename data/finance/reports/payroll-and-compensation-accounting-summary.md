# Payroll & Compensation Accounting Summary

_Robotix Technologies — Internal Finance Data Summary_

This report summarizes payroll liabilities, compensation accruals, payroll-tax filings, stock compensation, benefits liabilities, and workers' compensation claims, drawn from the files in `compensation/`. All figures are computed directly from the source files. Data is 100% synthetic.

## Payroll Liability Ledger

The payroll liability ledger spans **480 monthly department records, 2021-11 through 2025-09**, across **10 departments**.

| Metric | Value |
| --- | --- |
| Total gross wages | $18,561,084.00 |
| Total payroll taxes | $2,032,439.04 |
| Total benefits | $2,948,564.96 |
| Total compensation cost | $25,669,214.72 |
| Average cost per employee (per record) | $7,443.26 |

### Total Compensation Cost by Department

| Department | Total Comp Cost |
| --- | --- |
| Finance | $5,085,586.85 |
| IT & Systems | $4,211,919.23 |
| Legal & Compliance | $4,126,203.11 |
| Product Development | $2,836,564.98 |
| Quality Assurance | $2,584,000.07 |
| Sales & Marketing | $1,838,386.12 |
| Manufacturing | $1,459,240.65 |
| Executive Leadership | $1,412,455.00 |
| Customer Service | $1,408,311.87 |
| Human Resources | $706,546.84 |

## Compensation Accruals

The accruals file holds **160 quarterly department records across 16 quarters (2021-2025)**.

| Metric | Value |
| --- | --- |
| Total accrued | $6,564,359.06 |
| Total paid | $1,478,205.77 |
| Net change in accruals | $5,086,153.18 |
| Bonus pool accrued | $2,123,958.88 |
| Vacation liability accrued | $1,484,886.72 |
| Severance expense | $1,855,981.34 |

### Representative Accrual Rows

| Accrual | Quarter | Department | Total Accrued | Total Paid |
| --- | --- | --- | --- | --- |
| ACC-000001 | Q4 2021 | Executive Leadership | $18,004.29 | $8,274.06 |
| ACC-000002 | Q4 2021 | Human Resources | $7,419.96 | $3,489.68 |

## Payroll Tax Schedule

The payroll-tax schedule covers **16 quarters, Q1 2022 through Q4 2024**, filed on Forms 941/940.

| Metric | Value |
| --- | --- |
| Total gross payroll | $121,012,724.41 |
| Total employer taxes | $16,787,597.33 |
| Total employee withholdings | $33,813,094.24 |
| Total tax liability | $50,600,691.57 |

Filing status: **15 Paid, 1 Pending**.

## Stock Compensation

There are **30 active equity grants** on the schedule.

| Grant Type | Grants |
| --- | --- |
| Restricted Stock Units (RSUs) | 16 |
| Stock Options | 7 |
| Performance Shares | 7 |

| Metric | Value |
| --- | --- |
| Shares granted | 287,635 |
| Vested shares | 196,477 |
| Unvested shares | 91,158 |
| Total grant value | $3,709,100.83 |
| Expense recognized to date | $2,758,836.00 |
| Remaining expense to recognize | $950,264.84 |
| Current intrinsic value | $2,298,064.13 |

### Representative Grant Rows

| Grant | Employee | Type | Shares | Total Value | Recognized |
| --- | --- | --- | --- | --- | --- |
| EQT-00001 | Sarah Chen (CEO) | Stock Options | 39,291 | $263,879.02 | $253,617.06 |
| EQT-00002 | Michael Rodriguez (CFO) | RSUs | 28,836 | $369,075.44 | $303,205.72 |

## Benefits Liability Schedule

The schedule lists **12 active benefit programs** (the file also includes a roll-up "Total All Benefits" row, excluded from the line totals below).

| Metric | Value |
| --- | --- |
| Total annual employer cost | $3,207,456.00 |
| Total annual employee contribution | $532,176.00 |
| Total annual cost | $3,739,632.00 |
| Total accrued liability | $451,159.76 |

### Selected Benefit Programs

| Benefit | Annual Cost | Accrued Liability | Participation |
| --- | --- | --- | --- |
| Health Insurance | $2,032,800 | $246,871.64 | 88.0% |
| 401(k) Employer Match | $949,200 | $130,817.45 | 78.0% |
| Dental Insurance | $162,000 | $10,292.78 | 82.0% |
| Life Insurance | $121,800 | $13,466.56 | 100.0% |
| Gym Membership Subsidy | $108,900 | $10,438.03 | 42.0% |

Health insurance and the 401(k) match account for the large majority of benefit cost and accrued liability.

## Workers' Compensation Claims

The claims log holds **87 claims, incidents from 2019-11-16 to 2025-08-22**.

| Metric | Value |
| --- | --- |
| Total claim cost | $2,151,453.25 |
| Total medical costs | $1,402,741.07 |
| Total lost wages paid | $629,208.52 |
| Total reserve amount | $124,947.14 |
| Average cost per claim | $24,729.35 |
| Total days away from work | 2,309 |

| Severity | Claims |  | Status | Claims |
| --- | --- | --- | --- | --- |
| Moderate | 44 |  | Closed | 62 |
| Serious | 27 |  | Settled | 20 |
| Minor | 16 |  | Open | 3 |
|  |  |  | Under Review | 2 |

### Claim Cost by Department (top 5)

| Department | Total Claim Cost |
| --- | --- |
| Human Resources | $330,769.10 |
| Finance | $268,907.77 |
| Sales & Marketing | $226,678.41 |
| Customer Service | $221,117.75 |
| Product Development | $219,374.82 |

## Headline Figures

- **Total compensation cost (payroll ledger): $25,669,214.72** across 480 monthly records.
- **Total payroll tax liability (2022-2024): $50,600,691.57.**
- **Net compensation accrual liability change: $5,086,153.18.**
- **Stock comp total grant value: $3,709,100.83** ($950,264.84 expense remaining).
- **Workers' comp claims total cost: $2,151,453.25** across 87 claims.
