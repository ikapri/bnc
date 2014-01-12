import random
import itertools

def gen_ss():
	ss = []
	digits = '0123456789'
	per = itertools.permutations(digits,4)
	for p in per:
		ss.append(''.join(p))
	return ss	



def guess():
	global chance
	global ss
	if chance == 0:
		chance+=1
		return '0123'
	elif chance == 1:
		chance+=1
		return random.choice(['0124','0132','0134','0145','0214','0231','0234','0245','0456','1032','1034','1045','1204','1230','1234','1245','1435','1456','4567'])
	else:
		chance+=1
		return random.choice(ss)

def check(num,guess):
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

def prune(ss,guess,b,c):
	ss1 = []
	for s in ss:
		b1,c1 = check(guess,s)
		if b1==b and c1==c:
			ss1.append(s)
	return ss1
			
def take_input():
	num = raw_input("Enter Your 4 digit Secret Number without repeating digits")
	if not validate_input(num):
		print "Invalid Number...Generating Random Number for Computer to Guess"
		num = generate_random()
		print "Your Number is ... %s"%generate_random()
		return num
	else:		
		return num

def validate_input(num):
	if not len(set(num)) == 4:
		return False
	else:
		return True	

def generate_random():
	d = []
	digits = "0123456789"
	while True:
		g = random.choice(digits)
		if g in d:
			continue
		else:
			d.append(g)
			if len(d) == 4:
				return ''.join(d)	

if __name__ == '__main__':
	num = take_input()
	print num
	#exit()
	chance = 0
	ss = gen_ss()
	while True:
		print "Sample Space-------------->"+str(len(ss))
		g = guess()
		print "Guess........---->"+str(g)
		b,c = check(num,g)
		print "Bulls %s  ,, Cows %s"%(str(b),str(c))
		if b == 4:
			print "WON"
			exit()
		else:
			ss = prune(ss,g,b,c)
