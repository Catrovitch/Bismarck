class Player:

    #The player class will be used to give commands of what cards to play where.
    def __init__(self, account_name, gamelogic, player_id):

        self.account_name = account_name
        self.gamelogic = gamelogic
        self.player_id = player_id
    
    #Stages a card to be committed.
    def stage_hand_card(self, player, card_index):    

        self.gamelogic.stage_card(player, card_index)


