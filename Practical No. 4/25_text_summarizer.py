import re

text = input("Enter paragraph: ")

sentences = re.split(r'(?<=[.!?])\s+', text)

words = re.findall(r'\b\w+\b', text.lower())

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

scores = []

for sentence in sentences:
    sentence_words = re.findall(r'\b\w+\b', sentence.lower())
    score = sum(frequency.get(word, 0) for word in sentence_words)
    scores.append((score, sentence))

scores.sort(reverse=True)

summary = scores[:2]

print("\nSummary:")

for score, sentence in summary:
    print(sentence)