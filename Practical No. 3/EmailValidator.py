# 27.	Email Validator 
# ●	Validate whether a given email address follows a valid format. 
Str=input("Enter an email address: ")
import re
a= re.match(r"[^@]+@[^@]+\.[^@]+", Str)
if a:
    print("Valid email address")
else:
    print("Invalid email address")