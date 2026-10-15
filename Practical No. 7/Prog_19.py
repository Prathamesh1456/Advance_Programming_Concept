#19.	Create a 3D array of shape (2, 3, 4) and write a program to access:
# •	First element 
# •	Last element 
# •	Element at index [0,1,2] 
# •	Element at index [1,2,3]
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D array:") 
print(arr)
print("First element:", arr[0, 0, 0])
print("Last element:", arr[1, 2, 3])
print("Element at index [0,1,2]:", arr[0, 1, 2])
print("Element at index [1,2,3]:", arr[1, 2, 3])