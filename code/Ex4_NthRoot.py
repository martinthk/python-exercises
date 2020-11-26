# Ex4: Finding the nth root

import math
x=int(input('Please enter a number: '))
n=int(input('Please enter a value for n: '))
y=10**(math.log(x,10)/n)
print('The',n,'th root is',y)
