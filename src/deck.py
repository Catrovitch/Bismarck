class Deck:

    def __init__(self, deck: list):

        self.deck = deck

    def draw(self, destination: list):

        if len(self.deck) == 0:
            return False

        destination.append(self.deck.pop())
        
        return True
    
    def empty(self):

        if len(self.deck) >= 1:
            return False
        
        else:
            return True
