# indexing = accessing elements of a sequence using [position], [start: end : step]

credit_number = "1234-5678-9012-3456"

print(f"The first 3 numbers are {credit_number[:3]}")
print(f"The last 3 numbers are {credit_number[-3:]}")
print(f"The next 4 numbers are {credit_number[5:9]}")

credit_number=credit_number.replace("-","")
print(f"Every two numbers are {" ".join(credit_number[::2])}")

print("\n")

print("Let's be anonymous")
print(f"The credit card number is: xxxx-xxxx-xxxx-{credit_number[-4:]}")

print("\n")

print(f"Let's reverse the number: {credit_number[::-1]}")