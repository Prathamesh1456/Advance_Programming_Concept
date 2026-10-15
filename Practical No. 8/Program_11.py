#11. Write a function that accepts a string and returns its reverse.
def reverse_string(input_string):
    return input_string[::-1]

str = input("Enter a string: ")
reversed_str = reverse_string(str)
print(f"The reversed string is: {reversed_str}")