# and- both conditions have to be true for the whole statement to be true.

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


if temp >= 28 and issunny(is_sunny):
    print("Let's cook an egg in the sunlight.")
elif temp <= 0 and issunny:
    print("The sun not sunning")

