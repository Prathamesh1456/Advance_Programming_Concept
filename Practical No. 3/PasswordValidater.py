# ⦁	Validate a password based on these conditions: 
# ⦁	Minimum 8 characters 
# ⦁	At least one uppercase letter 
# ⦁	One lowercase letter 
# ⦁	One digit 
# ⦁	One special character
str=input("Enter a password: ")
if str<8:
    print("Invalid password")
else:
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in str:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isspace():  
            has_special = True