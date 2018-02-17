#This program breaks a dollar amount into quarters, dimes, and pennies using the greedy algorithm.

while True:
	try:
		#input is multiplied by 100, this program works in cents because of rounding errors
		amount = float(input("Enter amount: ")) * 100
	except EOFError:
		break
	except ValueError:
		print("Invalid input.")
		break
	if a < 0:
		print("Invalid input.")
		break
	
	#coins will be subtracted from amount variable, so the user's original input is saved for later
	original = amount / 100
	
	result = [0, 0, 0]
	denom = [25, 10, 1]
	
	for x in range(0, 3):
		while amount >= denom[x]:
			amount -= denom[x]
			result[x] += 1
	
	print("$" + str(original) + " makes " + str(result[0]) + " quarters, " + str(result[1]) + " dimes, and " + str(result[2]) + " pennies (" + str(result[0] + result[1] + result[2]) \
+ " coins), total amount in coins: $" + str((result[0]*denom[0] + result[1]*denom[1] + result[2]*denom[2])/100) + ".")
