import random

def check(num,guess):
		""" check guess against num and return
		    number of bulls and cows
		"""    
		if num == guess:
			return 4,0
		else:
			b=c=0
			for g in guess:
				if g in num:
					if num.index(g) == guess.index(g):
						b+=1	
					else:
						c+=1
			return b,c

def generate_random():
		""" generate random 4 digit number """    
		digits = "0123456789"
		d = []
		while True:
			g = random.choice(digits)
			if g in d:
				continue
			else:
				d.append(g)
				if len(d) == 4:
					return ''.join(d)
