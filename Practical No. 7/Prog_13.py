#13.	Create an unsorted NumPy array and display it in:
# •	Ascending order 
# •	Descending order
import numpy as np
arr = np.array([5, 2, 9, 1, 7, 3, 8, 4, 6])
# Ascending order
print("Ascending order:", np.sort(arr))
# Descending order
print("Descending order:", np.sort(arr)[::-1])