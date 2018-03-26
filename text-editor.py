# non-interactive text editor

import os

def ed_read(filename, sfrom=0, to=-1):
	"""Function for reading a file.
	
	param filename: name of file to be read
	param sfrom: starting position
	param to: ending position
	"""
	try:
		with open (filename, "r") as in_file:
			contents = in_file.read()
		if to >= len(contents):
			raise ValueError("Upper bound exceeds file length, please check your input and try again.")
		if to == -1:
			to = None
		contents = contents[sfrom:to]
		return contents
	except ValueError as e:
		print("ERROR: " + str(e))
		return None
	
def ed_find(filename, search_str):
	"""Function for finding occurrences of a substring in the file.
	
	param filename: name of file to be searched
	param search_str: the string to be searched for
	"""
	contents = ed_read(filename)
	return list(find_all(contents, search_str))
	
def find_all(contents, search_str):
	"""Helper function to find substrings.
	
	param contents: contents of the file
	param search_str: string to be searched for
	"""
	start = 0
	while True:
		start = contents.find(search_str, start)
		if start == -1:
			return
		yield start
		start += 1
	
def ed_replace(filename, search_str, replace_with, occurrence=-1):
	"""Function for replacing substrings in the file.
	
	param filename: name of file to be edited
	param search_str: the string to be replaced
	param replace_with: the string to replace the search string with
	param occurrence: which occurrence of search string to be overwritten(-1 overwrites all occurrences)
	"""
	try: 
		count = 0
		contents = ed_read(filename)
		if occurrence == -1:
			contents = contents.replace(search_str, replace_with)
			count = len(list(find_all(contents, search_str)))
		else:
			indexes = list(find_all(contents, search_str))
			i = indexes[occurrence]
			# splits the string at desired index i, then replaces the first occurrence in the 2nd half of the string (which of course is index i)
			contents = contents[:i] + contents[i:].replace(search_str, replace_with, 1)
		with open (filename, "w") as out_file:
			out_file.write(contents)
	except IndexError:
		print("ERROR: Occurrence index parameter invalid, please check your input and try again.")
	finally:
		return count
	
def ed_append(filename, string):
	"""Function for appending to the file.
	
	param filename: name of file to be edited
	param string: the string to be appended
	"""
	with open (filename, "a") as out_file:
		out_file.write(string)
	return len(string)

def ed_write(filename, pos_str_col):
	"""Function for overwriting strings at specific positions in the file.
	
	param filename: name of file to be edited
	param pos_str_col: a collection of tuples (position, string)
	"""
	try: 
		count = 0
		contents = ed_read(filename)
		# x[0] = index to start overwrite
		# x[1] = string
		for x in pos_str_col:
			if x[0] < 0 or x[0] >= len(contents):
				raise ValueError("One or more positional parameter(s) are invalid, please check your input and try again. ")
			contents = contents[:x[0]] + x[1] + contents[x[0]+len(x[1]):]
			count += 1
		with open (filename, "w") as out_file:
			out_file.write(contents)
		return count
	except ValueError as e:
		print("ERROR: " + str(e))
		return None

def ed_insert(filename, pos_str_col):
	"""Function for inserting strings at specific positions without overwriting the file.
	
	param filename: name of file to be inserted into
	param pos_str_col: a collection of tuples (position, string)
	"""
	try:
		count = 0
		contents = ed_read(filename)
		# x[0] = index to start write
		# x[1] = string
		for x in pos_str_col:
			if x[0] < 0 or x[0] >= len(contents):
				raise ValueError("One or more positional parameter(s) are invalid, please check your input and try again. ")
			contents = contents[:x[0]] + x[1] + contents[x[0]:]
			count += 1
		with open (filename, "w") as out_file:
			out_file.write(contents)
		return count
	except ValueError as e:
		print("ERROR: " + str(e))
		return None
	
def testif(b, testname, msgOK="", msgFailed=""):
	"""Function used for testing. 
    
	param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
	if b:
		print("Success: "+ testname + "; " + msgOK)
	else:
		print("Failed: "+ testname + "; " + msgFailed)
	return b

def test_ed_write():
	"""Function for testing ed_write."""
	fn = "test.txt"
	if os.path.isfile(fn):
		os.remove(fn)
		
	# initial write
	ed_append(fn, "mike sherman is the best")
	
	# test
	ed_write(fn, [(0, "matt"), (5, "bailey ")])
	testif(ed_read(fn) == "matt bailey  is the best", "TEST ED_WRITE")
	
def test_ed_replace():
	"""Function for testing ed_replace."""
	fn = "test.txt"
	if os.path.isfile(fn):
		os.remove(fn)
		
	# initial write
	ed_append(fn, "mike sherman is the best")
	
	# test
	ed_replace(fn, "mike", "matt", occurrence=-1)
	ed_replace(fn, "sherman", "bailey ", occurrence=-1)
	testif(ed_read(fn) == "matt bailey  is the best", "TEST ED_REPLACE")
	
# some examples that show how to use all the editor functions
def main():	
	fn = "file1.txt" # assume this file does not exist yet.
	os.remove(fn)
	ed_append(fn, "0123456789") # this will create a new file
	ed_append(fn, "0123456789") # the file content is: 01234567890123456789

	print(ed_read(fn, 3, 9)) # prints 345678. Notice that the interval excludes index to (9)
	print(ed_read(fn, 3)) # prints from 3 to the end of the file: 34567890123456789

	lst = ed_find(fn, "345")
	print(lst) # prints [3, 13]
	print(ed_find(fn, "356")) # prints []

	ed_replace(fn, "345", "ABCDE", 1) # changes the file to 0123456789012ABCDE6789

	# reset the file content to 01234567890123456789 
	os.remove(fn)
	ed_append(fn, "01234567890123456789") 
	ed_replace(fn, "345", "ABCDE") # changes the file to 012ABCDE6789012ABCDE6789

	# reset the file content to 01234567890123456789 
	os.remove(fn)
	ed_append(fn, "01234567890123456789") 
	# this function overwrites original content:
	ed_write(fn, ((2, "ABC"), (10, "DEFG"))) # changes file to: 01ABC56789DEFG456789
	ed_write(fn, [(2, "ABC"), (10, "DEFG")]) # changes file to: 01ABC56789DEFG456789 (list)

	# reset the file content to 01234567890123456789 
	os.remove(fn)
	ed_append(fn, "01234567890123456789") 
	# this function inserts new text, without overwriting:
	ed_insert(fn, ((2, "ABC"), (10, "DEFG"))) # changed file to: 01ABC23456789DEFG0123456789
