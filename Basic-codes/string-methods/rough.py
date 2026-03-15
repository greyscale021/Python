
name = input("Enter your full name: ")

length = len(name)
print(f"The length of the name is {length}")

result = name.find(" ")
print(f"The first occurrence of space is at {result} index")

result = name.rfind(" ")
print(f"The last occurrence of space is at {result} ")

name = name.capitalize()
print(f"Capitalized version of the name: {name}")

name = name.upper()
print(f"Full capitalized version of the name: {name}")

name = name.lower()
print(f"Full lower case version of the name: {name}")

result = name.isalpha()
print(f"Does the whole name consists of only alphabets?: {result}")
