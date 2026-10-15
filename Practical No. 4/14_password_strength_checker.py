# Password Strength Checker using Regular Expression

import re


def check_password(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*()_-]', password)):
        return True
    else:
        return False


password = input("Enter password: ")

if check_password(password):
    print("Strong password.")
else:
    print("Weak password.")