#functions
import random

from my_functions import greet

with open("data.txt", "w") as file:
    # file.write("99\n")
    # file.write("69\n")

    for temp in range(100):
        x = random.randint(-10,65)
        file.write(str(x)+"\n")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

#install
#use
greet()


