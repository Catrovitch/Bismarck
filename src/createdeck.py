from card import Card
import random

class CreateDeck:

    def __init__(self):

        self.deck = []

        self.create_deck()

    def create_deck(self):
        
        suits = ["hearts", "diamonds", "clubs", "spades"]
        numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]

        for suit in suits:
            for number in numbers:
                next_card = Card(suit, number)
                self.deck.append(next_card)

        self.deck.append(Card("black-joker", 0))
        self.deck.append(Card("red-joker", 0))

    def shuffle(self):

        random.shuffle(self.deck)

    def export(self):
        
        return self.deck
        