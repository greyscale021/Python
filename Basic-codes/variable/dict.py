some = {"value":23, "pokemon": "pikachu", "s":"ram", "er":52}

some["value"] = 35
some["value2"] = 36
some.update({"value4": 1, "value5":2, "value6":3})
del some["value4"]

for i in some:
    print(i)

for i in some.values():
    print(i)

for x,y in some.items():
    print(x,y)

