# iterator class for generating a sequence of the first n prime numbers
class PrimeSeq:
	def __init__(self, n):
		self.__primes = []
		self.current = 1
		self.n = n
	
	def __iter__(self):
		return self
		
	def __next__(self):
		if len(self.__primes) >= self.n:
			raise StopIteration
		else:	
			test = self.current + 1
			while True:
				isPrime = True
				for p in self.__primes:
					if test % p == 0:
						isPrime = False
						break
				if isPrime:
					self.__primes.append(test)
					self.current = test
					break
				else:
					test += 1
			return self.current

# generator for generating the first n prime numbers		
def prime_gen(n):
	test = 1
	count = 0
	while count < n:
		test += 1
		while True:
			for i in range(2, test//2 + 1):
				if test % i == 0:
					test += 1
					break
			else:
				break
		yield test
		count += 1
	
def main():
	primes_lst = [p for p in PrimeSeq(100)]
	print(primes_lst)
	primes_lst2 = [p for p in prime_gen(100)]
	print(primes_lst2)
	
main()
		

