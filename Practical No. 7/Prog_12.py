#Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
arr[arr > 50] = 0
print("Modified array:", arr)