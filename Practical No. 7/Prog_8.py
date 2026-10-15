#8.	Create a 3 × 4 matrix and display its transpose.
import numpy as np
arr=np.arange(1,13).reshape(3,4)
print("Original matrix:")
print(arr)
print("Transpose of the matrix:")
print(arr.T)