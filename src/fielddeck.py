from deck import Deck


class FieldDeck(Deck):

    def __init__(self):

        self.deck = []
        self.fallen = []

    def fell(self):

        while not self.empty():
            self.fallen.append(self.deck.pop())
            