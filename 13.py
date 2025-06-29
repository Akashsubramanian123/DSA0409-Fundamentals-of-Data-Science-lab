from collections import Counter
import string
with open("sample_text.txt", "r") as f:
    words = f.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
for word, freq in Counter(words).most_common():
    print(f"{word}: {freq}")
