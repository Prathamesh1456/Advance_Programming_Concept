#6.	Define a function to calculate the area of a circle using its radius.
def area_of_circle(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        area = 3.14159 * radius ** 2
        return area
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")