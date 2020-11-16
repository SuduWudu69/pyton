import random
import math

participants = input("Please input your list of participants separated by a comma. ")
prizes = input("Please input your list of prizes separated by a comma. ")

list_participants = participants.split(", ")
list_prizes = prizes.split(", ")
times_repeated = len(list_participants)
if times_repeated>10000:
    print("You cannot use more than 10000 participants in this program. Try lowering your amount of " + times_repeated + ".")

for x in range(0, times_repeated):
    