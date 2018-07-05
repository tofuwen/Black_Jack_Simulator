from unittest import TestCase
from Board import Board


class TestBoard(TestCase):

    def test_create_board(self):
        board = Board(4)
        self.assertTrue(board.count() == 52 * 4)

    def test_random_draw(self):
        board = Board(4)
        board.random_draw()
        self.assertTrue(board.count() == 52 * 4 - 1)