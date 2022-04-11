class Card:

    def __init__(self, suit, number):

        self.suit = suit
        self.number = number
        self.name = f"{number} {suit}"

    def __str__(self):

        return self.name
