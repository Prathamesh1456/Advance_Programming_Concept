# ⦁	Anagram Check 
# ⦁	Check whether two strings are anagrams. 

str1=input("Enter a first string: ")
str2=input("Enter second string: ")
if(len(str1)!=len(str2)):
    print("The strings are not anagram")
else:
    if(sorted(str1)==sorted(str2)):
        print("STring is Anagram")
    else:
        print("String is not anagram")