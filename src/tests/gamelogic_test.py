import unittest
from createdeck import CreateDeck
from gameboard import GameBoard
from gamelogic import GameLogic
from card import Card


class TestGameLogic(unittest.TestCase):

    def setUp(self):
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

        self.assertEqual((p1h, p1f, p2h, p2f), (6, 3, 6, 3))

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

    def test_stage_card_normal(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.gameboard.initial_deal()

        player1 = gamelogic.stage_card_from_hand(
            1, gamelogic.gameboard.player1_hand[0])
        player2 = gamelogic.stage_card_from_hand(
            -1, gamelogic.gameboard.player2_hand[0])

        self.assertEqual((player1, player2), (True, True))

    def test_stage_card_two_different_false(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        gamelogic.gameboard.initial_deal()

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

    def test_play_staged_cards_field_deck_length_player1(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card(2, "hearts")
        card2 = Card(2, "spades")

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

        gamelogic.gameboard.player2_staged.append(card1)
        gamelogic.gameboard.player2_staged.append(card2)

        gamelogic.play_staged_cards(-1)

        field_deck_length = len(gamelogic.gameboard.field_deck)

        self.assertEqual(field_deck_length, 2)

    def test_stage_card_from_endgame_normal(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 3)
        card2 = Card("spades", 3)

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

    def test_check_card_hierarchy_card2_is_higher(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 3)
        card2 = Card("hearts", 4)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_card2_is_lower(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

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

        gamelogic.gameboard.field_deck.append(card1)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_two(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 2)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_ten(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 10)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        result = gamelogic.check_card_hierarchy(1, 1)

        self.assertEqual(result, True)

    def test_check_card_hierarchy_special_card_ten_empties_field_to_trash(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 13)
        card2 = Card("hearts", 10)

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.field_deck.append(card2)

        gamelogic.check_card_hierarchy(1, 1)

        field_length = len(gamelogic.gameboard.field_deck)
        trash_length = len(gamelogic.gameboard.trash_deck)

        self.assertEqual((field_length, trash_length), (0, 2))

    def test_chance_player1_chances_on_turn_and_succeeds(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 5)

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

    def test_chance_player1_chances_on_offturn_and_succeeds(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 4)

        gamelogic.turn *= -1

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

        result = gamelogic.chance(1)

        self.assertEqual(result, True)

    def test_chance_player1_chances_on_offturn_and_fails(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

        card1 = Card("hearts", 4)
        card2 = Card("hearts", 3)
        card3 = Card("spades", 5)

        gamelogic.turn *= -1

        gamelogic.gameboard.field_deck.append(card1)
        gamelogic.gameboard.reserve_deck.append(card2)
        gamelogic.gameboard.reserve_deck.append(card3)

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

        gamelogic.turn *= -1

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

    def test_chance_player2_chances_on_offturn_and_succeeds(self):

        createddeck = CreateDeck()
        deck = createddeck.export()
        gameboard = GameBoard(deck)
        gamelogic = GameLogic(gameboard)

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
