#16.	Create a function to find the second-largest number in a list.
def second_largest(numbers):
    if len(numbers)<2:
        return None
    max_num = second_max = numbers[0]
    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif max_num > num > second_max:
            second_max = num
    return second_max
l=[3, 5, 1, 8, 2]
second_largest_number = second_largest(l)
if second_largest_number is not None:
    print(f"The second largest number in the list is: {second_largest_number}")
else:
    print("The list does not have enough unique elements to determine the second largest number.")