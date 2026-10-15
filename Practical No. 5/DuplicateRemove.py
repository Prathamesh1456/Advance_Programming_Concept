# ⦁	Remove Duplicate Characters 
# ⦁	Remove duplicate characters while maintaining the original order. 
str=input("Enter a string: ")
d=""
for i in str:
    if i not in d:
        d+=i
print(d)

