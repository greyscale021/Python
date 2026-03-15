# or- at least one condition has to be true, for the whole statement to be true

temp = int(input("Enter the temperature: "))

is_raining = input("Is it raining? (y/n): ")

def israining(is_raining):
    if is_raining == 'y':
        return True
    elif is_raining == 'n':
        return False
    else:
        while (is_raining != 'y' or is_raining != 'n'):
            print("Please enter y or n for yes and no.")
            is_raining = input("Is it raining? (y/n): ")
            return israining(is_raining)

if temp > 35 or temp < 0 or israining(is_raining):
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
