import re

contractions = {
    "don't": "do not",
    "can't": "cannot",
    "isn't": "is not",
    "aren't": "are not",
    "won't": "will not",
    "I'm": "I am",
    "you're": "you are",
    "it's": "it is",
    "didn't": "did not"
}

text = input("Enter text: ")

for contraction, expansion in contractions.items():
    text = re.sub(
        re.escape(contraction),
        expansion,
        text,
        flags=re.IGNORECASE
    )

text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

print("Normalized text:", text)