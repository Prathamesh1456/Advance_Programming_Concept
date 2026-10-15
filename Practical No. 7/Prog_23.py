# 23.	Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24. Flatten the array into a one-dimensional array and display both the original and flattened arrays.
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
flattened_arr = arr.flatten()
print("Original 3D array:")
print(arr)
print("Flattened array:")
print(flattened_arr)
