# Ex9: Modify the program from previous version
# so that it now counts the number of heads and/or tails
# and saves this value in a variable.
# Use this variable to print the total number of heads and the total number of tails.
import random
t = 0
h = 0
n = int(input("How many times would you like to flip the coin: "))

for k in range(n):
    r = random.random()

    if (r > 0.5):
        print("The coin campe up heads")
        h += 1
    else:
        print("The coin came up tails")
        t += 1

print("Total number of Heads:", h)
print("Total number of Tails:", t)
