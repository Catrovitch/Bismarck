class Card:

    def init(self, suit, number):
        
        self.suit = suit
        self.number = number
        self.name = f"{number} {suit}"

    def get_number(self):

        return self.number

    def get_suit(self):

        return self.suit

    def get_name(self):

        return self.name