# Ex1: Find the root of the given quadratic equation

import math
a= int(input('Please input value of A: '))
b= int(input('Please input value of B: '))
c= int(input('Please input value of C: '))

x1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)
x2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)

print('The 1st root is: ',x1)
print('The 2nd root is ',x2)
