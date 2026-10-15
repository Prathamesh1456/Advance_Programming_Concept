#Duplicate Characters 
#Print all duplicate characters in a string. 
str=input("Enter a string: ")
d=""
printed=""
for i in str:
    if i in d:
        if i not in printed:
            print(i)
            d+=i
            printed+=i
    else:
        d+=i

