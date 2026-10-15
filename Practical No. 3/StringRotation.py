# 30.	String Rotation 
# ●	Check whether one string is a rotation of another. 
# ●	Example:
# ●	ABCD
# ●	CDAB
# Output: Yes

Str1=input("Enter the first string: ")
Str2=input("Enter the second string: ")

if len(Str1) != len(Str2):
    print("No")
else:
    concatenated = Str1 + Str1
    if Str2 in concatenated:
        print("Yes")
    else:
        print("No")