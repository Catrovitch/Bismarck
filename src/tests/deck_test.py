import unittest
from createdeck import CreateDeck
from deck import Deck

class TestDeck(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_deck_type(self):


        create_deck = CreateDeck()
        create_deck = create_deck.export()
        deck = Deck(create_deck)

        if type(deck.deck) == list:
            result = True
        else:
            result = False

        self.assertEqual(result, True)

    def test_draw_one_card(self):

        create_deck = CreateDeck()
        create_deck = create_deck.export()
        deck = Deck(create_deck)

        destination_list = []

        result = deck.draw(destination_list)

        self.assertEqual(result, True)



    def test_draw_last_card(self):

        create_deck = CreateDeck()
        create_deck = create_deck.export()
        deck = Deck(create_deck)

        destination_list = []

        for i in range(55):
            result = deck.draw(destination_list)

        self.assertEqual(result, False)


    def test_draw_correct_card(self):

        create_deck = CreateDeck()
        create_deck = create_deck.export()
        deck = Deck(create_deck)

        destination_list = []

        deck.draw(destination_list)

        result = str(destination_list[0])

        self.assertEqual(result, "0 red-joker")

    def test_deck_empty_not_empty(self):

        create_deck = CreateDeck()
        create_deck = create_deck.export()
        deck = Deck(create_deck)

        result = deck.empty()

        self.assertEqual(result, False)

    def test_deck_empty_is_empty(self):

        create_deck = CreateDeck()
        create_deck = create_deck.export()
        deck = Deck(create_deck)

        destination_list = []

        for i in range(55):
            result = deck.draw(destination_list)

        result = deck.empty()

        self.assertEqual(result, True)
