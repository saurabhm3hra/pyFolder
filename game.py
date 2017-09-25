from cards_saurabh import deck
from cards_saurabh import hand

class game:
	def __init__(self):
		self.deck = deck()
		self.deck.shuffle()

nos = int(raw_input("Enter Number of Players:"))
g1 = game()
h = [0]*(nos)
print h
for i in range(0,nos):
	st = "p"+str(i+1)
	print st
        h[i] = hand(st)

g1.deck.deal(h, 1)

for i in range(0, nos):
	print h[i]

for i in range(0, nos):
	if i==0:
		high = h[i].cards[0]
	else:
		if high < h[i].cards[0]:
			high = h[i].cards[0]

print high
