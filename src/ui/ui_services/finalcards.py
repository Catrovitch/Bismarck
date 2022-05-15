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
        self.first_target = False
        self.first_x = 0
        self.first_y = 0

        self.second = False
        self.second_target = False
        self.second_x = 0
        self.second_y = 0

        self.third = False
        self.third_target = False
        self.third_x = 0
        self.third_y = 0

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

    def use_card(self, place):

        if place == "first":
            self.first = False
            return
        if place == "second":
            self.second = False
            return

        self.third = False
        return
