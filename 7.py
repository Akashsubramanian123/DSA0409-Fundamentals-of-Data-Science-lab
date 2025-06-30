import pandas as pd
import matplotlib.pyplot as plt
data = {
    'customer_id': [101, 102, 101, 103, 102, 101, 104],
    'order_date': ['2024-01-10', '2024-01-12', '2024-01-15', '2024-02-01', '2024-02-10', '2024-03-05', '2024-03-10'],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Mouse', 'Laptop', 'Monitor', 'Keyboard'],
    'order_quantity': [1, 2, 1, 3, 1, 2, 1]
}
order_data = pd.DataFrame(data)
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
orders_per_customer = order_data.groupby('customer_id').size()
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()
print("1. Total Orders per Customer:\n", orders_per_customer, "\n")
print("2. Average Order Quantity per Product:\n", avg_quantity_per_product, "\n")
print("3. Order Date Range:")
print("   Earliest:", earliest_date.strftime('%Y-%m-%d'))
print("   Latest:", latest_date.strftime('%Y-%m-%d'))
product_sales = order_data.groupby('product_name')['order_quantity'].sum()
top_selling = product_sales.sort_values(ascending=False)
print("Top-Selling Products:\n")
print(top_selling)
top_selling.plot(kind='bar', color='skyblue')
plt.title("Top-Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()