# 17.	Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
num = int(input("Enter a number: "))
fib_numbers = fibonacci(num)
print(f"The first {num} Fibonacci numbers are: {fib_numbers}")