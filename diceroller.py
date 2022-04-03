import random
dice_name = input("What sided die are you rolling? ")
dice_numbo = int(dice_name)
number_of_rolls = input("How many times are you rolling it? ")
numbo = int(number_of_rolls)
num_sum = []
min_roll_val = 1
if numbo>1000:
    print("Your number of " + str(numbo) + " is too many times for the dice roller.")
    numbo = 0

for x in range(0, numbo):
    max_roll_val = dice_numbo
    result = random.randint(min_roll_val, max_roll_val)
    print(str(result))
    num_sum.append(result)
final_result = str(sum(num_sum))
print("Sum: " + final_result)