# 1 D Array
import numpy as np
nums=np.array([1,2,3,4,5])
# print(nums)

# 2 D Array
nums2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(nums2)

# 3 D Array
nums3=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
# print(nums3)

#Apply the addition operation on the 3D array  
result = nums3 + 10
# print(result)

#Apply the subtraction operation on the 3D array
result = nums3 - 10
# print(result)

#Apply the multiplication operation on the 3D array
result = nums3 * 10
# print(result)

#Apply the transpose operation on the 3D array
result = np.transpose(nums3)
# print(result)

#adding two 2D arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
result=arr1+arr2
# print(result)
#Subtracting two 2D arrays
result=arr1-arr2
# print(result)

#Multiplying two 2D arrays
result=arr1*arr2
# print(result)

#Apply Exponential operation on the 2D array
result = np.exp(arr1)
print(result)


