#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
l=[3, 5, 1, 8, 2]
largest_number = find_largest(l)
print(f"The largest number in the list is: {largest_number}")