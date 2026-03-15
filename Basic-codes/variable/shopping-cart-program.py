
item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))
total = price*quantity

print(f"You have bought {item} x {quantity}")
print(f"The total is: ${total}")