import unittest
from createdeck import CreateDeck


class TestCreateDeck(unittest.TestCase):

    def setUp(self):

        pass

    def test_create_deck_length_(self):

        created_deck = CreateDeck()

        length = len(created_deck.deck)

        self.assertEqual(length, 54)

    def test_create_deck_shuffle(self):

        created_deck = CreateDeck()

        for i in range(5):

            created_deck.shuffle()
            top_card = str(created_deck.deck[-1])
            self.assertNotEqual(top_card, "0 red-joker")

    def test_create_deck_export(self):

        created_deck = CreateDeck()

        exported_deck = created_deck.export()

        exported_deck_len = len(exported_deck)

        self.assertEqual(exported_deck_len, 54)
