#Write a Python Program to find a Largest of Three Numbers
num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))
num3=int(input("Enter a third number: "))
if(num1>num2):
    if(num1>num3):
        print(num1," is Largest")
    else:
        print(num3," is Largest")
else:
    if(num2>num3):
        print(num2," is Largest")
    else:
        print(num3," is Largest")