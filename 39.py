import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simulate transaction data
np.random.seed(42)
n_customers = 300
data = {
    'CustomerID': range(1, n_customers + 1),
    'TotalSpent': np.random.normal(5000, 1500, n_customers).clip(500, None),
    'ItemsPurchased': np.random.poisson(10, n_customers)
}
df = pd.DataFrame(data)

# 2. Feature Scaling
features = df[['TotalSpent', 'ItemsPurchased']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# 3. K-Means Clustering
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(features_scaled)

# 4. Cluster Summary
print("\n🧩 Cluster Summary:")
print(df.groupby('Cluster')[['TotalSpent', 'ItemsPurchased']].mean())

# 5. Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='TotalSpent', y='ItemsPurchased', hue='Cluster', palette='Set2', s=80, edgecolor='k')
plt.title("Customer Segments Based on Spending and Item Purchase Behavior")
plt.xlabel("Total Spent (₹)")
plt.ylabel("Number of Items Purchased")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
