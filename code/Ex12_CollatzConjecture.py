# Ex12: Write a program that asks (prompts) the user to enter a positive value n . 
# If n is even, divide n by 2. If n is odd, multiply it by 3 and add 1. 
# Each time save the result back to n. 
# Repeat the process until n is equal to 1.

n = int(input("Enter the value for n: "))

if (n > 0):
    while (n != 1):
        if (n % 2 == 0):
            n = n//2
            print(n)
        else:
            n = n*3 + 1
            print(n)

else:
    print('Enter a positive number')
