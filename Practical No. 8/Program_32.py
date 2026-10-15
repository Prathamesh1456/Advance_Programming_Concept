#32.	Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
def calculate(a, b, operation):
    return operation(a, b)
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        result = calculate(num1, num2, add)
        print(f"Result: {result}")
    elif choice == '2':
        result = calculate(num1, num2, subtract)
        print(f"Result: {result}")
    elif choice == '3':
        result = calculate(num1, num2, multiply)
        print(f"Result: {result}")
    elif choice == '4':
        result = calculate(num1, num2, divide)
        print(f"Result: {result}")
    else:
        print("Invalid choice.")
