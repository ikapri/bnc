import random , itertools
from util import check , generate_random

class Bot:
	def __init__(self):
		self.chance = 0
		self.digits = "0123456789"
		self.ss = self.gen_ss()
		self.num = generate_random()

	def gen_ss(self):
		""" generate sample space i.e all possible 4 digit
		    numbers without repeating digits
		""" 
		ss = []
		per = itertools.permutations(self.digits,4)
		for p in per:
			ss.append(''.join(p))
		return ss

	def guess(self):
		""" guess the opponents number """
		if self.chance == 0:
			self.chance+=1
			return generate_random()
		else:
			self.chance+=1
			return random.choice(self.ss)		
	
	def prune(self,guess,b,c):
		""" reduce the sample space based on the 
		    response to the guess
		"""    
		ss1 = []
		for s in self.ss:
			b1,c1 = check(guess,s)
			if b1==b and c1==c:
				ss1.append(s)
		self.ss = ss1

class Player:
	def __init__(self):
		self.num = self.take_input()
		self.chance = 0

	def take_input(self):
		""" take input from user """
		num = raw_input("Enter Your 4 digit Secret Number without repeating digits\n")
		if not self.validate_input(num):
			print "Invalid Number...Generating Random Number for Computer to Guess"
			num = generate_random()
			print "Your Number is ... %s"%num
			return num
		else:		
			return num

	def validate_input(self,num):
		if not len(set(num)) == 4:
			return False
		else:
			return True	
	
	def guess(self):
		while True:
			num = raw_input("Guess Opponents Number....\n")
			if not self.validate_input(num):
				print "Please enter 4 digit number with non repeating digits...Try Again"
				continue
			else:
				self.chance+=1
				return num