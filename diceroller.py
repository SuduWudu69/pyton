import random
dice_name = input("What die are you rolling? ")
number_of_rolls = input("How many times are you rolling it? ")
numbo = int(number_of_rolls)
min_roll_val = 1
if numbo>1000:
    print("Your number of " + str(numbo) + " is too many times for the dice roller.")
    numbo = 0

for x in range(0, numbo):
    if dice_name == "d4":
        max_roll_val = 4
        print(str(random.randint(min_roll_val, max_roll_val)))
    if dice_name == "d6":
        max_roll_val = 6
        print(str(random.randint(min_roll_val, max_roll_val)))
    if dice_name == "d8":
        max_roll_val = 8
        print(str(random.randint(min_roll_val, max_roll_val)))
    if dice_name == "d10":
        max_roll_val = 10
        print(str(random.randint(min_roll_val, max_roll_val)))
    if dice_name == "d12":
        max_roll_val = 12
        print(str(random.randint(min_roll_val, max_roll_val)))
    if dice_name == "d20":
        max_roll_val = 20
        print(str(random.randint(min_roll_val, max_roll_val)))
    if dice_name == "d100":
        max_roll_val = 100
        print(str(random.randint(min_roll_val, max_roll_val)))