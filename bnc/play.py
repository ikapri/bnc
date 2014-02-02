import random
import itertools
import bnc
import util			
from clint.textui import puts, indent


class Play:
	def __init__(self):
		self.players = []
		for i in range(2):
			while True:
				print """ Choose Option For Player %s 
					1 - Human
					2 - Bot""" % str(i+1)
				opt = raw_input()
				try:
					opt = int(opt)
					if opt == 1:
						self.players.append(bnc.Player(i+1))
					elif opt == 2:
						self.players.append(bnc.Bot(i+1))
					else:
						print "Not A Valid Option"
						continue
					break	
				except:
					print "Not A Valid Option"
		self.turn = 0#0 for Player 1 , 1 for Player 2
		for i in range(20):
			print '\n'

	def play(self):
		while True:
			player = self.players[self.turn]
			self.turn = (self.turn + 1) % 2
			opponent = self.players[self.turn]
			with indent(player.indentation):
				puts("Player %s's Turn" % player.player_num)
				guess = player.guess()
				b,c = util.check(opponent.num,guess)
				player.guess_response(guess,b,c)
				if b == 4:
					print "Player %s Won in %s chances..." % (player.player_num,player.chance)
					print "Player %s's Number is %s" % (player.player_num ,player.num)
					break

if __name__ == '__main__':
	p = Play()
	p.play()