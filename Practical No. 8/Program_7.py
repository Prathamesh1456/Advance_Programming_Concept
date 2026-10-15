#7.	Write a function that accepts n and returns the sum of the first n natural numbers.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Input must be a positive integer."
    else:
        return n * (n + 1) // 2
num=int(input("Enter a positive integer to calculate the sum of the first n natural numbers: "))
result = sum_of_natural_numbers(num)
print(f"The sum of the first {num} natural numbers is: {result}")