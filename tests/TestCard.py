from unittest import TestCase
from Card import Card


class TestCard(TestCase):

    def test_create_card_by_id(self):
        cards = [Card(id=0), Card(id=23), Card(id=34), Card(id=51)]
        ids = [0, 23, 34, 51]
        suits = ['C', 'D', 'H', 'S']
        numbers = [2, 12, 10, 14]
        for i, card in enumerate(cards):
            self.assertTrue(card.id == ids[i])
            self.assertTrue(card.suit == suits[i])
            self.assertTrue(card.number == numbers[i])

    def test_create_card_by_suit_and_number(self):
        cards = [Card(suit='C', number=2), Card(suit='D', number=12),
                 Card(suit='H', number=10), Card(suit='S', number=14)]
        ids = [0, 23, 34, 51]
        suits = ['C', 'D', 'H', 'S']
        numbers = [2, 12, 10, 14]
        for i, card in enumerate(cards):
            self.assertTrue(card.id == ids[i])
            self.assertTrue(card.suit == suits[i])
            self.assertTrue(card.number == numbers[i])

    def test_get_score(self):
        cards = [Card(suit='C', number=2), Card(suit='D', number=12),
                 Card(suit='H', number=10), Card(suit='S', number=14)]
        scores = [[2], [10], [10], [1, 11]]
        for i, card in enumerate(cards):
            self.assertTrue(card.get_score() == scores[i])