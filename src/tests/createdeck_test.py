import unittest
from createdeck import CreateDeck


class TestCreateDeck(unittest.TestCase):

    def setUp(self):

        pass

    def test_create_deck_length_(self):

        created_deck = CreateDeck()

        length = len(created_deck.deck)

        self.assertEqual(length, 54)


    def test_create_deck_bottom_card(self):

        created_deck = CreateDeck()
        
        bottom_card = str(created_deck.deck[0])

        self.assertEqual(bottom_card, "2 hearts")

    def test_create_deck_top_card(self):

        created_deck = CreateDeck()
        
        top_card = str(created_deck.deck[-1])

        self.assertEqual(top_card, "0 red-joker")

    def test_create_deck_shuffle(self):

        created_deck = CreateDeck()

        for i in range(5):

            created_deck.shuffle()
            top_card = str(created_deck.deck[-1])
            self.assertNotEqual(top_card, "0 red-joker")

    def test_create_deck_export(self):

        created_deck = CreateDeck()

        exported_deck = created_deck.export()

        exported_deck_top_card = str(exported_deck[-1])

        self.assertEqual(exported_deck_top_card, "0 red-joker")