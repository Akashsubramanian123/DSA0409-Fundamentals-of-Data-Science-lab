import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("likes_data.csv")
like_counts = df['likes'].value_counts().sort_index()
print("Frequency Distribution of Likes:\n", like_counts)
like_counts.plot(kind='bar', figsize=(8, 5), title="Likes Frequency")
plt.xlabel("Likes")
plt.ylabel("Posts")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()








