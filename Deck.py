from Card import Card
from Constants import Constants
import random


class Deck(object):

    """Represent a standard 52-card deck (without jokers)

    Attributes:
        cards: cards remaining in the deck after playing several rounds (originally 52 cards)
    """

    def __init__(self):
        self.cards = {Card(id=i) for i in range(Constants().NUM_CARD_IN_SUIT * Constants().NUM_SUIT)}

    def count(self):
        return len(self.cards)

    def remove_card(self, card):
        assert (card in self.cards)
        self.cards.remove(card)

    def random_draw(self):
        drawn_card = random.choice(self.cards)
        self.remove_card(drawn_card)
        return drawn_card
