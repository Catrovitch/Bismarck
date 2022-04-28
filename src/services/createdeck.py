import random
from services.card import Card


class CreateDeck:

    """A class that is used to create a deck of cards of the English/French deck. Each individual card is an instance of the "Card" class.

    Attributes:
        deck: A list which contains all cards.
    """

    def __init__(self):

        """Constructor of the class which initiates the class and calls on the method "create_deck" which takes care of the actual creation of the deck.

        Args:
            No arguments.
        """
        self.deck = []

        self.create_deck()

    def create_deck(self):

        """Creates a deck of cards where each card is an instance of the "Card" class.

        Args:
            No arguments.
        """

        suits = ["hearts", "diamonds", "clubs", "spades"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for suit in suits:
            for number in numbers:
                next_card = Card(suit, number)
                self.deck.append(next_card)

        self.deck.append(Card("black-joker", 0))
        self.deck.append(Card("red-joker", 0))

    def shuffle(self):
    
        """Shuffles the items (cards) in the attribute self.deck"

        Args:
            No arguments.
        """

        random.shuffle(self.deck)

    def export(self):

        """This method is used to export a ready to use shuffled deck of cards. To make sure the cards are shuffled it always calls on the shuffle function.

        Returns:
            _type_: A deck of cards.
        """

        self.shuffle()

        return self.deck
