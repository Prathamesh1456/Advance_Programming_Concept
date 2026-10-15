# 15.	Create two NumPy arrays and concatenate them horizontally and vertically. 
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
horizontally_concatenated = np.hstack((arr1, arr2))
print("Horizontally concatenated array:")
print(horizontally_concatenated)

vertically_concatenated = np.vstack((arr1, arr2))
print("Vertically concatenated array:")
print(vertically_concatenated)