# The Gameboard class will be used to oversee all cards
# and where they are at all times of the game.

class GameBoard:

    def __init__(self, deck):

        # All of these are shared between both players
        self.reserve_deck = deck

        self.field_deck = []
        self.trash_deck = []

        # Player1 specific
        self.player1_hand = []
        self.player1_endgame = []
        self.player1_final = []
        self.player1_staged = []

        # Player2 specific
        self.player2_hand = []
        self.player2_endgame = []
        self.player2_final = []
        self.player2_staged = []
