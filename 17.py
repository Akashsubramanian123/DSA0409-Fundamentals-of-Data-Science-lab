import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("❌ File not found. Please make sure 'data.csv' exists.")
    exit()
if 'feedback' not in df.columns:
    print("❌ 'feedback' column not found in the dataset.")
    exit()
def preprocess_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words
all_words = []
for comment in df['feedback']:
    all_words.extend(preprocess_text(comment))
word_freq = Counter(all_words)
try:
    N = int(input("Enter the number of top frequent words to display (N): "))
except ValueError:
    print("❌ Please enter a valid integer.")
    exit()
top_words = word_freq.most_common(N)
top_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
print("\n📊 Top", N, "Most Frequent Words:\n")
print(top_df)
colors = ['red' if i == 0 else 'skyblue' for i in range(len(top_df))]
plt.figure(figsize=(10, 5))
plt.bar(top_df['Word'], top_df['Frequency'], color=colors, edgecolor='black')
plt.title(f"Top {N} Most Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()