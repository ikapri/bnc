import random , itertools
from util import check , generate_random
from clint.textui import puts

class Bot:
	def __init__(self,player_num):
		self.chance = 0
		self.digits = "0123456789"
		self.ss = self.gen_ss()
		self.num = generate_random()
		self.player_num = player_num
		if player_num == 1:
			self.indentation = 1
		else:
			self.indentation = 50
			


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
			guessed_num = generate_random()
		else:
			self.chance+=1
			guessed_num = random.choice(self.ss)
		return guessed_num	

	def guess_response(self,guess,b,c):
		puts("Player %s Guessed ---> %s" % (self.player_num,guess))
		puts("Bulls %s ..... Cows %s" % (b,c))
		self.prune(guess,b,c)
	
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
	def __init__(self,player_num):
		self.player_num = player_num
		self.num = self.take_input()
		self.chance = 0		
		if player_num == 1:
			self.indentation = 1
		else:
			self.indentation = 50

	def take_input(self):
		""" take input from user """
		puts("Player %s , Enter Your 4 digit Secret Number without repeating digits" % self.player_num)
		num = raw_input()
		if not self.validate_input(num):
			puts("Invalid Number...Generating Random Number On Your Behalf")
			num = generate_random()
			puts("Your Number is ... %s"%num)
		return num

	def validate_input(self,num):
		if not len(set(num)) == 4:
			return False
		else:
			return True	
	
	def guess(self):
		while True:
			puts("Guess opponents Number")
			num = raw_input()
			if not self.validate_input(num):
				puts("Please enter 4 digit number with non repeating digits...Try Again")
				continue
			else:
				self.chance+=1
				return num

	def guess_response(self,guess,b,c):
		puts("Player %s Guessed ---> %s" % (self.player_num,guess))
		puts("Bulls %s ..... Cows %s" % (b,c))