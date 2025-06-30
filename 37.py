import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# 1. Simulate data
np.random.seed(42)
study_hours = np.random.normal(5, 2, 50).clip(1, 10)  # 1–10 hours
scores = study_hours * 10 + np.random.normal(0, 5, 50)  # score ~ linear + noise

df = pd.DataFrame({'Study Hours': study_hours, 'Exam Score': scores})

# 2. Correlation analysis
corr, p_value = pearsonr(df['Study Hours'], df['Exam Score'])

print(f"\n📈 Correlation Coefficient (r): {corr:.2f}")
print(f"P-value: {p_value:.4f}")
if p_value < 0.05:
    print("✅ Significant positive correlation between study time and scores.")
else:
    print("⚠️ No significant correlation found.")

# 3. Basic scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Study Hours'], df['Exam Score'], alpha=0.7, color='blue', edgecolor='k')
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Score")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 4. Regression line with Seaborn
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='Study Hours', y='Exam Score', line_kws={'color': 'red'})
plt.title("Regression Plot: Study Time vs Score")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 5. Heatmap of correlation matrix
plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
