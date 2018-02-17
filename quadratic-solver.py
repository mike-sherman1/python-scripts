#This program solves and plots quadratic equations.

import math
import pylab as pylab

while True:
    try:
        a = float(input("Enter a: "))
    except EOFError:
        break
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
	
    
    if (b**2 - 4*a*c) < 0:
        print("no real solutions")
    else:
        x1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    
        if (b**2 - 4*a*c) == 0:
            print("one solution: " + str(x1))
        if (b**2 - 4*a*c) > 0:
            print("two solutions: x1 = " + str(x1) + " x2 = " + str(x2))
    
        x = pylab.linspace(-5, 5, num=100)
        for val in x:
            y = a*x*x + b*x + c
        
        pylab.plot(x,y, marker='.', color='b')
pylab.show()
