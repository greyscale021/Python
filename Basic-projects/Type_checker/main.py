# Check if <value> is <type>
# Bool

def type_check(x,y) -> bool:
    data = {
        "int": lambda x:int(x),
        "float": lambda x:float(x),
        "bool": lambda x: x in ("True","False"),
        "str": lambda x: True
    }

    if y not in data:
        return False
    
    if y == "bool":
        if data[y](x) == False:
            return False
        return True
    

    if y == "str":
        try: 
            int(x)
            return False
        except ValueError:
            pass
        try:
            float(x)
            return False
        except ValueError:
            pass
        if x in ("True","False"):
            return False
        return
    
    try:
        data[y](x)
        return True
    except ValueError:
        return False


a = input("Enter a value: ")
b = input("Enter a type(int/float/bool/str): ")
print(type_check(a,b))