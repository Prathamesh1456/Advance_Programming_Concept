# Uppercase and Lowercase Count 
# Count the number of uppercase and lowercase letters in a string. 
str=input("Enter a string: ")
upper_count=0
lower_count=0
for i in str:
    if i.isupper():
        upper_count+=1
    else:
        lower_count+=1
print("Number of upper case characters: ",upper_count)
print("Number of lower case characters: ",lower_count)