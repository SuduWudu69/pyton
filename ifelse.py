print("Hello and welcome to the Sudu Industries online job interview. I'm going to ask you a few basic questions")
name = input("What is your first name? ")
if len(name)>10:
    print("That's quite a long name you have " + name)
else:
    print("I like that name, it fits you well.")
gender = input("So, " + name + " what gender are you? You do not have to answer this question if it causes you discomfort, just leave this answer blank. ")
if gender.startswith("m") or gender.startswith("M"):
    print("Well we could always use another guy in the workplace.")
if gender.startswith("f") or gender.startswith("F"):
    print("Well we could always use another woman in the workplace.")