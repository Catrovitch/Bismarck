from email.errors import FirstHeaderLineIsContinuationDefect
import unittest
from createdeck import CreateDeck
from gameboard import GameBoard
from gamelogic import GameLogic
from card import Card

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        pass

    def test_stage_card_two_different_false(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.gameboard.initial_deal()  

        first = gamelogic.stage_card(1, 2)
        second = gamelogic.stage_card(1, 2)

        self.assertEqual((first, second), (True, False))

        pass

    def test_gamelogic_gameboard(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
    

        self.assertEqual(type(gamelogic.gameboard), type(gameboard))


    def test_initial_deal(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.initial_deal()

        p1h = len(gamelogic.gameboard.player1_hand)
        p1f = len(gamelogic.gameboard.player1_final)
        p2h = len(gamelogic.gameboard.player2_hand)
        p2f = len(gamelogic.gameboard.player2_final)

        self.assertEqual((p1h,p1f, p2h, p2f), (6, 3, 6, 3))

    def test_stage_card_normal(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.gameboard.initial_deal()  

        p1 = gamelogic.stage_card(1, 0)
        p2 = gamelogic.stage_card(2, 0)

        self.assertEqual((p1, p2), (True, True))

    def test_stage_card_two_different_false(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.gameboard.initial_deal()  

        p1first = gamelogic.stage_card(1, 0)
        p1second = gamelogic.stage_card(1, 0)
        p2first = gamelogic.stage_card(2, 0)
        p2second = gamelogic.stage_card(2, 0)

        self.assertEqual((p1first, p2second, p2first, p2second), (True, False, True, False))

    def test_stage_card_two_same(self):
        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card1 = Card("hearts", 2)
        card2 = Card("clubs", 2)
        card3 = Card("spades", 2)
        card4 = Card("diamonds", 2)
        
        gamelogic.gameboard.player1_hand.append(card1)
        gamelogic.gameboard.player1_hand.append(card2)
        gamelogic.gameboard.player2_hand.append(card3)
        gamelogic.gameboard.player2_hand.append(card4)
        

        gamelogic.stage_card(1, 0)
        gamelogic.stage_card(1, 0)
        gamelogic.stage_card(2, 0)
        gamelogic.stage_card(2, 0)

        p1 = len(gamelogic.gameboard.player1_staged)
        p2 = len(gamelogic.gameboard.player2_staged)

        self.assertEqual((p1,p2), (2,2))