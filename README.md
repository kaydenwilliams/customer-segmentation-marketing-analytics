# Customer Segmentation & Marketing Analytics

## Overview
End-to-end customer analytics project analyzing 8,000 customers and 25,000 orders from an eCommerce platform (2020–2026). Uses RFM analysis and K-Means clustering to segment customers, identify product performance, and analyze churn behavior.

## Tools
Python, pandas, scikit-learn, matplotlib, Tableau

## Dataset
E-Commerce Customer Behavior & Sales (2020–2026) — Kaggle
8,000 customers, 25,000 orders, 14 product categories

## Business Questions
1. Who are our most valuable customers and what segments do they fall into?
2. Which product categories drive the most revenue and have the highest return rates?
3. What is the churn rate and what behavioral patterns predict customer churn?

## Key Findings
- K-Means clustering identified 4 customer segments — VIP (190 customers, avg spend $11,612), Loyal Mid-Tier (1,740), At-Risk (1,289), and New/Occasional (4,781)
- 59.8% of customers are New/Occasional — the largest conversion opportunity
- Electronics generated $1.08M in revenue — nearly 3x the next highest category
- Travel & Luggage had the highest return rate at 10.0% despite moderate revenue
- 8.9% overall churn rate — churned customers averaged 94.9 days since last purchase vs 56.1 days for active customers and spent 23.5% less ($1,218 vs $1,592)

## Business Recommendations
1. Launch a VIP retention program — 190 customers averaging $11,612 spend represent 
   disproportionate revenue; losing even 10% is a significant financial impact
2. Create re-engagement campaigns targeting the 1,289 At-Risk customers who haven't 
   purchased in 165 days on average
3. Investigate Travel & Luggage return rate — 10% return rate is the highest of any 
   category and directly erodes margin
4. Focus acquisition spend on converting New/Occasional buyers — at 59.8% of the base, even a 10% conversion to Loyal Mid-Tier would meaningfully grow revenue

## Files
- `clean.py` — data cleaning and datetime conversion
- `eda.py` — RFM analysis, K-Means clustering, product performance, churn analysis
- `outputs/customers_cleaned.csv` — cleaned customer dataset
- `outputs/orders_cleaned.csv` — cleaned orders dataset
- `outputs/rfm_segments.csv` — customer segments with RFM scores
- `outputs/category_performance.csv` — revenue and return rate by category
- `outputs/churn_analysis.csv` — churn behavioral comparison
- `outputs/customer_segments.png` — segment distribution chart
- `executive_summary.pdf` — plain English findings for non-technical stakeholders

## Tableau Dashboard
