#20.	Create a (2, 3, 4) array and calculate:
# •	Sum of all elements 
# •	Sum of each layer 
# •	Sum along rows 
# •	Sum along columns
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D array:")
print(arr)
print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
print("Sum along rows:", np.sum(arr, axis=1))
print("Sum along columns:", np.sum(arr, axis=2))