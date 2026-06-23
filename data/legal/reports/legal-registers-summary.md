# Robotix Technologies — Legal Registers Summary

**Company:** Robotix Technologies (fictional, IT-led enterprise technology and robotics/automation company)
**HQ:** Bothell, Washington · **Founded:** 1998 · **Employees:** ~290
**Report date:** 2026-06-23
**Source data:** 100% synthetic. This report summarizes four legal registers so the underlying CSVs can be archived/deleted.

This summary captures the key statistics from the Contracts, Compliance, Intellectual Property, and Litigation registers. All figures below are computed directly from the source CSV files.

---

## Contracts Register

**Source:** `contracts/contract_register.csv` · **Total records:** 100

- **Total contract value:** $46,730,607.64
- **Active contract value:** $35,116,069.15
- **Auto-renew enabled:** 46 contracts (Yes) vs. 54 (No)
- **Effective dates range:** 2022-11-04 to 2025-09-14
- **Expiration dates range:** 2023-11-04 to "At-Will" (open-ended employment agreements)

**By status**

| Status | Count |
|---|---|
| Active | 72 |
| Expired | 10 |
| Terminated | 9 |
| Renewed | 5 |
| Expiring Soon | 4 |

**By risk level:** Medium 40 · Low 37 · High 23

**Top contract types**

| Contract Type | Count |
|---|---|
| Distribution Agreement | 16 |
| Equipment Purchase Agreement | 13 |
| Consulting Services Agreement | 12 |
| Partnership Agreement | 11 |
| Non-Disclosure Agreement (NDA) | 9 |
| Employment Agreement | 9 |
| Software License Agreement | 8 |
| Lease Agreement | 8 |
| Supply Agreement | 8 |
| Master Service Agreement | 6 |

**Representative records**

| ID | Type | Counterparty | Value ($) | Status | Risk | Expires |
|---|---|---|---|---|---|---|
| CTR-00001 | Software License Agreement | Healthcare Provider #710 | 69,538.20 | Active | Low | 2026-07-28 |
| CTR-00002 | Master Service Agreement | Tech Startup #837 | 322,066.44 | Active | Low | 2029-02-22 |
| CTR-00003 | Master Service Agreement | Government Agency #275 | 455,480.94 | Renewed | Medium | 2025-09-14 |
| CTR-00004 | Distribution Agreement | Government Agency #785 | 209,261.41 | Expired | High | 2024-07-06 |
| CTR-00005 | Software License Agreement | Retail Chain #495 | 38,961.43 | Active | Medium | 2026-12-15 |

---

## Compliance Register

**Source:** `compliance/compliance_register.csv` · **Total records:** 60

- **Distinct compliance areas:** 10 (e.g., SOX Financial Controls, EPA Environmental, Employment Law, Export Control (ITAR/EAR), ISO 9001 Quality)
- **Total findings:** 68 · **Critical findings:** 5
- **Average last audit score:** 86.4
- **Review dates range:** last reviews back to 2024-10-23; next reviews scheduled through 2026-10-07

**By status**

| Status | Count |
|---|---|
| Compliant | 44 |
| Minor Issues | 7 |
| Action Required | 7 |
| Under Review | 2 |

**Certification status:** Certified 21 · In Progress 10 · Renewal Due 7 (remaining records marked N/A)

**Representative records**

| ID | Area | Regulator | Status | Findings | Audit Score | Next Review |
|---|---|---|---|---|---|---|
| CMP-00001 | SOX Financial Controls | SEC | Minor Issues | 3 | 86.8 | 2025-08-04 |
| CMP-00002 | EPA Environmental | EPA | Action Required | 2 | 85.0 | 2025-07-27 |
| CMP-00003 | Employment Law | DOL/EEOC | Action Required | 4 | 82.7 | 2025-05-16 |
| CMP-00004 | Export Control (ITAR/EAR) | State Dept/Commerce | Compliant | 0 | 86.5 | 2025-08-17 |
| CMP-00005 | ISO 9001 Quality | ISO | Compliant | 0 | 99.6 | 2025-05-05 |

---

## Intellectual Property

**Source:** `intellectual_property.csv` · **Total records:** 19

- **Portfolio mix:** 15 Patents · 4 Trademarks
- **Total estimated portfolio value:** $7,141,964.38
- **Total annual maintenance cost:** $96,036.16
- **Filing dates range:** 2018-08-29 to 2024-07-27

**By status**

| Status | Count |
|---|---|
| Granted | 6 |
| Pending | 5 |
| Abandoned | 4 |
| Registered | 4 |

**By jurisdiction:** US 6 · JP 5 · International (PCT) 3 · CN 3 · EU 2

**Representative records**

| ID | Type | Title | Status | Jurisdiction | Value Est. ($) |
|---|---|---|---|---|---|
| PAT-001 | Patent | Robotic System Innovation 1 | Granted | International (PCT) | 482,353.10 |
| PAT-002 | Patent | Robotic System Innovation 2 | Abandoned | International (PCT) | 167,803.13 |
| PAT-003 | Patent | Robotic System Innovation 3 | Abandoned | CN | 467,713.27 |
| PAT-004 | Patent | Robotic System Innovation 4 | Pending | JP | 485,743.91 |
| PAT-006 | Patent | Robotic System Innovation 6 | Granted | EU | 182,159.18 |

---

## Litigation Register

**Source:** `litigation/litigation_register.csv` · **Total records:** 25

- **Open matters (not Closed):** 21 — of which 12 are currently **Active**
- **Total legal costs to date:** $6,662,859.28
- **Total settlement amounts:** $1,731,012.08
- **Total potential exposure:** $13,529,371.38
- **Filed dates range:** 2023-05-17 to 2025-08-14
- **Plaintiff split:** Robotix 13 · Third Party 12

**By status**

| Status | Count |
|---|---|
| Active | 12 |
| Settled | 7 |
| Closed | 4 |
| Dismissed | 2 |

**By priority:** High 13 · Medium 7 · Low 5

**By case type**

| Case Type | Count |
|---|---|
| Customer Complaint | 6 |
| Patent Infringement | 4 |
| Product Liability | 4 |
| Vendor Dispute | 3 |
| Regulatory Compliance | 2 |
| Employment Dispute | 2 |
| Intellectual Property | 2 |
| Contract Dispute | 2 |

**Representative records**

| ID | Type | Status | Plaintiff | Priority | Legal Costs ($) | Exposure ($) |
|---|---|---|---|---|---|---|
| LIT-0001 | Patent Infringement | Settled | Robotix | High | 57,209.45 | — |
| LIT-0002 | Patent Infringement | Settled | Third Party | Medium | 41,790.86 | — |
| LIT-0003 | Regulatory Compliance | Closed | Third Party | High | 186,608.95 | — |
| LIT-0004 | Customer Complaint | Active | Third Party | High | 184,649.27 | 50,617.18 |
| LIT-0005 | Customer Complaint | Active | Third Party | Medium | 905,234.08 | 1,623,224.56 |

---

*All data is synthetic and generated for demonstration purposes only. Figures are computed directly from the source CSV registers as of 2026-06-23.*
