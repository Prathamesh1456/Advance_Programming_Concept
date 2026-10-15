# Character Frequency Counter

text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Sort by frequency in descending order
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nCharacter frequencies:")

for char, count in sorted_frequency:
    if char == " ":
        print("'space':", count)
    else:
        print(repr(char) + ":", count)