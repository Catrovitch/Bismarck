class Player:

    def __init__(self, player_id, gamelogic):

        self.player_id = player_id
        self.gamelogic = gamelogic

    def stage_card_from_hand(self, card):
        
        self.gamelogic.stage_card_from_hand(self.player_id, card)

    def stage_card_from_endgame(self, card):
        
        self.gamelogic.stage_card_from_endgame(self.player_id, card)

    def play_staged_cards(self):

        self.gamelogic.play_staged_cards(self.player_id)

    def pick_up_field_deck(self):

        self.gamelogic.pick_up_field_deck(self.player_id)

    def chance(self):

        self.gamelogic.chance(self.player_id)

    