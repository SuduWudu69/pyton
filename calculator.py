import math
import random
num_1 = input("First Number: ")
num_2 = input("Second Number: ")
operation = input("Please input your function[div, mult, add, sub, pow, root, fact, circle_area, circumference, random]: ")
if operation == "div":
    answer = float(num_1)/float(num_2)
if operation == "mult":
    answer = float(num_1)*float(num_2)
if operation == "add":
    answer = float(num_1)+float(num_2)
if operation == "sub":
    answer = float(num_1)-float(num_2)
if operation == "pow":
    answer = math.pow(float(num_1), float(num_2))
if operation == "root":
    answer = math.pow(float(num_1), 1/float(num_2))
if operation == "fact":
    answer = math.factorial(float(num_1))
if operation == "circle_area":
    answer = math.pow(float(num_1), 2)*math.pi
if operation == "circumference":
    answer = math.pi*2*float(num_1)
if operation == "random":
    answer = random.randint(int(num_1), int(num_2))
print("Your answer is "+ str(answer))