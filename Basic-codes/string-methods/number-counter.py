import time
number = (input("Enter number: "))

counter = number.count(input("What do you want to find?"))
print(f"Total: {counter}")

time.sleep(2)

x= input("What do you want to replace?: ")
y= input("With what?: ")

print(number.replace(x, y))
