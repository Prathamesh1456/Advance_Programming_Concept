# ⦁	Character Frequency 
# ⦁	Display the frequency of every character in a string. 

str=input("Enter a string: ")
d=""
printed=""
for i in str:
    if i not in d:
        print("The frequency of ",i," is ",str.count(i))
        d+=i
        printed+=i
