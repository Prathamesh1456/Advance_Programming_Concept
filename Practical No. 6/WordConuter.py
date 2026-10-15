import re

filename = "sample.txt"

with open("sample.txt", "r") as file:
    text = file.read()

# Remove punctuation and convert to lowercase
text = re.sub(r'[^\w\s]', '', text.lower())

# Split into words
words = text.split()

# Count words
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Total words:", len(words))

# Display 10 most frequent words
top_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 most frequent words:")
for word, count in top_words[:10]:
    print(word, ":", count)