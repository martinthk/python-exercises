# Ex8: takes a number n as input from the user
# and simulates n coin flips.
import random

n = int(input("How many times would you like to flip the coin: "))

for k in range(n):
    r = random.random()

    if (r > 0.5):
        print("The coin campe up heads")
    else:
        print("The coin came up tails")
