from card import Card
import random

class Deck:

    def __init__(self):

        self.deck = []

    def draw(self, destination: list):

        if len(self.deck) == 0:
            return False

        destination.append(self.deck.pop())
    
    def empty(self):

        if len(self.deck) >= 1:
            return False
        
        else:
            return True
d = Deck()
