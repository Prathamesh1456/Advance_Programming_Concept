#3.	Define a function that accepts two numbers and returns the greater number.
def greater_number(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal."
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = greater_number(num1, num2)
print(f"The greater number is: {result}")