from Deck import Deck
import random


class Board(object):

    """Represent a board, which can contain multiple decks

    Attributes:
        decks: decks remaining in the board after playing several rounds
    """

    def __init__(self, num_deck):
        self.num_deck = num_deck
        self.decks = [Deck() for i in range(num_deck)]

    def count(self):
        return sum([deck.count() for deck in self.decks])

    def random_draw(self):
        [deck_index] = random.choices(range(0, self.num_deck), weights=[deck.count() for deck in self.decks])
        drawn_card = self.decks[deck_index].random_draw()
        return drawn_card
