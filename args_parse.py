prefix = (";;")
words = input("Say command with ;; at start: ")
if(words.startswith(prefix)):
    args = words.removeprefix(prefix).split(" ")
