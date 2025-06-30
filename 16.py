import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re
data = {
    'review': [
        "Great product! Really loved it.",
        "Not satisfied with the quality of the product.",
        "Excellent value for money.",
        "The product is good but delivery was late.",
        "Loved it! Will buy again.",
    ]
}
reviews_df = pd.DataFrame(data)
all_reviews = ' '.join(reviews_df['review'])
clean_text = re.sub(r'[^\w\s]', '', all_reviews.lower())
words = clean_text.split()
word_freq = Counter(words)
freq_df = pd.DataFrame(word_freq.items(), columns=['word', 'frequency']).sort_values(by='frequency', ascending=False)
print("📊 Word Frequency Distribution:\n")
print(freq_df.head(10))
top_n = 10
plt.figure(figsize=(10, 5))
plt.bar(freq_df['word'][:top_n], freq_df['frequency'][:top_n], color='skyblue', edgecolor='black')
plt.title("Top 10 Most Frequent Words in Reviews")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()