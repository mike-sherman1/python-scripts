# everything working correctly, just need good parameters and docstrings / comments

# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
# Predator-Prey Simulation
# four classes are defined: animal, predator, prey, and island where island is where the simulation is taking place,
# i.e. where the predator and prey interact (live). A list of predators and prey are instantiated, and
# then their breeding, eating, and dying are simulated.

import random
import time
import pylab

#Island is n X n grid where zero value indicates not occupied
class Island (object):
	# Initialize grid to all 0's, then fill with animals
	def __init__(self, n, prey_count=0, predator_count=0, human_count=0):
		# print(n,prey_count,predator_count)
		self.grid_size = n
		self.grid = []
		for i in range(n):
			row = [0]*n    # row is a list of n zeros
			self.grid.append(row)
		self.init_animals(prey_count,predator_count,human_count)

	# Put some initial animals on the island
	def init_animals(self,prey_count,predator_count,human_count):
		count = 0
		# while loop continues until prey_count unoccupied positions are found
		while count < prey_count:
			x = random.randint(0,self.grid_size-1)
			y = random.randint(0,self.grid_size-1)
			if not self.animal(x,y):
				new_prey=Prey(island=self,x=x,y=y)
				count += 1
				self.register(new_prey)
		count = 0
		# same while loop but for predator_count
		while count < predator_count:
			x = random.randint(0,self.grid_size-1)
			y = random.randint(0,self.grid_size-1)
			if not self.animal(x,y):
				new_predator=Predator(island=self,x=x,y=y)
				count += 1
				self.register(new_predator)
		count = 0
		# same while loop but for human_count
		while count < human_count:
			x = random.randint(0,self.grid_size-1)
			y = random.randint(0,self.grid_size-1)
			if not self.animal(x,y):
				new_human=Human(island=self,x=x,y=y)
				count += 1
				self.register(new_human)
		
	# Animals have a moved flag to indicated they moved this turn. Clear that so we can do the next turn
	def clear_all_moved_flags(self):
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				if self.grid[x][y]:
					self.grid[x][y].clear_moved_flag()

	# Return size of the island: one dimension
	def size(self):
		return self.grid_size

	# Register animal with island, i.e. put it at the animal's coordinates
	def register(self,animal):
		x = animal.x
		y = animal.y
		self.grid[x][y] = animal

	# Remove animal from island
	def remove(self,animal):
		x = animal.x
		y = animal.y
		self.grid[x][y] = 0

	# Return animal at location (x,y)
	def animal(self,x,y):
		if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
			return self.grid[x][y]
		else:
			return -1  # outside island boundary

	# String representation for printing. (0,0) will be in the lower left corner
	def __str__(self):
		s = ""
		for j in range(self.grid_size-1,-1,-1):  # print row size-1 first
			for i in range(self.grid_size):      # each row starts at 0
				if not self.grid[i][j]:
					# print a '.' for an empty space
					s+= "{:<2s}".format('.' + "  ")
				else:
					s+= "{:<2s}".format((str(self.grid[i][j])) + "  ")
			s+="\n"
		return s

	# count all the prey on the island
	def count_prey(self):
		count = 0
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				animal = self.animal(x,y)
				if animal:
					if type(animal) == Prey:
						count+=1
		return count

	# count all the predators on the island
	def count_predators(self):
		count = 0
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				animal = self.animal(x,y)
				if animal:
					if type(animal) == Predator:
						count+=1
		return count
		
	# count all the humans on the island
	def count_humans(self):
		count = 0
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				animal = self.animal(x,y)
				if animal:
					if type(animal) == Human:
						count+=1
		return count

class Animal(object):
	# Initialize the animal's and their positions
	def __init__(self, island, x=0, y=0, s="A"):
		self.island = island
		self.name = s
		self.x = x
		self.y = y
		self.moved=False

	# Return coordinates of current position
	def position(self):
		return self.x, self.y

	def __str__(self):
		return self.name

	# Look in the 8 directions from the animal's location
	# and return the first location that presently has an object
	# of the specified type. Return 0 if no such location exists
	def check_grid(self,type_looking_for=int):
		# neighbor offsets
		offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
		result = 0
		for i in range(len(offset)):
			x = self.x + offset[i][0]  # neighboring coordinates
			y = self.y + offset[i][1]
			if not 0 <= x < self.island.size() or not 0 <= y < self.island.size():
				continue
			if type(self.island.animal(x,y))==type_looking_for:
				result=(x,y)
				break
		return result

	# Move to an open, neighboring position
	def move(self):
		if not self.moved:
			location = self.check_grid(int)
			if location:
				# print('Move, {}, from {},{} to {},{}'.format(type(self),self.x,self.y,location[0],location[1]))
				self.island.remove(self)   # remove from current spot
				self.x = location[0]       # new coordinates
				self.y = location[1]
				self.island.register(self) # register new coordinates
				self.moved=True

	# Breed a new Animal.If there is room in one of the 8 locations
	# place the new Animal there. Otherwise you have to wait.
	def breed(self):
		if self.breed_clock <= 0:
			location = self.check_grid(int)
			if location:
				# print('Breeding Animal {},{}'.format(self.x,self.y))
				self.breed_clock = self.breed_time
				the_class = self.__class__
				new_animal = the_class(self.island,x=location[0],y=location[1])
				self.island.register(new_animal)

	def clear_moved_flag(self):
		self.moved=False

class Prey(Animal):
	def __init__(self, island, x=0,y=0,s="O"):
		Animal.__init__(self,island,x,y,s)
		self.breed_clock = self.breed_time
		# print('Init Prey {},{}, breed:{}'.format(self.x, self.y,self.breed_clock))

	# Prey only updates its local breed clock
	def clock_tick(self):
		self.breed_clock -= 1
		# print('Tick Prey {},{}, breed:{}'.format(self.x,self.y,self.breed_clock))

