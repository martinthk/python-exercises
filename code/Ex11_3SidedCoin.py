# Ex11: Extend  program so that it uses 3 sided coins.
import random

n = int(input("How many times would you like to flip the coin? "))

side1 = 0
side2 = 0
side3 = 0

for i in range(n):
    r = random.randrange(1, 4)
    if r == 1:
        print("The coin come up side", r)
        side1 += 1
    elif r == 2:
        print("The coin come up side", r)
        side2 += 1
    elif r == 3:
        print("The coin come up side", r)
        side3 += 1

print("Side 1:", side1, "Side 2:", side2, "Side 3:", side3)
