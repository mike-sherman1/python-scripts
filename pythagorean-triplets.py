#This program computes all possible Pythagorean triplets from 0 to n (0 < a,b,c <= n)

def find_pythag_triplets(limit):
	result = ""
	m = 2
	a, b, c = 0, 0, 0
	while c < limit:
		for i in range(1, m):
			a = m*m - i*i
			b = 2*m*i
			c = m*m + i*i
			if c > limit:
				break
			result += str(a) + " " + str(b) + " " + str(c) + "\n"
		m += 1
	return result
	
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

choice = int(input("Enter your own limit n or enter -1 to test program: "))
if choice == -1:
	testif(find_pythag_triplets(0) == "", "test 1 (n = 0)")
	testif(find_pythag_triplets(4) == "", "test 2 (n = 4)")
	testif(find_pythag_triplets(5) == "3 4 5\n", "test 3 (n = 5)")
	testif(find_pythag_triplets(10) == "3 4 5\n8 6 10\n", "test 4 (n = 10)")
	testif(find_pythag_triplets(20) == "3 4 5\n8 6 10\n5 12 13\n15 8 17\n12 16 20\n", "test 5 (n = 20)")
else:
print(find_pythag_triplets(choice))
