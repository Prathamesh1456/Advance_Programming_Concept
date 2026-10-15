#  29. Write a recursive function to search for an element in a sorted list using binary search.
def binary_search(sorted_list, target, left, right):
    if left > right:
        return -1 

    mid = (left + right) // 2

    if sorted_list[mid] == target:
        return mid 
    elif sorted_list[mid] < target:
        return binary_search(sorted_list, target, mid + 1, right) 
    else:
        return binary_search(sorted_list, target, left, mid - 1)  
example_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value = int(input("Enter the element to search for: "))
result_index = binary_search(example_list, target_value, 0, len(example_list) - 1)
if result_index != -1:
    print(f"Element {target_value} found at index {result_index}.")
else:
    print(f"Element {target_value} not found in the list.")
