# Validate user input
#     1. usernaem is no more than 12 characters
#     2. username must not contain spaces
#     3. username must not contain digits

username = input("Enter username: ")

def validate(username):
    if len(username) > 12:
        print("Username can't be more than 12 characters")
        username = input("Enter username(charecter limit 12): ")
        return validate(username)
    elif not username.find(" ") == -1:
        print("Username can't have spaces")
        username = input("Enter username: ")
        return validate(username)
    elif not username.isalpha():
        print("Username must consists of only alphabets.")
        username = input("Enter username: ")
        return validate(username)
    else:
        print(f"Welcome {username}!")

validate(username)