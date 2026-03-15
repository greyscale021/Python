# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.1415936546
price2 = -987.65
price3 = 12.34/75

print(f"Price 1 is {price1:^10.2f}")
print(f"Price 2 is {price2:012,}")
print(f"Price 3 is {price3:.2%}")
