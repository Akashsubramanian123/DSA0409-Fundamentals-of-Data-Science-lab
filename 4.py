import numpy as np
import matplotlib.pyplot as plt
sales_data = np.array([250000, 275000, 300000, 400000])
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
plt.figure(figsize=(10, 5))
plt.bar(quarters, sales_data, color='skyblue', label='Quarterly Sales')
plt.plot(quarters, sales_data, color='darkblue', marker='o', linestyle='-', label='Sales Trend')
for i, value in enumerate(sales_data):
    plt.text(i, value + 10000, f"₹{value//1000}k", ha='center', fontsize=10)
plt.title("Company Sales Performance Over Four Quarters")
plt.xlabel("Quarter")
plt.ylabel("Sales (₹)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
print("Quarterly Sales Data:", sales_data)
print(f"\nTotal Sales for the Year: ₹{total_sales:,}")
print(f"Percentage Increase from Q1 to Q4: {percentage_increase:.2f}%")