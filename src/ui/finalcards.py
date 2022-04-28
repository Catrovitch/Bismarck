class PlayerFinal:

    """The class PlayerFinal is used by the UI to keep track on the final_cards of a player. 

    Attributes:
        first: Keeps track of the first final_card of the player. This is False when not available I.E. before the initial_deal (GameLogic method) of the game or after a player has used a final_card.
        second: Keeps track of the second final_card.
        third: Keeps track of the third final_card.
    """

    def __init__(self):

        """The constructor of the class. 
        """

        self.first = False
        self.second = False
        self.third = False

    def add_card(self):

        """Method is used to add a card to a player. This happens at the initial_deal (GameLogic method).
        """

        if self.first == False:
            self.first = True
            return
        if self.second == False:
            self.second = True
            return
        if self.third == False:
            self.third = True
            return

