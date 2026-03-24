def frog(fly):
    print(f"Forg ate {fly}")

def froggy(*fly):
    for flyy in fly:
        print(f"Froggy ate {flyy}")

def foggitier(**flies_with_name):
    for x,y in flies_with_name.items():
        print(f"Foggitier ate {x} named {y}")

frog("fly1")

froggy("fly1","fly2","fly3")

foggitier(fly1="michal", fly2="al", fly3="p")

