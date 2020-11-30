# Ex13: Heron’s method of convergence
# compute √𝑎 using Heron's method of Convergence 

# Take as input a number (a), and an initial guess for the value of √𝑎
# and repeatedly apply equation 1 until the approximate solution converges to close to the true solution.

import math

a = int(input('Enter the value for a: '))
guess = int(input('Enter your initial guess for x: '))
xOld = guess
xNew = 1/2*(xOld+(a/xOld))

while abs(xOld-xNew) > 0.001:
    xOld = xNew
    xNew = (1/2)*(xOld + a/xOld)
    print(xNew)

print('The square root of', a, 'is', xNew)
