#TODO: add comments, refactor

#function for inputting tuples, data types of input and the separator are passed in
#working correctly
def input_tuple(prompt, types, sep=","):
	try:
		#dictionary for checking valid bool inputs
		bool_dict = {"T":True, "t":True, "true":True, "True":True, "TRUE":True, "F":False, "f":False, "false":False, "False":False, "FALSE":False}
		
		#take user input, throw error if wrong number of parameters
		user_input_tuple = input(prompt).split(sep)
		if len(types) != len(user_input_tuple):
			raise IndexError() 
		
		#iterate over expected types
		output_tuple = []
		for i in range(0, len(types)):
			#if bool, check if it is valid bool input, throw error if not
			if types[i] == bool:
				if user_input_tuple[i] in bool_dict:
					output_tuple.append(bool_dict[user_input_tuple[i]])
				else:
					raise ValueError()
			#if not bool, try to use types constructor on user input. will throw value error if fails
			else:
				output_tuple.append(types[i](user_input_tuple[i]))
	
	#error catching
	except IndexError:
		print("ERROR: Wrong number of parameters, please check your input and try again")
		return ()
	except ValueError:
		print("ERROR: Wrong type of one or more non-Boolean parameters, please check your input and try again")
		return ()
	except KeyError:
		print("ERROR: Booleans must be equal to true or false, please check your input and try again")
		return ()
	
	#if no error, return output tuple
	else:
		return tuple(output_tuple)
		
#same function but using a list comprehension instead
#working correctly
def input_tuple_lc(prompt, types, sep=","):
	try:
		#dictionary for checking valid bool inputs
		bool_dict = {"T":True, "t":True, "true":True, "True":True, "TRUE":True, "F":False, "f":False, "false":False, "False":False, "FALSE":False}
		
		#take user input, throw error if wrong number of parameters
		user_input_tuple = input(prompt).split(sep)
		if len(types) != len(user_input_tuple):
			raise IndexError() 	

		#list comprehension that adds item to output tuple if the types constructor succeeds, and if it is a proper bool input when expected
		output_tuple = [types[i](x) if (types[i] != bool) else bool_dict[x] for i, x in enumerate(user_input_tuple)]

	#error catching	
	except IndexError:
		print("ERROR: Wrong number of parameters, please check your input and try again")
		return ()
	except ValueError:
		print("ERROR: Wrong type of one or more non-Boolean parameters, please check your input and try again")
		return ()
	except KeyError:
		print("ERROR: Booleans must be equal to true or false, please check your input and try again")
		return ()
	
	#if no error, return output tuple
	else:
		return tuple(output_tuple)

#reading tuples from file
#working correctly
def read_tuple(file_obj, types, sep=","):
	try:
		#dictionary for checking valid bool inputs
		bool_dict = {"T":True, "t":True, "true":True, "True":True, "TRUE":True, "F":False, "f":False, "false":False, "False":False, "FALSE":False}
		
		#take first line of file, throw error if wrong number of parameters
		input_tuple = f.readline().strip().split(sep)
		if len(types) != len(input_tuple):
			raise IndexError()

		#list comprehension that adds item to output tuple if the types constructor succeeds, and if it is a proper bool input when expected
		output_tuple = [types[i](x) if (types[i] != bool) else bool_dict[x] for i, x in enumerate(input_tuple)]			
		
	#error catching	
	except IndexError:
		print("ERROR: Wrong number of parameters, please check your input and try again")
		return ()
	except ValueError:
		print("ERROR: Wrong type of one or more non-Boolean parameters, please check your input and try again")
		return ()
	except KeyError:
		print("ERROR: Booleans must be equal to true or false, please check your input and try again")
		return ()
	
	#if no error, return output tuple
	else:
		return tuple(output_tuple)

#function used for testing
#parameters:
#b - boolean, normally a tested condition: true if test passed, false otherwise
#testname - the test name
#msgOK - string to be printed if test passed
#msgFailed - string to be printed if test failed
def testif(b, testname, msgOK="", msgFailed=""):
	if b:
		print("Success: "+ testname + "; " + msgOK)
	else:
		print("Failed: "+ testname + "; " + msgFailed)
	return b
		
#main code, tests "fail" if error happens
testif(input_tuple("Enter first name, last name, age (float), ID (int), fulltime (bool): ", \
(str, str, float, int, bool), ",") != (), "test 1 (no list comprehension)")

testif(input_tuple_lc("Enter first name, last name, age (float), ID (int), fulltime (bool): ", \
(str, str, float, int, bool), ",") != (), "test 2 (list comprehension)")

try:
	f = open("cars.csv", "r")
except FileNotFoundError:
	testif(False, "test 3 (read from file cars.csv)", "", "That file does not exist. Please try again")
else:
	testif(read_tuple(f, (str, str, float, int, bool), ",") ==  ("Lada","Niva",19.5,1987,False), "test 3 (read from file cars.csv)")
	f.close()