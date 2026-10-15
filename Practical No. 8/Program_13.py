#13. Write a function that accepts a list of numbers and returns their average.
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
l=[3, 5, 1, 8, 2]
average= calculate_average(l)
print(f"The average of the list is: {average}")