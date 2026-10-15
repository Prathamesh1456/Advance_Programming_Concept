#16.	Store marks of 10 students in a NumPy array. Calculate:
# •	Highest marks 
# •	Lowest marks 
# •	Average marks 
# •	Median 
# •	Standard deviation
import numpy as np
marks = np.array([85, 92, 78, 96, 88, 91, 84, 89, 93, 87])
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))