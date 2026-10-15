# #18.	Write a Python program using NumPy to create a 3D array of shape (2, 3, 4) containing numbers from 1 to 24. Display the array and its:
# •	Number of dimensions 
# •	Shape 
# •	Size
import numpy as np
arr=np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D array:")
print(arr)
print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)