class Predator(Animal):
	def __init__(self, island, x=0,y=0,s="X"):
		Animal.__init__(self,island,x,y,s)
		self.starve_clock = self.starve_time
		self.breed_clock = self.breed_time
		# print('Init Predator {},{}, starve:{}, breed:{}'.format(self.x,self.y,self.starve_clock,self.breed_clock))

	# Predator updates both breeding and starving
	def clock_tick(self):
		self.breed_clock -= 1
		self.starve_clock -= 1
		# print('Tick, Predator at {},{} starve:{}, breed:{}'.format(self.x,self.y,self.starve_clock,self.breed_clock))
		if self.starve_clock <= 0:
			# print('Death, Predator at {},{}'.format(self.x,self.y))
			self.island.remove(self)

	# Predator looks for one of the 8 locations with Prey. If found
	# moves to that location, updates the starve clock, removes the Prey
	def eat(self):
		if not self.moved:
			location = self.check_grid(Prey)
			if location:
				# print('Eating: pred at {},{}, prey at {},{}'.format(self.x,self.y,location[0],location[1]))
				self.island.remove(self.island.animal(location[0],location[1]))
				self.island.remove(self)
				self.x=location[0]
				self.y=location[1]
				self.island.register(self)
				self.starve_clock=self.starve_time
				self.moved=True
				
class Human(Predator):
	def __init__(self, island, x=0,y=0,s="H"):
		Predator.__init__(self,island,x,y,s)
		self.starve_clock = self.starve_time
		self.breed_clock = self.breed_time
		self.hunt_clock = self.hunt_time
		# print('Init Human {},{}, starve:{}, breed:{}, hunt:{}'.format(self.x,self.y,self.starve_clock,self.breed_clock,self.hunt_clock))
		
	# Human updates breeding, starving, and hunting
	def clock_tick(self):
		self.breed_clock -= 1
		self.starve_clock -= 1
		self.hunt_clock -= 1
		# print('Tick, Human at {},{} starve:{}, breed:{}, hunt:{}'.format(self.x,self.y,self.starve_clock,self.breed_clock,self.hunt_clock))
		if self.starve_clock <= 0:
			# print('Death, Human at {},{}'.format(self.x,self.y))
			self.island.remove(self)

	# Human looks for one of the 8 locations with Predator. If found moves to that location, 
	# updates the hunt clock, removes the Predator
	def hunt(self):
		if self.hunt_clock <= 0:
			if not self.moved:
				location = self.check_grid(Predator)
				if location:
					# print('Hunting: human at {},{}, predator at {},{}'.format(self.x,self.y,location[0],location[1]))
					self.island.remove(self.island.animal(location[0],location[1]))
					self.island.remove(self)
					self.x=location[0]
					self.y=location[1]
					self.island.register(self)
					self.hunt_clock=self.hunt_time
					self.moved=True

# main simulation. Sets defaults, runs event loop, plots at the end
# book defaults: (predator_breed_time=6, predator_starve_time=3, initial_predators=10, prey_breed_time=3, initial_prey=50, size=10, ticks=300)
def main(human_breed_time=6, human_starve_time=3, human_hunt_time=7, initial_humans=20, predator_breed_time=6, predator_starve_time=3, initial_predators=10, prey_breed_time=3, initial_prey=50, size=10, ticks=300):
	# initialization values
	Predator.breed_time = predator_breed_time
	Predator.starve_time = predator_starve_time
	Prey.breed_time = prey_breed_time
	Human.breed_time = human_breed_time
	Human.starve_time = human_starve_time
	Human.hunt_time = human_hunt_time

	# for graphing
	predator_list=[]
	prey_list=[]
	human_list=[]

	# make an island
	isle = Island(size,initial_prey, initial_predators, initial_humans)
	print(isle)
	print(initial_prey, initial_predators, initial_humans)
	
	# test
	# a = Animal(isle)
	# x = Predator(isle)
	# o = Prey(isle)
	# h = Human(isle)
	# print(isinstance(h,Predator))
	# print(type(h))
	# print(type(x))

	# event loop.
	# For all the ticks, for every x,y location.
	# If there is an animal there, try eat, move, breed and clock_tick
	for i in range(ticks):
		# important to clear all the moved flags!
		isle.clear_all_moved_flags()
		for x in range(size):
			for y in range(size):
				animal = isle.animal(x,y)
				if animal:
					if isinstance(animal,Predator):
						animal.eat()
					if isinstance(animal,Human):
						animal.hunt()
					animal.move()
					animal.breed()
					animal.clock_tick()

		# record info for display, plotting
		prey_count = isle.count_prey()
		predator_count = isle.count_predators()
		human_count = isle.count_humans()
		if prey_count == 0:
			print('Lost the Prey population. Quiting.')
			break
		# if predator_count == 0:
			# print('Lost the Predator population. Quitting.')
			# break
		prey_list.append(prey_count)
		predator_list.append(predator_count)
		human_list.append(human_count)
		# print out every 10th cycle, see what's going on
		if not i%10:
			print(prey_count, predator_count, human_count)
		# print the island, hold at the end of each cycle to get a look
		# print('*'*20)
		# print(isle)
		# ans = input("Return to continue")

	print(isle)
	pylab.plot(range(0,ticks), predator_list, label="Predators")
	pylab.plot(range(0,ticks), prey_list, label="Prey")
	pylab.plot(range(0,ticks), human_list, label="Humans")
	pylab.legend(loc="best", shadow=True)
	pylab.show()
	
main()

