# 26.	Caesar Cipher 
# ●	Encrypt and decrypt a message using the Caesar Cipher algorithm. 
Str=input("Enter a string: ")
shift=int(input("Enter the shift value: "))
cipher=""
for i in Str:
    if i.isalpha():
        shift_base = ord('A') if i.isupper() else ord('a')
        cipher += chr((ord(i) - shift_base + shift) % 26 + shift_base)
    else:
        cipher += i
print("Encrypted message:", cipher)