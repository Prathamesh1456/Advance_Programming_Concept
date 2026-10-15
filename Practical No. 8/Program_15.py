#15. Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(input_list):
    return list(set(input_list))
l=[1, 2, 3, 4, 2, 5, 2]
unique_list = unique_elements(l)
print(f"The unique elements in the list are: {unique_list}")