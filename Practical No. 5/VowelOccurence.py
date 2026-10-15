# ⦁	Count Occurrences of a Word 
# ⦁	Count how many times a specific word appears in a sentence. 
str=input("Enter a string: ")
d=""
for i in str:
    if i in "AEIOUaeiou":
        if i not in d:
            print("Occurence of ",i," is ",str.count(i))
            d+=i