#7.	Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.
import numpy as np
matrix1 = np.array([[1, 2, 3],[4, 5, 6]])
matrix2=np.array([[7,8,9],[10,11,13]])
product = np.dot(matrix1, matrix2.T)
print("Matrix Multiplication:")
print(product)