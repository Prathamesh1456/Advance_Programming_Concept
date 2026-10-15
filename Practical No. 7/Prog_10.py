#10.	Create a 4 × 4 matrix and calculate the sum of each row and each column separately.
import numpy as np
matrix = np.arange(1, 17).reshape(4, 4)
print("Original matrix:")
print(matrix)
print("Sum of each row:")
print(np.sum(matrix, axis=1))
print("Sum of each column:")
print(np.sum(matrix, axis=0))