#12.	Create a function that checks whether a given string or number is a palindrome.
def is_palindrome(input_value):
    input_str = str(input_value)   
    return input_str == input_str[::-1]
str_or_num = input("Enter a string or number: ")
if is_palindrome(str_or_num):
    print(f"{str_or_num} is a palindrome.")
else:
    print(f"{str_or_num} is not a palindrome.")