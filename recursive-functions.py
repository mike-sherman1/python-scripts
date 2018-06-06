from turtle import *
	
# not complete, can't get it to work
def binary_tree(depth, length):
	# stamp()
	if depth <= 0:
		return
	forward(length)
	binary_tree(depth-1, 0.6*length)
	backward(length)
	setheading(270)
	left(60)
	forward(length)
	binary_tree(depth-1, 0.6*length)
	backward(length)
	
def power(x, n):	
	"""Function that recursively computes x^n.
	
	param x: base, any number
	param n: exponent, non-negative integer
	"""
	if n == 0:
		return 1
	elif n % 2 == 0:
		return power(x, n/2)*power(x, n/2)
	else:
		return x*power(x, n//2)*power(x, n//2)
		
# not complete, ran out of time and stressed
def slice_sum(lst, begin, end):
	return None
	
def testif(b, testname, msgOK="", msgFailed=""):
	"""Function used for testing.
	
	param b: boolean, normally a tested condition: true if test passed, false otherwise
	param testname: the test name
	param msgOK: string to be printed if test passed
	param msgFailed: string to be printed if test failed
	returns b
	"""
	if b:
		print("Success: "+ testname + "; " + msgOK)
	else:
		print("Failed: "+ testname + "; " + msgFailed)
	return b
	
def test_power():
	testif(power(0,0) == 1, "Test 1 (base case)")
	testif(power(8,8) == 16777216, "Test 2 (8^8)")
	testif(power(-4,13) == -67108864, "Test 3 ((-4)^13)")
