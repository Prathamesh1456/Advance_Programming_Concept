import re

def is_palindrome(text):
    text = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return text == text[::-1]


text = input("Enter word or phrase: ")

print(is_palindrome(text))