from collections import namedtuple
import random
from typing import List

Card = namedtuple('card', 'rank suit')
beer_card = Card('7', 'diamonds')
ranked, suited = beer_card
print(beer_card.rank)
print(beer_card.suit)

# suits et ranks
SUITS = "clubs diamonds spades hearts".split()
RANKS = [str(n) for n in range(2,11)] + list('JQKA')
CARDS = [Card(r,s) for s in SUITS for r in RANKS]


# deck class  --> Créer une séquence - surcharge __len__ et __gztitem__
class Deck:
    def __init__(self):
        self._cards = list(CARDS)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

deck = Deck()
len(deck)
print(deck[0])
print(deck[:5])
sorted(deck)
myChoice = random.choice(deck)
print("mon choix :"+ str(myChoice))




