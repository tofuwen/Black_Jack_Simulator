from unittest import TestCase
from Deck import *
from Card import *


class TestDeck(TestCase):

    def test_create_deck(self):
        deck = Deck()
        self.assertTrue(deck.count() == 52)

    def test_remove_card(self):
        deck = Deck()
        deck.remove_card(Card(id=0))
        self.assertTrue(deck.count() == 51)
        deck.remove_card(Card(id=1))
        self.assertTrue(deck.count() == 50)
        with self.assertRaises(AssertionError):
            deck.remove_card(Card(id=1))