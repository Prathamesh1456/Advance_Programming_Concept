# 24.	Create a 3D array containing integers from 1 to 27. Flatten the array and calculate:
# •	Sum 
# •	Average 
# •	Maximum 
# •	Minimum
import numpy as np
arr = np.arange(1, 28).reshape(3, 3, 3)
flattened_arr = arr.flatten()   
sum_elements = np.sum(flattened_arr)
average_elements = np.mean(flattened_arr)
max_element = np.max(flattened_arr)
min_element = np.min(flattened_arr)
print("Original 3D array:")
print(arr)
print("Flattened array:")
print(flattened_arr)
print("Sum of elements:", sum_elements)
print("Average of elements:", average_elements)
print("Maximum element:", max_element)
print("Minimum element:", min_element)
