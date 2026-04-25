import pandas as pd

customers = pd.read_csv('customers.csv')
monthly_revenue = pd.read_csv('monthly_revenue.csv')
orders = pd.read_csv('orders.csv')
product_summary = pd.read_csv('product_summary.csv')

print(f"Shape: {customers.shape}")
print(f"Columns: {customers.columns.tolist()}")

print(f"Shape: {monthly_revenue.shape}")
print(f"Columns: {monthly_revenue.columns.tolist()}")

print(f"Shape: {orders.shape}")
print(f"Columns: {orders.columns.tolist()}")

print(f"Shape: {product_summary.shape}")
print(f"Columns: {product_summary.columns.tolist()}")

print("\nCustomers missing values:")
print(customers.isnull().sum())

print("\nMonthly Revenue missing values:")
print(monthly_revenue.isnull().sum())

print("\nOrders missing values:")
print(orders.isnull().sum())

print("\nProduct Summary missing values:")
print(product_summary.isnull().sum())

customers['registration_date'] = pd.to_datetime(customers['registration_date'])
orders['order_date'] = pd.to_datetime(orders['order_date'])

customers.to_csv('outputs/customers_cleaned.csv', index=False)
orders.to_csv('outputs/orders_cleaned.csv', index=False)
product_summary.to_csv('outputs/product_summary_cleaned.csv', index=False)
monthly_revenue.to_csv('outputs/monthly_revenue_cleaned.csv', index=False)

print("Cleaning complete.")