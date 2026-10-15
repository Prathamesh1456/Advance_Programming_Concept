# Simple Text Analysis Tool

text = input("Enter a paragraph: ")

# Split text into words
words = text.lower().split()

# Count total number of words
total_words = len(words)

# Dictionary to store word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Find top 3 most frequent words
top_3 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]

# Count vowels
vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1

# Display results
print("\nTotal number of words:", total_words)
print("Word frequencies:", frequency)
print("Top 3 most frequent words:", top_3)
print("Number of vowels:", vowel_count)