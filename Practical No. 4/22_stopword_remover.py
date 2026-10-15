import re

stopwords = {
    "is", "am", "are", "the", "a", "an",
    "and", "or", "of", "to", "in", "on",
    "for", "with", "this", "that"
}

text = input("Enter paragraph: ")

words = re.findall(r'\b\w+\b', text.lower())

cleaned_words = []

for word in words:
    if word not in stopwords:
        cleaned_words.append(word)

print("Cleaned text:", " ".join(cleaned_words))