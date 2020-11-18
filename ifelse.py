import random
can_run = True
print("Hello and welcome to the Sudu Industries online job interview. I'm going to ask you a few basic questions so that we can see if you're fit for the company.")
name = input("What is your first name? ")
if len(name)>10 and can_run:
    name_meaning = input("That's quite a long name you have " + name +". It sounds interesting, tell me about what it means. ")
    if name_meaning == "":
        print("You don't have to talk about it if you don't want to. Let's move on to the next question.")
    else:
        print("Wow, that's pretty interesting. I'd love to know more about you, but we don't have time for that today. Let's move on to the next question.")
else:
    print("I like that name, it fits you well.")

gender = input("So, " + name + " what gender are you? You do not have to answer this question if it causes you discomfort, just leave this answer blank. ")

if gender.startswith("m") or gender.startswith("M") and can_run:
    print("Well, we could always use another guy in the workplace.")

if gender.startswith("f") or gender.startswith("F") and can_run:
    print("Well, we could always use another woman in the workplace.")

if gender == "" and can_run:
    print("Well, I hope that you'll feel welcome at Sudu Industries.")

qualities = input("Now, what qualities do you have that will make you suited for a job at Sudu Industries? Make sure to separate your qualities with a comma. ")
list_of_qualities = qualities.split(", ")

if qualities == "" and can_run:
    print("Well it seems that you are not fit for a job at Sudu industries but if you improve your skills we may be open to a second interview.")
    can_run = False
else:
    if can_run:
        rando_index = random.randint(0, len(list_of_qualities)-1)
        print("Well " + name + ". It seems like your qualities will make you a great addition to the company. I'm particularly interested in you being " + list_of_qualities[rando_index])