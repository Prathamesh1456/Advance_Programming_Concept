# 24.	Most Frequent Character 
# ●	Find the character with the highest frequency. 
str=input("Enter a string: ")
d=""
for i in str:
    if i not in d:
        d+=i

max_char = d[0]
max_count = str.count(d[0])
for char in d:
    if str.count(char) > max_count:
        max_count = str.count(char)
        max_char = char

print(f"The most frequent character is '{max_char}' with a frequency of {max_count}.")