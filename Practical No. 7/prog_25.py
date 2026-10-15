# 25.	Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are:
# •	Greater than 50 
# •	Even numbers 
# •	Less than the average value
# •	

import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
flattened_arr = arr.flatten()
average_value = np.mean(flattened_arr)
filtered_elements = flattened_arr[(flattened_arr > 50) & (flattened_arr % 2 == 0) & (flattened_arr < average_value)]
print("Original 3D array:")
print(arr)
print("Flattened array:")
print(flattened_arr)
print("Average value:", average_value)
print("Filtered elements:", filtered_elements)