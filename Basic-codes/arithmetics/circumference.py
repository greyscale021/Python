import math

radius = float(input("Enter the radius of circle: "))

circumference = 2 * math.pi * radius

area = math.pi * radius ** 2

print(f"circumference = {round(circumference, 3)}")
print(f"area = {round(area, 3)}")