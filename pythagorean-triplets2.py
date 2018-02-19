#TODO: add comments

def compute_Pythagoreans(n):
	try: 
		output = [(a,b,c) for a in range(1,n+1) for b in range(a,n+1) for c in range(b,n+1) if a**2 + b**2 == c**2]
	except ValueError:
		print("Value n must be an integer. Please try again.")
		return ()
	else:
		return output
	
print(compute_Pythagoreans(int(input("Enter the value of n: "))))

