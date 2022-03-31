from card import Card


class Deck:

    def init(self):

        self.deck = []

    def create_deck(self):
        
        suits = ["hearts", "diamonds", "clubs", "spades"]
        numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        


        for suit in suits:
            for number in numbers:
                next_card = Card(suit, number)
                self.deck.append(next_card)

    def lay_deck(self):
        
        for card in self.deck:
            print(card.get_name())
        

deck = Deck()

deck.create_deck()