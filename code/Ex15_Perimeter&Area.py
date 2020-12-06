# Ex15: Perimeter & Area

import math

area = 0
perimeter = 0
print('[1]Square [2]Rectangle [3]Triangle [4]Rhombus [0]Quit')
choice = input('Input the number in order to choose that shape: ')

while choice != '0':

    #[1]Square
    if choice == '1':
        side = int(input('Input the length of the side of the square:'))
        perimeter = 4*side
        area = side**2

    #[2]Rectangle
    elif choice == '2':
        l = int(input('Input the length of the rectangle:'))
        b = int(input('Input the base of the rectangle:'))
        perimeter = 2*(l+b)
        area = l*b

    #[3]Triangle
    elif choice == '3':
        #h = int(input('Input the height of the triangle:'))
        #b = int(input('Input the base of the triangle:'))
        a = int(input('Input the 1st side of the triangle:'))
        b = int(input('Input the 2nd side of the triangle:'))
        c = int(input('Input the 3rd side of the triangle:'))
        perimeter = a + b +c
        s = (a+b+c)/2
        #area = (1/2)*b*h
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))


    #[4]Rhombus
    elif choice == '4':
        h = int(input('Input the height of the rhombus:'))
        b = int(input('Input the base of the rhombus:'))
        s = int(input('Input the side of the rhombus:'))
        perimeter = 4*s
        area = h*b

    print('The perimeter is',perimeter)
    print('The area is',area)
    print('[1]Square [2]Rectangle [3]Triangle [4]Rhombus [0]Quit')
    choice = input('Input the number in order to choose that shape: ')

