# ternary - oneline shortcut of if-else

user_role = input("What is your role?: ")

access_level = "System access level full." if user_role == "Admin" else "Limited system access"
print(access_level)