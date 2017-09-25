class Card:
    """Playing Cards"""

    names = ['Clubs','Diamonds','Hearts','Spades']
    ranks = ['None','Ace','1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return '%s of %s' %(Card.ranks[self.rank], Card.names[self.suit])


    def __lt__(self, other):
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        return self.rank < other.rank

class Deck:
    """whole deck"""

    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(14):
                card=Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for cards in self.cards:
            res.append(str(cards))
        return '\n'.join(res)

queen_diamond = Card(1,12)
print(queen_diamond)
deck=Deck()
print(deck)
