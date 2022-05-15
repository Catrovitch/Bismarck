import unittest
from services.createdeck import CreateDeck
from services.card import Card
from services.bismarck_ai import BismarckAI
from services.gameboard import GameBoard
from services.gamelogic import GameLogic
from services.player import Player
from ui.endgame import PlayerEndgame
from ui.finalcards import PlayerFinal


class TestBismarckAI(unittest.TestCase):

    def setUp(self):

        self.deck = CreateDeck()
        self.deck = self.deck.export()
        self.gameboard = GameBoard(self.deck)
        self.gamelogic = GameLogic(self.gameboard)
        self.player = Player(-1, self.gamelogic)
        
        self.hand = self.gameboard.player2_hand
        self.staged = self.gameboard.player2_staged
        self.endgame = self.gameboard.player2_endgame
        self.final = self.gameboard.player2_final

        self.bismarck_endgame = PlayerEndgame()
        self.bismarck_final = PlayerFinal()

        self.bismarck_ai = BismarckAI(self.gamelogic, self.bismarck_endgame, self.bismarck_final, self.player)

    def test_choose_endgame_cards_normal(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 11), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in card_list:
            self.hand.append(card)
        
        self.bismarck_ai.choose_endgame_cards()

        normal = [11, 12, 13]

        chose_correct = True

   
        for card in self.endgame:
            if card.number in (normal):
                continue
            else:
                chose_correct = False

            
        
        self.assertEqual(chose_correct, True)

    def test_choose_endgame_cards_special(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 10), Card("hearts", 14)]

        for card in card_list:
            self.hand.append(card)
        
        self.bismarck_ai.choose_endgame_cards()

        special = [2, 10, 14]

        chose_correct = True

   
        for card in self.endgame:
            if card.number in (special):
                continue
            else:
                chose_correct = False

            
        
        self.assertEqual(chose_correct, True)

    def test_choose_least_valuable_card_normal(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 11), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]
        deck = []

        for card in card_list:
            deck.append(card)

        top_card = Card("hearts", 6)

        chosen_card = self.bismarck_ai.choose_least_valuable_card(deck, top_card.number)

        self.assertEqual(chosen_card.number, 7)

    def test_choose_least_valuable_card_special(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 10), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]
        deck = []

        for card in card_list:
            deck.append(card)

        top_card = Card("hearts", 14)

        chosen_card = self.bismarck_ai.choose_least_valuable_card(deck, top_card.number)

        self.assertEqual(chosen_card.number, 10)


    def test_choose_least_valuable_card_none(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 4), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]
        deck = []

        for card in card_list:
            deck.append(card)

        top_card = Card("hearts", 14)

        chosen_card = self.bismarck_ai.choose_least_valuable_card(deck, top_card.number)

        self.assertEqual(chosen_card, False)

    def test_bismarck_chance(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 4), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in card_list:
            self.gameboard.reserve_deck.append(card)

        top_card = Card("hearts", 11)

        self.gameboard.field_deck.append(top_card)

        self.assertEqual(self.bismarck_ai.chance(), None)

    def test_play_from_hand_no_card_available(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 4), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in card_list:
            self.hand.append(card)

        top_card = Card("hearts", 14)

        chosen_card = self.bismarck_ai.play_from_hand(top_card.number)

        self.assertEqual(chosen_card, False)        

    def test_play_from_hand_normal(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 4), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in card_list:
            self.hand.append(card)

        top_card = Card("hearts", 6)

        chosen_card = self.bismarck_ai.play_from_hand(top_card.number)

        self.assertEqual(chosen_card, True)   

    def test_play_from_hand_special(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in card_list:
            self.hand.append(card)

        top_card = Card("hearts", 14)

        chosen_card = self.bismarck_ai.play_from_hand(top_card.number)

        self.assertEqual(chosen_card, True)   

    def test_play_from_endgame_no_card_available(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 4)]


        for card in card_list:
            self.endgame.append(card)

        top_card = Card("hearts", 14)

        chosen_card = self.bismarck_ai.play_from_endgame(top_card.number)

        self.assertEqual(chosen_card, False)        

    def test_play_from_endgame_normal(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 4)]

        for card in card_list:
            self.endgame.append(card)

        top_card = Card("hearts", 6)

        chosen_card = self.bismarck_ai.play_from_endgame(top_card.number)

        self.assertEqual(chosen_card, True)   

    def test_play_from_endgame_special(self):

        card_list = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2)]

        for card in card_list:
            self.endgame.append(card)

        top_card = Card("hearts", 14)

        chosen_card = self.bismarck_ai.play_from_endgame(top_card.number)

        self.assertEqual(chosen_card, True)   

    def test_choose_played_cards_on_off_turn(self):

        self.gamelogic.turn = 1

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_hand_succsesful(self):

        self.gamelogic.turn = -1
        
        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)
        
        card_list = [Card("clubs", 5), Card("spades", 7), Card("diamonds", 2), Card("clubs", 3), Card("spades", 12), Card("hearts", 10)]

        for card in card_list:
            self.hand.append(card)

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_hand_fail(self):

        self.gamelogic.turn = -1
        
        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)
        
        card_list = [Card("clubs", 5), Card("spades", 7), Card("diamonds", 4), Card("clubs", 3), Card("spades", 12), Card("hearts", 3)]

        for card in card_list:
            self.hand.append(card)

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_chance_succsess(self):

        self.gamelogic.turn = -1

        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)

        card_list = [Card("clubs", 5), Card("spades", 7), Card("diamonds", 2), Card("clubs", 3), Card("spades", 12), Card("hearts", 10)]
        for card in card_list:
            self.gameboard.reserve_deck.append(card)

        self.gameboard.player2_hand = []

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_chance_fails(self):

        self.gamelogic.turn = -1

        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)


        self.gameboard.reserve_deck = []
        self.gameboard.player2_hand = []

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_endgame_successful(self):

        self.gamelogic.turn = -1

        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)

        card_list = [Card("clubs", 5), Card("spades", 14), Card("diamonds", 2)]

        for card in card_list:
            self.endgame.append(card)

        self.gameboard.player2_hand = []
        self.gameboard.reserve_deck = []

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_endgame_fails(self):

        self.gamelogic.turn = -1

        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)

        card_list = [Card("clubs", 5), Card("spades", 7), Card("diamonds", 4)]

        for card in card_list:
            self.endgame.append(card)

        self.gameboard.player2_hand = []
        self.gameboard.reserve_deck = []

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_final(self):

        self.gamelogic.turn = -1
        
        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)

        card_list = [Card("clubs", 5), Card("spades", 7), Card("diamonds", 2)]

        for card in card_list:
            self.final.append(card)

        self.gameboard.player2_hand = []
        self.gameboard.reserve_deck = []

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_no_cards_left(self):

        self.gamelogic.turn = -1
        
        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)
        
        self.gameboard.player2_hand = []
        self.gameboard.player2_endgame = []
        self.gameboard.player1_final = []
        self.gameboard.reserve_deck = []

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)

    def test_choose_played_cards_no_card_to_play(self):

        self.gamelogic.turn = -1
        
        deck = [Card("hearts", 5), Card("hearts", 7), Card("hearts", 2), Card("hearts", 3), Card("hearts", 12), Card("hearts", 13)]

        for card in deck:
            self.gameboard.field_deck.append(card)
        
        card_list = [Card("clubs", 5), Card("spades", 7), Card("diamonds", 4), Card("clubs", 3), Card("spades", 12), Card("hearts", 3)]

        for card in card_list:
            self.hand.append(card)

        self.gameboard.reserve_deck = []

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)


    def test_choose_played_cards_field_deck_is_empty(self):

        self.gamelogic.turn = -1

        self.gameboard.field_deck = []

        card_list = [Card("clubs", 5), Card("spades", 7), Card("diamonds", 4), Card("clubs", 3), Card("spades", 12), Card("hearts", 3)]

        for card in card_list:
            self.hand.append(card)

        self.bismarck_ai.choose_played_cards()

        self.assertEqual(self.bismarck_ai.choose_played_cards(), None)