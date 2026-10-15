import re

def check_password(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[!@#$%^&*()_-]', password)):
        return True
    return False

password = input("Enter password: ")

if check_password(password):
    print("Strong Password")
else:
    print("Weak Password")