# 1. Basic
if age >= 18:
    status = "adult"
else:
    status = "minor"

status = "adult" if age >= 18 else "minor"


# 2. Even or odd
if num % 2 == 0:
    result = "even"
else:
    result = "odd"

result = "even" if num % 2 == 0 else "odd"


# 3. Instance state
if instance["state"] == "running":
    label = "active"
else:
    label = "inactive"

label = "active" if instance["state" == "running"] else "inactive"


# 4. Absolute value (manually)
if num < 0:
    value = -num
else:
    value = num

value = -num if num<0 else num


# 5. Default fallback
if username:
    display = username
else:
    display = "Anonymous"

display = username if username else "Anonymous"


# 6. Pass or fail
if score >= 50:
    grade = "pass"
else:
    grade = "fail"

grade = "pass" if score >= 50 else "fail"

# 7. Max of two numbers
if a > b:
    bigger = a
else:
    bigger = b

bigger = a if a>b else b

The pattern is always the same:

<value_if_true> if <condition> else <value_if_false>