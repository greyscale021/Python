# not- inverts the condition

temp = int(input("Enter the temperature: "))

is_sunny = input("Is it sunny? (y/n): ")

def issunny(is_sunny):

    if is_sunny == 'y':
        return True
    elif is_sunny == 'n':
        return False
    else:
        while (is_sunny != 'y' or is_sunny != 'n'):
            print("Please enter y or n for yes and no.")
            is_sunny = input("Is it raining? (y/n): ")
            return issunny(is_sunny)

if temp >= 28 and not issunny(is_sunny):
    print("The clouds aren't working properly")
elif temp <= 0 and issunny:
    print("The sun not working properly")
