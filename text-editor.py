# non-interactive text editor
# everything done, just needs error catching and docstrings

# returns as a string the content of the file named filename, with file positions in the half-open range [from, to).
# If to == -1, the content between from and the end of the file will be returned. If parameter to exceeds the file length, 
# then the function raises exception ValueError with a corresponding error message. 
def ed_read(filename, sfrom=0, to=-1):
	with open (filename, "r") as in_file:
		contents = in_file.read()	
	if to == -1:
		to = None
	contents = contents[sfrom:to]
	return contents
	
# finds string search_str in the file named by filename and returns a list with index positions in the file text where the string 
# search_str is located. E.g. it returns [4, 100] if the string was found at positions 4 and 100. 
# It returns [] if the string was not found.
def ed_find(filename, search_str):
	contents = ed_read(filename)
	return list(find_all(contents, search_str))
	
# helper function to find substrings
def find_all(contents, search_str):
	start = 0
	while True:
		start = contents.find(search_str, start)
		if start == -1:
			return
		yield start
		start += 1
	
# replaces search_str in the file named by filename with string replace_with. If occurrence==-1, then it replaces ALL occurrences.
# If occurrence>=0, then it replaces only the occurrence with index occurrence, where 0 means the first,
# 1 means the second, etc. If the occurrence argument exceeds the actual occurrence index in the file of that string, 
# the function does not do the replacement. The function returns the number of times the string was replaced. 
def ed_replace(filename, search_str, replace_with, occurrence=-1):
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
	return count
	
# appends string to the end of the file. If the file does not exist, a new file is created with the given file name. 
# The function returns the number of characters written to the file.
def ed_append(filename, string):
	with open (filename, "a") as out_file:
		out_file.write(string)
	return len(string)

# for each tuple (position, s) in collection pos_str_col (e.g. a list) this function writes to the file at position pos the string s.
# This function overwrites some of the existing file content. If any position parameter is invalid (< 0) or greater than 
# the file contents size, the function does not change the file and raises ValueError with a proper error message. 
# In case of no errors, the function returns the number of strings written to the file. Assume the strings to be written do not overlap.
def ed_write(filename, pos_str_col):
	count = 0
	contents = ed_read(filename)
	# x[0] = index to start overwrite
	# x[1] = string
	for x in pos_str_col:
		contents = contents[:x[0]] + x[1] + contents[x[0]+len(x[1]):]
		count += 1
	with open (filename, "w") as out_file:
		out_file.write(contents)
	return count

# for each tuple (position, s) in collection pos_str_col (e.g. a list) this function inserts into to the file content the string s 
# at position pos. This function does not overwrite the existing file content, as seen in the examples below. If any 
# position parameters is invalid (< 0) or greater than the original file content length, the function does not change the file at 
# all and raises ValueError with a proper error message. In case of no errors, the function returns the number of strings inserted to the file.
def ed_insert(filename, pos_str_col):
	count = 0
	contents = ed_read(filename)
	# x[0] = index to start write
	# x[1] = string
	for x in pos_str_col:
		contents = contents[:x[0]] + x[1] + contents[x[0]:]
		count += 1
	with open (filename, "w") as out_file:
		out_file.write(contents)
	return count
	
# example code
fn = "file1.txt" # assume this file does not exist yet.
ed_append(fn, "0123456789") # this will create a new file
ed_append(fn, "0123456789") # the file content is: 01234567890123456789

print(ed_read(fn, 3, 9)) # prints 345678. Notice that the interval excludes index to (9)
print(ed_read(fn, 3)) # prints from 3 to the end of the file: 34567890123456789

lst = ed_find(fn, "345")
print(lst) # prints [3, 13]
print(ed_find(fn, "356")) # prints []

# ed_replace(fn, "345", "ABCDE", 1) # changes the file to 0123456789012ABCDE6789

# assume we reset the file content to 01234567890123456789  (not shown)
# ed_replace(fn, "345", "ABCDE") # changes the file to 012ABCDE6789012ABCDE6789

# assume we reset the file content to 01234567890123456789 (not shown)
# this function overwrites original content:
# ed_write(fn, ((2, "ABC"), (10, "DEFG"))) # changes file to: 01ABC56789DEFG456789
# ed_write(fn, [(2, "ABC"), (10, "DEFG")]) # changes file to: 01ABC56789DEFG456789 (list)

# assume we reset the file content to 01234567890123456789 (not shown)
# ed_write(fn, ((2, "ABC"), (30,"DEFG"))) # fails. raises ValueError("invalid position 30")

# assume we reset the file content to 01234567890123456789 (not shown)
# this function inserts new text, without overwriting:
ed_insert(fn, ((2, "ABC"), (10, "DEFG"))) # changed file to: 01ABC23456789DEFG0123456789