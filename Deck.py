import Card
import random


class Deck(object):

    """Represent a standard 52-card deck (without jokers)

    Attributes:
        cards: cards remaining in the deck after playing several rounds (originally 52 cards)
    """
    NUM_CARD_IN_SUIT = 13
    NUM_SUIT = 4

    def __init__(self):
        Deck.NUM_CARD_IN_SUIT = 13
        Deck.NUM_SUIT = 4
        self.cards = {Card(i) for i in range(Deck.NUM_CARD_IN_SUIT * Deck.NUM_SUIT)}

    def count(self):
        return len(self.cards)

    def remove_card(self, card):
        self.cards.remove(card)

    def random_draw(self):
        drawn_card = random.choice(self.cards)
        self.remove_card(drawn_card)
        return drawn_card