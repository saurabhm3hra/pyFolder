class card:
	colors = ["Club","Diamond","Heart","Spade"]
	numbers = ["none","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
	
	def __init__(self,color,number):
		self.color = color
		self.number = number
	
	def __str__(self):
		return self.numbers[self.number] + " of " + self.colors[self.color]
	
	def __cmp__(self,c2):
		if(self.number == c2.number):
			if(self.color > c2.color):
				return 1
			elif(self.color == c2.color):
				return 0
			else:
				return -1
		elif(self.number == 1 or c2.number == 1):
			if(self.number == 1):
				return 1
			else:
				return -1
		elif(self.number > c2.number):
			return 1
		else:
			return -1
class deck:
	cards = []
	def __init__(self):
		for suit in range(0,4):
			for rank in range(1,14):
				c = card(suit,rank)
				self.cards.append(c)
	
	def __str__(self):
		s = ""
		for i in range(0,len(self.cards)):
			s = s + str(i+1) + ". " + str(self.cards[i]) + "\n"
		return s
	
	def shuffle(self):
		import random
		for i in range(0,len(self.cards)):
			j = random.randrange(i,len(self.cards))
			self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

	def pickcard(self):
		return self.cards.pop()
	
	def deal(self,hands,n=0):
		h=0
		if n==0:
			while True:
				if(not self.cards):
					break
				else:
					if(h==len(hands)):
						h=0
					else:
						hands[h].addcard(self)
						h=h+1
		else:
			i=1
			while i <= n*(len(hands)+1):
                                if(not self.cards):
                                        break
                                else:
                                        if(h==len(hands)):
                                                h=0
						i=i+1
                                        else:
                                                hands[h].addcard(self)
                                                h=h+1
						i=i+1

class hand(deck):
	pass
	cards = []
	name = ""
	
	def __init__(self, name=""):
		self.cards = []
		self.name = name

	def addcard(self,deck):
		self.cards.append(deck.pickcard())
	
