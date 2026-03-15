
food = input("Enter a food you like (q to quit): ")

while not food == "q" and not food == "exit":
    print(f"You like {food}")
    food = input("Enter another food you like ( q to quit): ")

print("bye")