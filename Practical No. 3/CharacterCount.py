str=input("Enter a string: ")
vowel_count=0
consonants_count=0
digits_count=0
space_count=0
special_count=0
for i in str:
    if i in "AEIOUaeiou":
        vowel_count+=1
    elif i.isalpha():
        consonants_count+=1
    elif i.isdigit():
        digits_count+=1
    elif i.isspace():
        space_count+=1
    else:
        special_count+=1

print("Number of vowels: ",vowel_count)
print("Number of consonants: ",consonants_count)
print("Number of spaces: ",space_count)
print("Number of Digits: ",digits_count)
print("Number of Special Characters: ",special_count)