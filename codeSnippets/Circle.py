import math

radius = float(input("enter the radius of the circle:"))
circumference  = 2 * math.pi * radius
area = math.pi * radius * radius

print(f"The circumference of the circle is {circumference}")
print(f"The area of the circle is {area}")

# if you want to round of to a certain decimal places use the round function

# circumference = round(circumference, 2)
# area = round(area, 2)

print(f"The circumference of the circle is {round(circumference, 2)}")
print(f"The area of the circle is {round(area ,2)}")