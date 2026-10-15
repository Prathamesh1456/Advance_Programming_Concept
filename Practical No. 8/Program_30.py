#30.	Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
n = int(input("Enter a decimal number: "))
if n == 0:
    print("Binary representation: 0")
else:
    binary_representation = decimal_to_binary(n)
    print(f"Binary representation: {binary_representation}")
