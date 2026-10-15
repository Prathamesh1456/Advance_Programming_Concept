import re

dictionary = {
    "python", "java", "programming", "computer",
    "science", "student", "college", "learning",
    "software", "development", "database", "coding"
}

text = input("Enter text: ")

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

misspelled = []

for word in words:
    if word not in dictionary and word not in misspelled:
        misspelled.append(word)

print("Misspelled words:", misspelled)