# Ex10: Modify the program from previous version
# allow the user to enter the probability of the coin flip coming up heads.
# Then calculate the ratio of Heads to total number of flips.
import random
t = 0
h = 0
n = int(input("How many times would you like to flip the coin: "))
p = float(input("What probability would you like to give to heads <0 to 1>: "))

for k in range(n):
    r = random.random()

    if (r > p):
        #print("The coin campe up heads")
        h += 1
    else:
        #print("The coin came up tails")
        t += 1

print("There were", h, "heads and", t, "tails.")
print("Ratio of heads to total flips is", h/n)
