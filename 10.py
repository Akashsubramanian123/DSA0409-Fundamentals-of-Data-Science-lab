import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12000, 15000, 17000, 16000, 18000, 20000,
         22000, 21000, 19000, 23000, 25000, 24000]
max_idx = sales.index(max(sales))
min_idx = sales.index(min(sales))
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.plot(months[max_idx], sales[max_idx], 'go', label='Highest')
plt.plot(months[min_idx], sales[min_idx], 'ro', label='Lowest')
plt.text(months[max_idx], sales[max_idx]+1000, f"₹{sales[max_idx]}", color='green', ha='center')
plt.text(months[min_idx], sales[min_idx]-2000, f"₹{sales[min_idx]}", color='red', ha='center')
plt.title("Monthly Sales Line Plot with Highlights")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
bar_colors = ['orange'] * len(months)
bar_colors[max_idx] = 'green'
bar_colors[min_idx] = 'red'
bars = plt.bar(months, sales, color=bar_colors, edgecolor='black')
plt.text(months[max_idx], sales[max_idx]+1000, f"₹{sales[max_idx]}", color='green', ha='center')
plt.text(months[min_idx], sales[min_idx]+1000, f"₹{sales[min_idx]}", color='red', ha='center')
plt.title("Monthly Sales Bar Plot with Highlights")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()