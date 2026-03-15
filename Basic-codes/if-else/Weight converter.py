# Python weight converter

print("Python weight converter-")
weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds? (K or L): ")

if unit == 'K':
    weight = weight*2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")

elif unit == 'L':
    weight = weight/2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")

else:
    print("Enter valid inputs.")

