#2.	Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number to check if it is even or odd: "))
result = check_even_odd(num)