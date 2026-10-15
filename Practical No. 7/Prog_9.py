#9.	Create a 4 × 4 NumPy array and write a program to:
# •	Display the first row 
# •	Display the last column 
# •	Display the diagonal elements 
# •	Display the elements from the second and third rows
import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
print("Original matrix:")
print(arr)
print("First row:")
print(arr[0])
print("Last column:")
print(arr[-1])
print("Diagonal elements:")
print(np.diag(arr))
print("Elements from the second and third rows:")
print(arr[1:3])