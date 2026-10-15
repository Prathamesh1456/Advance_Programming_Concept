import string

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

top_10 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:10]

print("Total number of words:", len(words))
print("\nTop 10 most frequent words:")

for word, count in top_10:
    print(word, ":", count)