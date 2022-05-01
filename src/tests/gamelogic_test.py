import unittest
from services.createdeck import CreateDeck
from services.gameboard import GameBoard
from services.gamelogic import GameLogic
from services.card import Card


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        pass

    def test_gamelogic_gameboard(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        self.assertEqual(type(gamelogic.gameboard), type(gameboard))

    def test_initial_deal_amount_of_cards(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.initial_deal()

        player1h = len(gamelogic.gameboard.player1_hand)
        player1f = len(gamelogic.gameboard.player1_final)
        player2h = len(gamelogic.gameboard.player2_hand)
        player2f = len(gamelogic.gameboard.player2_final)

        self.assertEqual(
            (player1h, player1f, player2h, player2f), (6, 3, 6, 3))

    def test_decide_turn_in_beginning_player1_starts(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 4)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 7)
        card6 = Card("spades", 8)
        card7 = Card("hearts", 9)
        card8 = Card("hearts", 10)
        card9 = Card("spades", 11)
        card10 = Card("hearts", 12)
        card11 = Card("hearts", 13)
        card12 = Card("spades", 14)

        gamelogic.gameboard.player1_hand = [
            card1, card2, card3, card4, card5, card6]
        gamelogic.gameboard.player2_hand = [
            card7, card8, card9, card10, card11, card12]

        gamelogic.decide_turn_in_beginning()

        self.assertEqual(gamelogic.turn, 1)

    def test_decide_turn_in_beginning_player1_locked_is_false(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 4)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 7)
        card6 = Card("spades", 8)
        card7 = Card("hearts", 9)
        card8 = Card("hearts", 10)
        card9 = Card("spades", 11)
        card10 = Card("hearts", 12)
        card11 = Card("hearts", 13)
        card12 = Card("spades", 14)

        gamelogic.gameboard.player1_hand = [
            card1, card2, card3, card4, card5, card6]
        gamelogic.gameboard.player2_hand = [
            card7, card8, card9, card10, card11, card12]

        gamelogic.decide_turn_in_beginning()

        self.assertEqual(gamelogic.player1_locked, False)

    def test_decide_turn_in_beginning_player2_starts(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 4)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 7)
        card6 = Card("spades", 8)
        card7 = Card("hearts", 9)
        card8 = Card("hearts", 10)
        card9 = Card("spades", 11)
        card10 = Card("hearts", 12)
        card11 = Card("hearts", 13)
        card12 = Card("spades", 14)

        gamelogic.gameboard.player2_hand = [
            card1, card2, card3, card4, card5, card6]
        gamelogic.gameboard.player1_hand = [
            card7, card8, card9, card10, card11, card12]

        gamelogic.decide_turn_in_beginning()

        self.assertEqual(gamelogic.turn, -1)

    def test_decide_turn_in_beginning_player2_locked_is_false(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 4)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 7)
        card6 = Card("spades", 8)
        card7 = Card("hearts", 9)
        card8 = Card("hearts", 10)
        card9 = Card("spades", 11)
        card10 = Card("hearts", 12)
        card11 = Card("hearts", 13)
        card12 = Card("spades", 14)

        gamelogic.gameboard.player2_hand = [
            card1, card2, card3, card4, card5, card6]
        gamelogic.gameboard.player1_hand = [
            card7, card8, card9, card10, card11, card12]

        gamelogic.decide_turn_in_beginning()

        self.assertEqual(gamelogic.player2_locked, False)

    def test_choose_endgame_cards_normal_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.initial_deal()

        for i in range(3):
            card = gameboard.player1_hand[-1]
            result = gamelogic.choose_endgame_cards(1, card)

        self.assertEqual(result, True)

    def test_choose_endgame_cards_normal_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.initial_deal()

        for i in range(3):
            card = gameboard.player2_hand[-1]
            result = gamelogic.choose_endgame_cards(-1, card)

        self.assertEqual(result, True)

    def test_choose_endgame_cards_too_many(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.initial_deal()

        for i in range(4):
            card = gameboard.player1_hand[-1]
            result = gamelogic.choose_endgame_cards(1, card)

        self.assertEqual(result, False)

    def test_stage_card_from_hand(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 4)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 7)
        card6 = Card("spades", 8)
        card7 = Card("hearts", 9)
        card8 = Card("hearts", 10)
        card9 = Card("spades", 11)
        card10 = Card("hearts", 12)
        card11 = Card("hearts", 13)
        card12 = Card("spades", 14)

        gamelogic.gameboard.player1_hand = [
            card1, card2, card3, card4, card5, card6]
        gamelogic.gameboard.player2_hand = [
            card7, card8, card9, card10, card11, card12]

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        player1 = gamelogic.stage_card_from_hand(
            1, gamelogic.gameboard.player1_hand[0])

        gamelogic.player2_locked = False

        player2 = gamelogic.stage_card_from_hand(
            -1, gamelogic.gameboard.player2_hand[0])

        self.assertEqual((player1, player2), (True, True))

    def test_stage_card_from_hand_player1_is_locked(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 4)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 7)
        card6 = Card("spades", 8)
        card7 = Card("hearts", 9)
        card8 = Card("hearts", 10)
        card9 = Card("spades", 11)
        card10 = Card("hearts", 12)
        card11 = Card("hearts", 13)
        card12 = Card("spades", 14)

        gamelogic.gameboard.player2_hand = [
            card1, card2, card3, card4, card5, card6]
        gamelogic.gameboard.player1_hand = [
            card7, card8, card9, card10, card11, card12]

        gamelogic.decide_turn_in_beginning()

        player1 = gamelogic.stage_card_from_hand(
            1, gamelogic.gameboard.player1_hand[0])

        self.assertEqual(player1, False)

    def test_stage_card_from_hand_player2_is_locked(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("hearts", 4)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 7)
        card6 = Card("spades", 8)
        card7 = Card("hearts", 9)
        card8 = Card("hearts", 10)
        card9 = Card("spades", 11)
        card10 = Card("hearts", 12)
        card11 = Card("hearts", 13)
        card12 = Card("spades", 14)

        gamelogic.gameboard.player1_hand = [
            card1, card2, card3, card4, card5, card6]
        gamelogic.gameboard.player2_hand = [
            card7, card8, card9, card10, card11, card12]

        gamelogic.decide_turn_in_beginning()

        player2 = gamelogic.stage_card_from_hand(
            -1, gamelogic.gameboard.player2_hand[0])

        self.assertEqual(player2, False)

    def test_stage_card_normal_joker_as_first_card(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        joker = Card("red-joker", 0)
        other_card = Card("hearts", 2)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gameboard.player1_hand.append(joker)
        gameboard.player1_hand.append(other_card)

        gamelogic.stage_card_from_hand(1, joker)
        player = gamelogic.stage_card_from_hand(1, other_card)

        self.assertEqual(player, True)

    def test_stage_card_two_different_false(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("clubs", 3)
        card3 = Card("spades", 4)
        card4 = Card("diamonds", 5)

        gamelogic.player1_locked = False
        gamelogic.player2_locked = False

        gamelogic.gameboard.player1_hand.append(card1)
        gamelogic.gameboard.player1_hand.append(card2)
        gamelogic.gameboard.player2_hand.append(card3)
        gamelogic.gameboard.player2_hand.append(card4)

        p1first = gamelogic.stage_card_from_hand(
            1, gamelogic.gameboard.player1_hand[0])
        p1second = gamelogic.stage_card_from_hand(
            1, gamelogic.gameboard.player1_hand[0])
        p2first = gamelogic.stage_card_from_hand(
            -1, gamelogic.gameboard.player2_hand[0])
        p2second = gamelogic.stage_card_from_hand(
            -1, gamelogic.gameboard.player2_hand[0])

        self.assertEqual((p1first, p1second, p2first, p2second),
                         (True, False, True, False))

    def test_stage_card_two_same(self):
        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card1 = Card("hearts", 2)
        card2 = Card("clubs", 2)
        card3 = Card("spades", 2)
        card4 = Card("diamonds", 2)

        gamelogic.player1_locked = False
        gamelogic.player2_locked = False

        gamelogic.gameboard.player1_hand.append(card1)
        gamelogic.gameboard.player1_hand.append(card2)
        gamelogic.gameboard.player2_hand.append(card3)
        gamelogic.gameboard.player2_hand.append(card4)

        gamelogic.stage_card_from_hand(1, gamelogic.gameboard.player1_hand[0])
        gamelogic.stage_card_from_hand(1, gamelogic.gameboard.player1_hand[0])
        gamelogic.stage_card_from_hand(-1, gamelogic.gameboard.player2_hand[0])
        gamelogic.stage_card_from_hand(-1, gamelogic.gameboard.player2_hand[0])

        player1 = len(gamelogic.gameboard.player1_staged)
        player2 = len(gamelogic.gameboard.player2_staged)

        self.assertEqual((player1, player2), (2, 2))

    def test_stage_card_from_endgame_normal(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 3)
        card2 = Card("spades", 3)

        gamelogic.player1_locked = False
        gamelogic.player2_locked = False

        gamelogic.gameboard.player1_endgame.append(card1)
        gamelogic.gameboard.player2_endgame.append(card2)

        player1 = gamelogic.stage_card_from_endgame(
            1, gamelogic.gameboard.player1_endgame[0])
        player2 = gamelogic.stage_card_from_endgame(
            -1, gamelogic.gameboard.player2_endgame[0])

        self.assertEqual((player1, player2), (True, True))

    def test_stage_card_from_endgame_normal_two_same(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 3)
        card2 = Card("spades", 3)

        gamelogic.player1_locked = False
        gamelogic.player2_locked = False

        gamelogic.gameboard.player1_endgame.append(card1)
        gamelogic.gameboard.player1_endgame.append(card2)

        player1 = gamelogic.stage_card_from_endgame(
            1, gamelogic.gameboard.player1_endgame[0])
        player2 = gamelogic.stage_card_from_endgame(
            1, gamelogic.gameboard.player1_endgame[0])

        self.assertEqual((player1, player2), (True, True))

    def test_stage_card_from_endgame_two_different_false(self):
        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 3)
        card2 = Card("hearts", 4)
        card3 = Card("hearts", 5)
        card4 = Card("hearts", 6)

        gamelogic.player1_locked = False
        gamelogic.player2_locked = False

        gamelogic.gameboard.player1_endgame = [card1, card2]
        gamelogic.gameboard.player2_endgame = [card3, card4]

        p1first = gamelogic.stage_card_from_endgame(
            1, gamelogic.gameboard.player1_endgame[0])
        p1second = gamelogic.stage_card_from_endgame(
            1, gamelogic.gameboard.player1_endgame[0])
        p2first = gamelogic.stage_card_from_endgame(
            -1, gamelogic.gameboard.player2_endgame[0])
        p2second = gamelogic.stage_card_from_endgame(
            -1, gamelogic.gameboard.player2_endgame[0])

        self.assertEqual((p1first, p1second, p2first, p2second),
                         (True, False, True, False))

    def test_play_staged_cards_field_deck_length_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card(2, "hearts")
        card2 = Card(2, "spades")

        gamelogic.player1_locked = False

        gamelogic.gameboard.player1_staged.append(card1)
        gamelogic.gameboard.player1_staged.append(card2)

        gamelogic.play_staged_cards(1)

        field_deck_length = len(gamelogic.gameboard.field_deck)

        self.assertEqual(field_deck_length, 2)

    def test_play_staged_cards_field_deck_length_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card(2, "hearts")
        card2 = Card(2, "spades")

        gamelogic.player2_locked = False

        gamelogic.gameboard.player2_staged.append(card1)
        gamelogic.gameboard.player2_staged.append(card2)

        gamelogic.play_staged_cards(-1)

        field_deck_length = len(gamelogic.gameboard.field_deck)

        self.assertEqual(field_deck_length, 2)

    def test_play_staged_cards_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card(2, "hearts")
        card2 = Card(2, "spades")
        card3 = Card(4, "hearts")
        card4 = Card(6, "spades")

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card3)
        gamelogic.gameboard.field_deck.append(card4)
        gamelogic.gameboard.player2_staged.append(card1)
        gamelogic.gameboard.player2_staged.append(card2)

        result = gamelogic.play_staged_cards(-1)

        self.assertEqual(result, True)

    def test_play_when_nothing_is_staged_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.player1_locked = False

        result = gamelogic.play_staged_cards(1)

        self.assertEqual(result, False)

    def test_play_when_nothing_is_staged_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.player2_locked = False

        result = gamelogic.play_staged_cards(-1)

        self.assertEqual(result, False)

    def test_play_joker_gets_inserted_singular(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("spades", 3)
        card3 = Card("red-joker", 0)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        gamelogic.gameboard.player1_staged.append(card3)

        gamelogic.play_staged_cards(1)

        joker = gameboard.field_deck[-2].number

        self.assertEqual(joker, 0)

    def test_play_joker_gets_inserted_two_jokers(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 2)
        card2 = Card("spades", 3)
        card3 = Card("red-joker", 0)
        card4 = Card("black-joker", 0)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        gamelogic.gameboard.player1_staged.append(card3)
        gamelogic.gameboard.player1_staged.append(card4)

        gamelogic.play_staged_cards(1)

        joker1 = gameboard.field_deck[-2].number
        joker2 = gameboard.field_deck[-3].number

        self.assertEqual((joker1, joker2), (0, 0))

    def test_check_card_hierarchy_card_was_played_on_turn_and_succeeds_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 3)
        card2 = Card("hearts", 4)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_card_was_played_on_turn_and_succeeds_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 3)
        card2 = Card("hearts", 4)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(-1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_card_was_played_on_turn_and_fails_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, False)

    def test_check_card_hierarchy_card_was_played_on_turn_and_fails_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(-1, 1)

        self.assertEqual(result, False)

    def test_check_card_hierarchy_card_was_played_off_turn_and_fails_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 5)

        gamelogic.turn = -1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.player1_last_played = card1
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, False)

    def test_check_card_hierarchy_card_was_played_off_turn_and_fails_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 5)

        gamelogic.turn = 1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.player2_last_played = card1
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(-1, 1)

        self.assertEqual(result, False)

    def test_check_card_hierarchy_more_than_one_card_was_played(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 5)
        card3 = Card("spades", 5)
        card4 = Card("clubs", 5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)
        gamelogic.gameboard.field_deck.append(card3)
        gamelogic.gameboard.field_deck.append(card4)

        result = gamelogic.check_card_hierarchy(1, 3)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_field_was_empty(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_two_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 2)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_two_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 2)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(-1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_ten_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 10)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_ten_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 10)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(-1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_ten_empties_field_to_trash(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 10)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        gamelogic.check_card_hierarchy(1, 1)

        field_length = len(gamelogic.gameboard.field_deck)
        trash_length = len(gamelogic.gameboard.trash_deck)

        self.assertEqual((field_length, trash_length), (0, 2))

    def test_check_card_hierarchy_ten_on_emtpy_field_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 10)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_ten_on_emtpy_field_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 10)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card1)

        result = gamelogic.check_card_hierarchy(-1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_four_of_same_result_is_true(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("spades", 6)
        card3 = Card("clubs", 6)
        card4 = Card("diamonds", 6)
        card5 = Card("hearts", 6)

        gameboard.field_deck.append(card1)
        gameboard.field_deck.append(card2)
        gameboard.field_deck.append(card3)
        gameboard.field_deck.append(card4)
        gameboard.field_deck.append(card5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.check_card_hierarchy(1, 1)

        field_length = len(gameboard.field_deck)
        trash_length = len(gameboard.trash_deck)

        self.assertEqual((field_length, trash_length), (0, 5))

    def test_check_card_hierarchy_four_of_same_result_joker_in_the_mix_is_true(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("spades", 6)
        card3 = Card("red-joker", 0)
        card4 = Card("diamonds", 6)
        card5 = Card("hearts", 6)

        gameboard.field_deck.append(card1)
        gameboard.field_deck.append(card2)
        gameboard.field_deck.append(card3)
        gameboard.field_deck.append(card4)
        gameboard.field_deck.append(card5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.check_card_hierarchy(1, 1)

        field_length = len(gameboard.field_deck)
        trash_length = len(gameboard.trash_deck)

        self.assertEqual((field_length, trash_length), (0, 5))

    def test_check_card_hierarchy_four_of_same_trashes(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 6)
        card3 = Card("hearts", 6)
        card4 = Card("hearts", 6)
        card5 = Card("hearts", 6)

        gameboard.field_deck.append(card1)
        gameboard.field_deck.append(card2)
        gameboard.field_deck.append(card3)
        gameboard.field_deck.append(card4)
        gameboard.field_deck.append(card5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_hierarchy_on_off_turn_succeeds_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 5)
        card2 = Card("spades", 5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.player1_hand.append(card1)
        gamelogic.gameboard.player1_hand.append(card2)
        gamelogic.stage_card_from_hand(1, card1)
        gamelogic.play_staged_cards(1)

        gamelogic.stage_card_from_hand(1, card2)
        result = gamelogic.play_staged_cards(1)

        self.assertEqual(result, True)

    def test_check_hierarchy_on_off_turn_succeeds_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 5)
        card2 = Card("spades", 5)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.player2_hand.append(card1)
        gamelogic.gameboard.player2_hand.append(card2)
        gamelogic.stage_card_from_hand(-1, card1)
        gamelogic.play_staged_cards(-1)

        gamelogic.stage_card_from_hand(-1, card2)
        result = gamelogic.play_staged_cards(-1)

        self.assertEqual(result, True)

    def test_last_played_card_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.player1_hand.append(card1)
        gamelogic.stage_card_from_hand(1, card1)
        gamelogic.play_staged_cards(1)

        self.assertEqual(gamelogic.player1_last_played, card1)

    def test_chance_player1_chances_on_turn_and_succeeds(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

        result = gamelogic.chance(1)

        self.assertEqual(result, True)

    def test_chance_player1_chances_on_turn_and_fails(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 5)
        card3 = Card("spades", 3)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

        result = gamelogic.chance(1)

        self.assertEqual(result, False)

    def test_chance_player1_chances_on_off_turn_and_succeeds(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 5)
        card4 = Card("hearts", 5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.player1_hand.append(card4)

        gamelogic.stage_card_from_hand(1, card4)
        result = gamelogic.play_staged_cards(1)

        gamelogic.gameboard.reserve_deck.append(card3)
        result = gamelogic.chance(1)

        self.assertEqual(result, True)

    def test_chance_player1_chances_on_off_turn_and_fails(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 6)
        card4 = Card("hearts", 5)

        gamelogic.turn = 1
        gamelogic.player1_locked = False

        gamelogic.gameboard.reserve_deck = []

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)
        gamelogic.gameboard.player1_hand.append(card4)

        gamelogic.stage_card_from_hand(1, card4)
        result = gamelogic.play_staged_cards(1)
        result = gamelogic.chance(1)

        self.assertEqual(result, False)

    def test_chance_player2_chances_on_turn_and_succeeds(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 5)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

        result = gamelogic.chance(-1)

        self.assertEqual(result, True)

    def test_chance_player2_chances_on_turn_and_fails(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 5)
        card3 = Card("spades", 3)

        gamelogic.turn *= -1

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

        result = gamelogic.chance(-1)

        self.assertEqual(result, False)

    def test_chance_player2_chances_on_off_turn_and_succeeds(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.turn = -1
        gamelogic.player2_locked = False

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 4)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

        result = gamelogic.chance(-1)

        self.assertEqual(result, True)

    def test_chance_player2_chances_on_offturn_and_fails(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 3)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

        result = gamelogic.chance(-1)

        self.assertEqual(result, False)

    def test_chance_reserve_deck_empty(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.player1_locked = False
        gamelogic.player2_locked = False
        gameboard.reserve_deck = []

        self.assertEqual(gamelogic.chance(1), False)

    def test_pick_up_field_deck_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 5)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)
        gamelogic.gameboard.field_deck.append(card3)

        gamelogic.pick_up_field_deck(1)

        field_length = len(gamelogic.gameboard.field_deck)
        player_hand_length = len(gamelogic.gameboard.player1_hand)

        self.assertEqual((field_length, player_hand_length), (0, 3))

    def test_pick_up_field_deck_player2(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 5)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)
        gamelogic.gameboard.field_deck.append(card3)

        gamelogic.pick_up_field_deck(-1)

        field_length = len(gamelogic.gameboard.field_deck)
        player_hand_length = len(gamelogic.gameboard.player2_hand)

        self.assertEqual((field_length, player_hand_length), (0, 3))

    def test_sort_hand(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card1 = Card("hearts", 2)
        card2 = Card("clubs", 3)
        card3 = Card("spades", 4)
        card4 = Card("diamonds", 5)

        gamelogic.gameboard.player1_hand.append(card3)
        gamelogic.gameboard.player1_hand.append(card4)
        gamelogic.gameboard.player1_hand.append(card2)
        gamelogic.gameboard.player1_hand.append(card1)

        gamelogic.gameboard.player2_hand.append(card3)
        gamelogic.gameboard.player2_hand.append(card4)
        gamelogic.gameboard.player2_hand.append(card2)
        gamelogic.gameboard.player2_hand.append(card1)

        gamelogic.sort_hand(1)
        gamelogic.sort_hand(-1)

        player1_first_card = gamelogic.gameboard.player1_hand[0].number
        player1_last_card = gamelogic.gameboard.player1_hand[-1].number
        player2_first_card = gamelogic.gameboard.player2_hand[0].number
        player2_last_card = gamelogic.gameboard.player2_hand[-1].number
        self.assertEqual((player1_first_card, player1_last_card,
                         player2_first_card, player2_last_card), (2, 5, 2, 5))

    def test_unstage_cards(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card1 = Card("hearts", 3)
        card2 = Card("clubs", 3)
        card3 = Card("spades", 3)
        card4 = Card("diamonds", 3)

        gamelogic.gameboard.player1_staged.append(card1)
        gamelogic.gameboard.player1_staged.append(card2)
        gamelogic.gameboard.player1_staged.append(card3)
        gamelogic.gameboard.player1_staged.append(card4)

        gamelogic.player1_locked = False

        gamelogic.unstage_cards()

        result = len(gamelogic.gameboard.player1_hand)

        self.assertEqual(result, 4)

    def test_sort_staged(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)
        card1 = Card("red_joker", 0)
        card2 = Card("clubs", 3)
        card3 = Card("spades", 3)
        card4 = Card("diamonds", 3)

        gamelogic.gameboard.player1_staged.append(card3)
        gamelogic.gameboard.player1_staged.append(card4)
        gamelogic.gameboard.player1_staged.append(card2)
        gamelogic.gameboard.player1_staged.append(card1)

        gamelogic.gameboard.player2_staged.append(card3)
        gamelogic.gameboard.player2_staged.append(card4)
        gamelogic.gameboard.player2_staged.append(card2)
        gamelogic.gameboard.player2_staged.append(card1)

        gamelogic.sort_hand(1)
        gamelogic.sort_hand(-1)

        player1_first_card = gamelogic.gameboard.player1_staged[0].number
        player1_last_card = gamelogic.gameboard.player1_staged[-1].number
        player2_first_card = gamelogic.gameboard.player2_staged[0].number
        player2_last_card = gamelogic.gameboard.player2_staged[-1].number
        self.assertEqual((player1_first_card, player1_last_card,
                         player2_first_card, player2_last_card), (3, 0, 3, 0))
