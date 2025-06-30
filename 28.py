import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Simulated dataset of 10 customers: [annual_spending, monthly_visits, avg_cart_value]
X = np.array([
    [50, 2, 3],
    [80, 5, 5],
    [20, 1, 2],
    [60, 4, 4],
    [25, 2, 2],
    [90, 6, 6],
    [30, 1, 3],
    [100, 7, 7],
    [40, 3, 3],
    [85, 5, 5.5]
])

# 2. Train K-Means model (k = 3 clusters)
k = 3
model = KMeans(n_clusters=k, random_state=42)
model.fit(X)

# 3. Input new customer data
try:
    print("\n🛍️ Enter details of the new customer:")
    annual_spending = float(input("Annual Spending (in ₹000s): "))
    monthly_visits = int(input("Monthly Visits: "))
    avg_cart_value = float(input("Average Cart Value (in ₹000s): "))

    new_customer = np.array([[annual_spending, monthly_visits, avg_cart_value]])
except:
    print("❌ Invalid input.")
    exit()

# 4. Predict cluster/segment
cluster = model.predict(new_customer)[0]
print(f"\n📊 This customer belongs to segment (cluster): {cluster}")

# 5. (Optional) Plot customers and the new point
plt.scatter(X[:, 0], X[:, 2], c=model.labels_, cmap='viridis', s=100, alpha=0.6, label="Existing Customers")
plt.scatter(new_customer[0][0], new_customer[0][2], color='red', s=150, marker='X', label="New Customer")
plt.xlabel("Annual Spending (₹000s)")
plt.ylabel("Avg Cart Value (₹000s)")
plt.title("Customer Segmentation (K-Means)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
