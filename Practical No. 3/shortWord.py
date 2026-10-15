str=input("Enter a string: ")
words = str.split()
res = words[0]
for word in words:
    if len(word) < len(res):
        res = word
print(res)
   