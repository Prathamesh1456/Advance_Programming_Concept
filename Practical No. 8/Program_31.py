#31.	Check whether a string is a palindrome using recursion.
def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])  
string_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string_input):
    print(f'"{string_input}" is a palindrome.')
else:
    print(f'"{string_input}" is not a palindrome.')