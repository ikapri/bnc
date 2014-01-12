import random
import itertools
import bnc
import util			



class Play:
	def __init__(self):
		self.p1 = bnc.Player()
		self.p2 = bnc.Bot()

	def play(self):
		while True:
			g1 = self.p1.guess()
			b1,c1 = util.check(self.p2.num,g1)
			print "Bulls:%s   Cows:%s" % (b1,c1)
			if b1 == 4:
				print "You Won in %s chances..." % self.p1.chance
				exit()
			g2 = self.p2.guess()	
			print '\t\t\t\t\t\t\t\t',
			print "Bot guessed...%s" % g2			
			b2,c2 = util.check(self.p1.num,g2)
			print '\t\t\t\t\t\t\t\t',
			print "Bulls:%s    Cows:%s" % (b2,c2)
			if b2 == 4:
				print "You lost...Your number is %s" % g2
				print "Bots number is %s....!" % self.p2.num
				exit()
			self.p2.prune(g2,b2,c2)	





if __name__ == '__main__':
	p = Play()
	p.play()