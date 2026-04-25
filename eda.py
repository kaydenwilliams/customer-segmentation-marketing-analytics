import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

customers = pd.read_csv('outputs/customers_cleaned.csv')
orders = pd.read_csv('outputs/orders_cleaned.csv')
product_summary = pd.read_csv('outputs/product_summary_cleaned.csv')
monthly_revenue = pd.read_csv('outputs/monthly_revenue_cleaned.csv')

# Business Question 1: Customer Segmentation Using RFM
# RFM Analysis
rfm = customers[['customer_id', 'days_since_last_purchase', 'total_orders', 'total_spend_usd']].copy()
rfm.columns = ['customer_id', 'Recency', 'Frequency', 'Monetary']

print(rfm.describe())

# Scale RFM features
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# K-Means with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

print(rfm.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean().round(2))

# Labels for Clusters
cluster_labels = {
    0: 'Loyal Mid-Tier',
    1: 'At-Risk',
    2: 'VIP',
    3: 'New/Occasional'
}

rfm['Segment'] = rfm['Cluster'].map(cluster_labels)
print(rfm['Segment'].value_counts())

# Bar Chart Showing Customer Count By Segment
rfm.to_csv('outputs/rfm_segments.csv', index=False)

segment_counts = rfm['Segment'].value_counts()
segment_counts.plot(kind='bar', color=['#2196F3', '#FF9800', '#4CAF50', '#F44336'])
plt.title('Customer Segments by Count')
plt.xlabel('Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/customer_segments.png')
print("Segment chart saved.")

# Business Question 2: Product Performance
category_performance = product_summary.groupby('category').agg(
    total_revenue_usd=('total_revenue_usd', 'sum'),
    return_rate=('return_rate', 'mean')
).sort_values('total_revenue_usd', ascending=False).round(2)

print(category_performance)

# Business Quesion 3: Churn Analysis
# Churn Rate
customer_churn = customers['churned'].value_counts()
print(customer_churn)

# Why they churned (churned vs non across behavioral metics)
churn_analysis = customers.groupby('churned').agg(
    Avg_Days_Since_Purchase=('days_since_last_purchase', 'mean'),
    Avg_Orders=('total_orders', 'mean'),
    Avg_Spend=('total_spend_usd', 'mean'),
    Avg_Returns=('returns_made', 'mean')
).round(2)

print(churn_analysis)

# Save churn analysis
churn_analysis.to_csv('outputs/churn_analysis.csv')

# Churn rate print
churn_rate = round(715/8000*100, 1)
print(f"Overall churn rate: {churn_rate}%")

# Save category performance
category_performance.to_csv('outputs/category_performance.csv')

print("=== KEY FINDINGS ===")
print(f"VIP customers: 190 (2.4% of base), Avg spend: $11,612")
print(f"At-Risk customers: 1,289 (16.1% of base), Avg 165 days since purchase")
print(f"Electronics revenue: $1.08M — {round(1082575/2900000*100,1)}% of total revenue")
print(f"Churn rate: 8.9% — churned customers spent 23.5% less and had 69% longer purchase gaps")