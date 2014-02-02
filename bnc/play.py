import random
import itertools
import bnc
import util			
from clint.textui import puts, indent


class Play:
	def __init__(self):
		self.p1 = bnc.Player(1)
		self.p2 = bnc.Bot(2)

	def play(self):
		while True:
			g1 = self.p1.guess()
			b1,c1 = util.check(self.p2.num,g1)
			self.p1.guess_response(g1,b1,c1)
			if b1 == 4:
				print "You Won in %s chances..." % self.p1.chance
				exit()
			with indent(50):
				g2 = self.p2.guess()	
				b2,c2 = util.check(self.p1.num,g2)
				self.p2.guess_response(g2,b2,c2)
				if b2 == 4:
					print "You lost...Your number is %s" % g2
					print "Bots number is %s....!" % self.p2.num
					exit()





if __name__ == '__main__':
	p = Play()
	p.play()