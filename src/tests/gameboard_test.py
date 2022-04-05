import unittest
from gameboard import GameBoard
from createdeck import CreateDeck

class TestGameBoard(unittest.TestCase):

    def setUp(self):

        pass

    def test_reserve_deck_length(self):
        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)

        length = len(gameboard.reserve_deck)

        self.assertEqual(length, 54)

    def test_initial_deal(self):
        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)

        gameboard.initial_deal()

        player1_hand = len(gameboard.player1_hand)
        player2_hand = len(gameboard.player2_hand)

        self.assertEqual((player1_hand, player2_hand), (6,6))
