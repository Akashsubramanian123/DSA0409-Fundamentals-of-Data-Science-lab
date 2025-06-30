import pandas as pd
import scipy.stats as stats
try:
    df = pd.read_csv('customer_reviews.csv')
except FileNotFoundError:
    print("❌ File not found. Please ensure 'customer_reviews.csv' exists.")
    exit()
if 'category' not in df.columns or 'rating' not in df.columns:
    print("❌ Missing required columns ('category', 'rating') in the dataset.")
    exit()
category = input("Enter the product category to analyze (Electronics, Clothing, Home): ")
filtered = df[df['category'].str.lower() == category.lower()]
if filtered.empty:
    print(f"❌ No ratings found for category '{category}'.")
    exit()
ratings = filtered['rating'].dropna()
mean_rating = ratings.mean()
std_err = stats.sem(ratings)
n = len(ratings)
confidence = 0.95
margin = stats.t.ppf((1 + confidence) / 2., n - 1) * std_err
ci_lower = mean_rating - margin
ci_upper = mean_rating + margin
print(f"\n📊 Rating Analysis for Category: {category}")
print(f"Number of Reviews: {n}")
print(f"Average Rating: {mean_rating:.2f}")
print(f"95% Confidence Interval: ({ci_lower:.2f}, {ci_upper:.2f})")
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 5))
sns.histplot(ratings, bins=5, kde=True, color='skyblue', edgecolor='black')
plt.title(f"Ratings Distribution for '{category}'")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.xticks([1, 2, 3, 4, 5])
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()