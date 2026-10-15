# 2.	Write a program to develope a system that manages the positions of points in a 2D plane. The position of each point is represented as a tuple of two values: (x, y). Write a program that:
# ●	Takes a list of points as input.
# ●	Calculates the distance between two given points.
# ●	Finds the point that is farthest from the origin (0, 0).
# Tasks:
# ●	Use tuples to represent the coordinates of each point.
# ●	Implement a function to calculate the Euclidean distance between two points using their tuple representations.
# ●	Implement a function to find the farthest point from the origin.
# ●	 

import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.hypot(x2 - x1, y2 - y1)

def find_farthest_point(points):
    farthest_point = None
    max_distance = 0
    for point in points:
        distance = calculate_distance(point, (0, 0))
        if distance > max_distance:
            max_distance = distance
            farthest_point = point
    return farthest_point

x1=float(input("Enter x-coordinate of first point: "))
y1=float(input("Enter y-coordinate of first point: "))
x2=float(input("Enter x-coordinate of second point: "))
y2=float(input("Enter y-coordinate of second point: "))

point1 = (x1, y1)
point2 = (x2, y2)

distance = calculate_distance(point1, point2)
print(f"Distance between the points: {distance}")

points = [point1, point2]
farthest_point = find_farthest_point(points)
print(f"Farthest point from the origin: {farthest_point}")

