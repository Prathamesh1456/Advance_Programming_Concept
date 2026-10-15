# 28.	Word Frequency Dictionary 
# ●	Count the frequency of every word in a paragraph. 
paragraph = input("Enter a paragraph: ")
frequency = {}
words = paragraph.split()
for word in words:
    word = word.lower()
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequencies:", frequency)