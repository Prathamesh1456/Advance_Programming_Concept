# Longest Word 
# Find the longest word in a given sentence
str=input("Enter a string: ")
words = str.split()
res = ""
for word in words:
    if len(word) > len(res):
        res = word
print(res)
   