#  Palindrome Check 
# Check whether the entered string is a palindrome. 
str=input("Enter a string: ")
demo=str[::-1]
if str==demo:
    print("String is Palindrome")
else:
    print("String is not palindrome")