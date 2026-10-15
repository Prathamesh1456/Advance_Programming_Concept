#Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.
import numpy as np
marks = np.array([85, 92, 78, 96, 88, 91, 84, 89, 93, 87, 90, 86, 94, 83, 95, 82, 97, 81, 98, 80])
class_average = np.mean(marks)
print("Class average:", class_average)
print("Marks of students who scored above the average:")
print(marks[marks > class_average])