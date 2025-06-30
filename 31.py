import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simulated customer dataset
np.random.seed(42)
df = pd.DataFrame({
    'customer_id': range(1, 201),
    'age': np.random.randint(18, 60, 200),
    'avg_cart_value': np.random.normal(3000, 800, 200),
    'purchase_freq': np.random.randint(1, 20, 200),
    'visit_freq': np.random.randint(1, 15, 200)
})

# 2. Features for clustering
features = ['age', 'avg_cart_value', 'purchase_freq', 'visit_freq']
X = df[features]

# 3. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Apply K-Means clustering
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
df['segment'] = kmeans.fit_predict(X_scaled)

# 5. Print segment counts
print("\n🧩 Customer Segment Counts:")
print(df['segment'].value_counts().sort_index())

# 6. Visualize clusters in 2D (PCA could be used for dimensionality reduction if needed)
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='avg_cart_value', y='purchase_freq', hue='segment', palette='Set2', s=100)
plt.title("Customer Segments Based on Purchase Behavior")
plt.xlabel("Avg Cart Value (₹)")
plt.ylabel("Purchase Frequency")
plt.legend(title="Segment")
plt.tight_layout()
plt.show()
