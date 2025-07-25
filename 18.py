import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
data = {
    'Age': [23, 25, 28, 30, 33, 35, 36, 38, 40, 42, 45, 47, 50, 52, 55, 58, 60, 62],
    '%Fat': [14, 15, 16, 17, 19, 20, 21, 21, 22, 24, 25, 25, 27, 28, 30, 31, 32, 34]
}
df = pd.DataFrame(data)
mean_age = df['Age'].mean()
mean_fat = df['%Fat'].mean()
median_age = df['Age'].median()
median_fat = df['%Fat'].median()
std_age = df['Age'].std()
std_fat = df['%Fat'].std()
print("📊 Summary Statistics:")
print(f"Mean Age: {mean_age:.2f}, Mean %Fat: {mean_fat:.2f}")
print(f"Median Age: {median_age}, Median %Fat: {median_fat}")
print(f"Std Dev Age: {std_age:.2f}, Std Dev %Fat: {std_fat:.2f}")
correlation = df['Age'].corr(df['%Fat'])
print(f"\n🔗 Pearson Correlation between Age and %Fat: {correlation:.3f}")
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.boxplot(data=df['Age'], color='skyblue')
plt.title("Boxplot of Age")
plt.subplot(1, 2, 2)
sns.boxplot(data=df['%Fat'], color='salmon')
plt.title("Boxplot of %Fat")
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 5))
sns.scatterplot(x='Age', y='%Fat', data=df, color='green', s=80)
plt.title("Scatter Plot: Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("% Body Fat")
plt.text(40, max(df['%Fat']) - 1, f"Corr = {correlation:.2f}", fontsize=12, color='black')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 5))
stats.probplot(df['%Fat'], dist="norm", plot=plt)
plt.title("Q-Q Plot of %Fat")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()