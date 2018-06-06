from Deck import *


class Card(object):

    """Represent a single card drawn from a 52-card deck (without jokers)

    Attributes:
        suit: Spade, Heart, Diamond, Club
        number: 2 to 10, J = 11, Q = 12, K = 13, A = 14
        id: C2 = 0, C3 = 1, ... SA = 51
    """

    def __init__(self, id=None, suit='C', number=2):
        suit_dict = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
        inv_suit_dict = {v: k for k, v in suit_dict.items()}
        if id:
            self.id = id
            self.suit = inv_suit_dict[id // Deck.NUM_CARD_IN_SUIT]
            self.number = id - id // Deck.NUM_CARD_IN_SUIT * Deck.NUM_CARD_IN_SUIT + 2
            assert (0 <= self.id < Deck.NUM_CARD_IN_SUIT * Deck.NUM_SUIT)
            assert (2 <= self.number <= 14)
        else:
            self.suit = suit
            self.number = number
            self.id = suit_dict[suit] * Deck.NUM_CARD_IN_SUIT + self.number - 2
            assert (0 <= self.id < Deck.NUM_CARD_IN_SUIT * Deck.NUM_SUIT)
            assert (2 <= self.number <= 14)