# python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount($): "))
    if principle < 0:
        print("Principle can't be less than zero dollars\n")
    else:
        break
while True:
    rate = float(input("Enter the rate amount(%): "))
    if rate < 0:
        print("Rate can't be less than zero\n")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if principle < 0:
        print("Time can't be less than zero\n")
    else:
        break


total = principle * pow((1 + rate / 100),time)


if time == 1:
    x = 'year'
else:
    x = 'years'
print(f"Balance would be :{total:.2f}$ ,after {time} {x}")
