#14. Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_occurrences(input_list, element):
    return input_list.count(element)
list=[1, 2, 3, 4, 2, 5, 2]
element=2
occurrences = count_occurrences(list, element)
print(f"The element {element} occurs {occurrences} times in the list.")