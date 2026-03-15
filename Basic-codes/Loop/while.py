# execute some code while some condition remains true

name = input("Enter your name: ")
age_str = input("Enter your age: ")


while name=='':
    print("You did not enter your name")
    name = input("Re-enter your name: ")

while age_str =='' or age_str.isalpha() or int(age_str)<=0:
    print("Please enter a proper age.")
    age_str = input("Re-enter your age:")

print(f"Hello {name}")
print(f"Your age is {age_str}")