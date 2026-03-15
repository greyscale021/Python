import math

x = int(input("Enter side A: "))
y = int(input("Enter side B: "))

hypotenuse = math.sqrt(pow(x,2) + pow(y,2))
print(f"hypotenuse = {hypotenuse}")