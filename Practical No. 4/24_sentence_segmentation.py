import re

text = input("Enter text: ")

text = re.sub(r'\b(Dr|Mr|Mrs|Ms|Prof|Sr|Jr)\.', r'\1<ABBR>', text)

sentences = re.split(r'(?<=[.!?])\s+', text)

sentences = [
    sentence.replace("<ABBR>", ".").strip()
    for sentence in sentences
]

print("\nSentences:")

for sentence in sentences:
    print(sentence)