#14.	Create an array containing duplicate values. Find and display only the unique elements.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 5])
unique = np.unique(arr)
print("Unique elements:", unique)