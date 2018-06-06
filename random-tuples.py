import random
import itertools

# generator that creates an infinite sequence of tuples (a, b) where a and b are random integers, with 0 < a,b < n
def gen_rndtup(n):
	while True:
		yield (random.randint(1,n-1), random.randint(1,n-1))
		
# part a
n = 7
print(list(filter(lambda x: x[0] + x[1] >= n // 2, itertools.islice(gen_rndtup(n), 10))))
		
# part b
rand_tuples = []
for x in range(0,10):
	rand_tuples.append((random.randint(1,n-1), random.randint(1,n-1)))
print(list(((a,b) for (a,b) in rand_tuples if a+b >= n//2)))


	