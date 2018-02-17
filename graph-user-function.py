#This program takes a user defined function and displays a graph and a table of x and y values

import math
import pylab as pylab

fun_str = input("Enter function with variable x: ")
ns = float(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

xs = []
ys = []
dx = (xmax - xmin) / ns

x = xmin
print("{:>10}{:>10}".format("x","y"))
print("--------------------")
while x <= xmax:
	xs.append(x)
	y = eval(fun_str)	
	print("{:>+10.4f}{:>+10.4f}".format(x,y))
	ys.append(y)
	x += dx
	
pylab.plot(xs,ys, marker='.', color='b')
pylab.xlabel("x") 
pylab.ylabel("y")
pylab.title(fun_str)
pylab.show()
