# 25.	Second Most Frequent Character 
# ●	Find the second most frequently occurring character. 
str=input("Enter a string: ")
d=""
for i in str:
    if i not in d:
        d+=i

max_char = d[0]
max_count = str.count(d[0])
second_max_char = None
second_max_count = 0

for char in d:
    count = str.count(char)
    if count > max_count:
        second_max_char = max_char
        second_max_count = max_count
        max_char = char
        max_count = count
    elif count > second_max_count and char != max_char:
        second_max_char = char
        second_max_count = count

if second_max_char is None:
    print("There is no second most frequent character.")
else:
    print(f"The second most frequent character is '{second_max_char}' with a frequency of {second_max_count}.")