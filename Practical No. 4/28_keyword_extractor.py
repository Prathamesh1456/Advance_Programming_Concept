import re

stopwords = {
    "the", "is", "a", "an", "and", "or",
    "of", "to", "in", "on", "for", "with",
    "this", "that", "are", "was", "were"
}

text = input("Enter research paper text: ")

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

frequency = {}

for word in words:
    if word not in stopwords:
        frequency[word] = frequency.get(word, 0) + 1

top_5 = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

print("Top 5 keywords:")

for word, count in top_5:
    print(word, ":", count)