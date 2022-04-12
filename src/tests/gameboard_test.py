import unittest
from services.gameboard import GameBoard
from services.createdeck import CreateDeck


class TestGameBoard(unittest.TestCase):

    def setUp(self):

        pass

    def test_reserve_deck_length(self):
        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)

        length = len(gameboard.reserve_deck)

        self.assertEqual(length, 54)


