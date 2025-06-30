import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simulate transaction data
np.random.seed(42)
n_customers = 200
data = {
    'customer_id': range(1, n_customers + 1),
    'total_spent': np.random.normal(5000, 1500, n_customers).clip(1000, None),
    'visit_frequency': np.random.poisson(6, n_customers)
}

df = pd.DataFrame(data)

# 2. Features for clustering
X = df[['total_spent', 'visit_frequency']]

# 3. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Apply K-Means clustering
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
df['segment'] = kmeans.fit_predict(X_scaled)

# 5. Segment summary
print("\n🧩 Segment Summary:")
print(df.groupby('segment')[['total_spent', 'visit_frequency']].mean())

# 6. Visualize segments
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='total_spent', y='visit_frequency', hue='segment', palette='Set2', s=100, edgecolor='k')
plt.title("Customer Segments Based on Spending and Frequency")
plt.xlabel("Total Amount Spent (₹)")
plt.ylabel("Visit Frequency")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
