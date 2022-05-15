import unittest
from services.player import Player
from services.createdeck import CreateDeck
from services.gameboard import GameBoard
from services.gamelogic import GameLogic
from services.card import Card


class TestPlayer(unittest.TestCase):

    def setUp(self):

        pass

    def test_player_id(self):
        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        player = Player(1, gamelogic)

        self.assertEqual(player.player_id, 1)

    def test_player_gamelogic_class(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        player = Player(1, gamelogic)

        what_type = type(player.gamelogic)

        self.assertEqual(what_type, type(GameLogic(gameboard)))

    def test_player_stage_card_from_hand(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card = Card("hearts", 2)

        player = Player(1, gamelogic)

        gamelogic.player1_locked = False

        gameboard.player1_hand.append(card)

        player.stage_card_from_hand(card)

        staged_card = gameboard.player1_staged[0]

        self.assertEqual(staged_card, card)

    def test_player_stage_card_from_endgame(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card = Card("hearts", 2)

        player = Player(1, gamelogic)

        gamelogic.player1_locked = False

        gameboard.player1_endgame.append(card)

        player.stage_card_from_endgame(card)

        staged_card = gameboard.player1_staged[0]

        self.assertEqual(staged_card, card)

    def test_player_staged_cards(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card = Card("hearts", 2)

        player = Player(1, gamelogic)

        gamelogic.player1_locked = False

        gameboard.player1_endgame.append(card)

        player.stage_card_from_endgame(card)

        player.play_staged_cards()

        self.assertEqual(gameboard.field_deck[-1], card)

    def test_pick_up_field_deck(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card = Card("hearts", 2)

        player = Player(1, gamelogic)

        gameboard.field_deck.append(card)

        player.pick_up_field_deck()

        self.assertEqual(gameboard.player1_hand[0], card)

    def test_chance(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        player = Player(1, gamelogic)

        gamelogic.player1_locked = False

        card = gameboard.reserve_deck[-1]

        player.chance()

        self.assertEqual(gameboard.field_deck[0], card)

    def test_play_final_card(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        player = Player(1, gamelogic)

        gamelogic.player1_locked = False

        card = Card("hearts", 2)

        gameboard.player1_final.append(card)

        player.play_finalcard()

        self.assertEqual(gameboard.field_deck[-1], card)

    def test_choose_endgame_cards(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        player = Player(1, gamelogic)

        gamelogic.player1_locked = False

        card = Card("hearts", 2)

        gameboard.player1_hand.append(card)

        player.choose_endgame_cards(card)

        self.assertEqual(gameboard.player1_endgame[-1], card)

    def test_sort_hand(self):

        deck = CreateDeck().export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        player = Player(1, gamelogic)

        gamelogic.player1_locked = False

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 13)
        card3 = Card("hearts", 7)
        card4 = Card("hearts", 5)

        gameboard.player1_hand.append(card1)
        gameboard.player1_hand.append(card2)
        gameboard.player1_hand.append(card3)
        gameboard.player1_hand.append(card4)

        player.sort_hand()

        self.assertEqual((gameboard.player1_hand[0].number, gameboard.player1_hand[-1].number), (2, 13))