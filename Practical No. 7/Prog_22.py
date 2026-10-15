# 22.	Generate a random 3D array of shape (3, 4, 5) and calculate its:
# mean, median, standard deviation, variance, minimum, and maximum.
import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
var = np.var(arr)
min_val = np.min(arr)
max_val = np.max(arr)
