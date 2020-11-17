import random
import math

participants = input("Please input your list of participants separated by a comma: ")
prizes = input("Please input your list of prizes separated by a comma: ")

list_participants = participants.split(", ")
list_prizes = prizes.split(", ")
times_repeated = len(list_participants)
if times_repeated>10000:
    print("You cannot use more than 10000 participants in this program. Try lowering your amount of " + str(times_repeated) + ".")
    times_repeated = 0

print("Your participants are " + str(list_participants))
print("Your prizes are " + str(list_prizes))
for x in range(0, times_repeated):
    random_participant_index = random.randint(0, len(list_participants)-1)
    random_prize_index = random.randint(0, len(list_prizes)-1)
    print(list_participants[random_participant_index] + " got " + list_prizes[random_prize_index])
    list_participants.pop(random_participant_index)