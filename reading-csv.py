#This is a program for reading and viewing csv files, with the basketball player L. James' stats as an example.
#needs comments

import pylab as pylab
import numpy as np

#working correctly, doesnt do career and seasons lines
def get_csv_data(f, string_pos_lst, sep=""):
	data_lst = []
	data_lst.append(f.readline().strip().split(sep))
	lines = f.readlines() #i guess it automatically skips the first line since we already read it?


	for x in lines:
		x = x.strip().split(sep)
		output = []
		for iLine, xLine in enumerate(x):
			try:
				if iLine in string_pos_lst:
					output.append(str(xLine))
				elif float(xLine):
					output.append(float(xLine))
			except ValueError:
				output = []
				break
		if output != []:
			data_lst.append(output)

	return data_lst

#working correctly
def get_columns(data_lst, cols_lst):
	to_get = []
	for i, x in enumerate(data_lst[0]):
		if x in cols_lst:
			to_get.append(i)
	index_dict = dict(zip(to_get, list(range(len(to_get)))))
	output_list = [[] for i in range(len(to_get))]

	data = data_lst[1:]
	for x in data:
		for iLine, xLine in enumerate(x):
			if iLine in to_get:
				output_list[index_dict[iLine]].append(xLine)

	return output_list

bb_file = open("lb-james.csv", "r")
james_lst = get_csv_data(bb_file, [0, 2, 3, 4], ",")
f.close()

#select 3 pts %, 2 pts %, and free throws %
x = get_columns(james_lst, ["Season"])
y1 = get_columns(james_lst, ["3P%"])
y2 = get_columns(james_lst, ["2P%"])
y3 = get_columns(james_lst, ["FT%"])
ys = get_columns(james_lst, ["3P%", "2P%", "FT%"])

line1, = pylab.plot(x[0],y1[0], color="blue", marker=".", label="3 point percentage")
line2, = pylab.plot(x[0],y2[0], color="red", marker=".", label="2 point percentage")
line3, = pylab.plot(x[0],y3[0], color="green", marker=".", label="Free throw percentage")
pylab.legend(loc="upper right")
pylab.xlabel("Seasons") 
pylab.ylabel("Stats")
pylab.title("Lebron James' stats from 2003-2018")
pylab.show()
