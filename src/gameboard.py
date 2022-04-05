from createdeck import CreateDeck

#The Gameboard class will be used to oversee all cards
#and where they are at all times of the game.
class GameBoard:

    def __init__(self, deck):

        #All of these are shared between both players
        self.reserve_deck = deck
        self.field_deck = []
        self.trash_deck = []

        #Player1 specific
        self.player1_hand = []
        self.player1_endgame = []
        self.player1_final = []
        self.player1_staged = []

        #Player2 specific
        self.player2_hand = []
        self.player2_endgame = []
        self.player2_final = []
        self.player2_staged = []

    def move(self, origin: list, destination: list, card_index):
        #This functions is used to move a card from one list to an other.
        destination.append(origin.pop(card_index))

    def initial_deal(self):
        #This function is called at the beginning of a game.
        for i in range(0, 6):

            self.move(self.reserve_deck, self.player1_hand, -1)
            self.move(self.reserve_deck, self.player2_hand, -1)

createddeck = CreateDeck()
deck = createddeck.export()
gameboard = GameBoard(deck)

print(len(gameboard.reserve_deck))