# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    print(round(num1/num2,3))
else:
    print("Please enter valid numbers.")
