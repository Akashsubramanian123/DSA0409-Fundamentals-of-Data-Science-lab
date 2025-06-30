import pandas as pd
import matplotlib.pyplot as plt
data = {
    'product_name': ['Phone', 'Laptop', 'Phone', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Monitor', 'Phone', 'Laptop'],
    'quantity_sold': [3, 2, 4, 5, 1, 1, 3, 2, 2, 2],
    'price':         [15000, 60000, 15000, 500, 1000, 60000, 500, 7000, 15000, 60000]  # price per unit
}
sales_data = pd.DataFrame(data)
product_quantity = sales_data.groupby('product_name')['quantity_sold'].sum()
top_5_quantity = product_quantity.sort_values(ascending=False).head(5)
sales_data['revenue'] = sales_data['quantity_sold'] * sales_data['price']
product_revenue = sales_data.groupby('product_name')['revenue'].sum()
top_5_revenue = product_revenue.sort_values(ascending=False).head(5)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
top_5_quantity.plot(kind='bar', color='skyblue')
plt.title("Top 5 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.subplot(1, 2, 2)
top_5_revenue.plot(kind='bar', color='orange')
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
print("\n🔝 Top 5 Products by Quantity Sold:")
print(top_5_quantity)
print("\n💰 Top 5 Products by Revenue:")
print(top_5_revenue)