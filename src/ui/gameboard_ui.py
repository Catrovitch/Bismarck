class GameboardUI:

    def __init__(self, gamelogic, player1_endgame, player1_final, player2_endgame, player2_final):

        self.gamelogic = gamelogic

        # All of these are shared between both players
        self.reserve_deck = True

        self.field_deck = False
        self.trash_deck = False

        # Player1 specific
        self.player1_hand = []
        self.player1_endgame = player1_endgame
        self.player1_final = player1_final
        self.player1_staged = 0

        # Player2 specific
        self.player2_hand = []
        self.player2_endgame = player2_endgame
        self.player2_final = player2_final
        self.player2_staged = 0

    def update(self):

        self.update_reserve_deck()
        self.update_field_deck()
        self.update_trash_deck()
        self.update_player1_hand()
        self.update_player2_hand()

    def update_reserve_deck(self):

        if len(self.gamelogic.gameboard.reserve_deck) == 0:
            self.reserve_deck = False
            return
        
        self.reserve_deck = True
        return
    
    def update_field_deck(self):
        
        if len(self.gamelogic.gameboard.field_deck) > 0:
            self.field_deck = self.gamelogic.gameboard.field_deck[-1].name
            return
        self.field_deck = False
        return

    def update_trash_deck(self):

        if len(self.gamelogic.gameboard.trash_deck) > 0:
            self.trash_deck = True
            return
        self.trash_deck = False
        return

    def update_player1_hand(self):
        
        self.player1_hand = []

        for card in self.gamelogic.gameboard.player1_hand:
            self.player1_hand.append(card.name)

    def update_player2_hand(self):
        
        self.player2_hand = []

        for card in self.gamelogic.gameboard.player2_hand:
            self.player2_hand.append(card.name)


    



    


