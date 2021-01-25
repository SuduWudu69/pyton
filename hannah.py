import random, time
name_list = ['hamster', 'cat', 'tiger']
name_chosen = name_list[random.randint(0, len(name_list)-1)]
name_hints = []
if name_chosen == 'hamster':
    name_hints = ["I am tiny", ""]
if name_chosen == 'cat':
    name_hints = []
if name_chosen == 'tiger':
    name_hints = []
print("Hello and welcome to Hannah's game of fun.")
time.sleep(.75)
input("press enter to continue")
player_name = input("To start the game off, I'm gonna need your name: ")
print("Ok " + player_name + ", it's time to play,\n HANNAH'S GAME OF FUN!")
