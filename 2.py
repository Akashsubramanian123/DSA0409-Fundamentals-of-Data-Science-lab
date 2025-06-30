import numpy as np
import matplotlib.pyplot as plt

# Sample 3x3 sales data matrix (rows = products, columns = individual sales)
sales_data = np.array([
    [100, 120, 110],  # Product 1
    [90,  95, 100],   # Product 2
    [130, 140, 135]   # Product 3
])

# Product labels
products = ['Product 1', 'Product 2', 'Product 3']

# 1. Calculate average price of all products sold
average_price = np.mean(sales_data)

# 2. Find the highest price among all sales
highest_price = np.max(sales_data)

# 3. Calculate total revenue per product
total_revenue = np.sum(sales_data, axis=1)

# 4. Plot total revenue per product
plt.figure(figsize=(8, 5))
bars = plt.bar(products, total_revenue, color='mediumseagreen')

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'₹{yval}', ha='center', fontsize=10)

plt.title("Total Revenue per Product")
plt.xlabel("Products")
plt.ylabel("Revenue (₹)")
plt.ylim(0, max(total_revenue) + 50)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Print outputs
print("Sales Data:\n", sales_data)
print(f"\nAverage price of all products sold: ₹{average_price:.2f}")
print(f"Highest price among all sales: ₹{highest_price:.2f}")
print("\nTotal Revenue per Product:")
for product, revenue in zip(products, total_revenue):
    print(f"{product}: ₹{revenue}")
