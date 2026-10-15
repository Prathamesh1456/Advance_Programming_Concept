#1.	Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("array:",arr)
print("size:",arr.size)
print("data type:",arr.dtype)
print("number of dimensions:",arr.ndim)