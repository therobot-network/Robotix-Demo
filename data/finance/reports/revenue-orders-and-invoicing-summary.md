# Revenue, Orders & Invoicing Summary

_Robotix Technologies — Internal Finance Data Summary_

This report summarizes the order book, product-line revenue, and customer invoicing activity captured in `orders/orders.csv`, `orders/order_items.csv`, and `invoices/invoices.csv`. All figures are computed directly from the source files. Data is 100% synthetic.

## Orders Overview

| Metric | Value |
| --- | --- |
| Orders | 1,000 |
| Date range | 2023-01-02 to 2024-12-30 |
| Gross order value (sum of `total`) | $68,778,010.12 |
| Subtotal | $67,514,939.00 |
| Discounts applied | $4,157,125.00 |
| Tax | $5,401,195.12 |
| Shipping | $19,001.00 |
| Average order total | $68,778.01 |
| Median order total | $56,692.10 |

### Order Status Breakdown

| Status | Orders |
| --- | --- |
| Completed | 494 |
| Cancelled | 178 |
| Shipped | 177 |
| In Production | 151 |

### Sales Channel

| Channel | Orders |
| --- | --- |
| Direct Sales | 404 |
| Partner | 206 |
| Online | 196 |
| Phone | 194 |

### Payment Method & Terms

| Payment Method | Orders |  | Payment Terms | Orders |
| --- | --- | --- | --- | --- |
| Purchase Order | 401 |  | Prepaid | 318 |
| Financing | 211 |  | Net 30 | 185 |
| Credit Card | 206 |  | 50/50 | 179 |
| Wire Transfer | 182 |  | Financing 24mo | 168 |
|  |  |  | Net 60 | 150 |

### Top Sales Representatives (by order value)

| Sales Rep | Order Value |
| --- | --- |
| David Martinez | $24,946,182.36 |
| Chris Patel | $22,206,987.32 |
| Jessica Martinez | $21,624,840.44 |

### Top States (by shipped order value)

| State | Order Value |
| --- | --- |
| CO | $9,864,185.56 |
| WA | $9,538,854.64 |
| OR | $9,206,393.56 |
| MI | $9,037,789.20 |
| MA | $8,705,509.40 |

## Product-Line Revenue (Order Items)

The `order_items.csv` file contains **3,460 line items** across **21 distinct products**, totaling **6,483 units** and **$67,514,939.00** in line revenue (matching the order subtotal).

### Top 10 Products by Revenue

| SKU | Product | Revenue | Units | Lines |
| --- | --- | --- | --- | --- |
| RBX-IND-1001 | HeavyDuty Articulated Robot | $7,656,486 | 159 | 159 |
| RBX-IND-1002 | HighSpeed Assembly Robot | $7,117,874 | 167 | 167 |
| RBX-COL-1004 | CoBot Assistant 5kg | $6,100,412 | 188 | 188 |
| RBX-IND-1000 | PrecisionArm 6-Axis | $5,743,624 | 152 | 152 |
| RBX-IND-1003 | Welding Robot Pro | $5,031,516 | 172 | 172 |
| RBX-MOB-1010 | PalletMover Robot | $4,283,303 | 149 | 149 |
| RBX-COL-1005 | CoBot Precision 10kg | $4,279,410 | 170 | 170 |
| RBX-MOB-1011 | Inspection Rover | $3,846,620 | 164 | 164 |
| RBX-COL-1007 | CoBot Dual-Arm System | $3,781,256 | 158 | 158 |
| RBX-COL-1006 | CoBot Mobile Platform | $3,372,432 | 168 | 168 |

Revenue is concentrated in the Industrial (RBX-IND) and Collaborative (RBX-COL) product families, with the top five SKUs accounting for over $31.6M of line revenue.

## Customer Invoicing

| Metric | Value |
| --- | --- |
| Invoices | 200 |
| Date range | 2023-01-13 to 2024-12-29 |
| Total invoiced | $13,100,226.76 |
| Average invoice | $65,501.13 |

### Payment Status Breakdown

| Status | Invoices | Amount |
| --- | --- | --- |
| Paid | 125 | $8,360,657.80 |
| Pending | 43 | $2,559,537.16 |
| Overdue | 32 | $2,180,031.80 |

Roughly 62.5% of invoices (representing $8.36M) are paid; the remaining $4.74M is split between pending and overdue balances.

### Invoice Payment Method

| Payment Method | Invoices |
| --- | --- |
| Purchase Order | 84 |
| Financing | 46 |
| Wire Transfer | 35 |
| Credit Card | 35 |

### Representative Invoice Rows

| Invoice | Customer | Order | Total | Status |
| --- | --- | --- | --- | --- |
| INV-20240001 | CUST10291 | ORD100088 | $5,702.04 | Paid |
| INV-20240002 | CUST10380 | ORD100184 | $144,949.56 | Paid |

## Headline Figure

**Gross order value across 1,000 orders (2023-2024): $68,778,010.12**, with $13.1M formally invoiced and $8.36M collected.
