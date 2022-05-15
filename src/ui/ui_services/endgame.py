class PlayerEndgame:

    """The class PlayerEndgame is used by the UI to keep track on the endgame_cards of a player. 

    Attributes:
        first: Keeps track on the first endgame_card. This is = False if it's not avaiable I.E it hasn't been chosen or it has been used and is = card if it is available.
        second: Keeps track on the endgame_card. 
        third: Keeps track on the third endgame_card.
    """

    def __init__(self):
        """The constructor of the class.
        """

        self.first = False
        self.first_target = False

        self.second = False
        self.second_target = False

        self.third = False
        self.third_target = False

    def add_card(self, card, place):
        """Adds a card to either the first, second or third endgame_card slot.

        Args:
            card: The card that will be placed. This is an item of the class Picture.
            place: will either be "first", "second" or "third". Which in each case will correspond to the relevant attribute.
        """

        if place == "first":
            self.first = card
            return
        if place == "second":
            self.second = card
            return
        else:
            self.third = card
            return

    def use_card(self, card):

        if self.first == card:
            self.first = False
            self.first_target = False
            return
        if self.second == card:
            self.second = False
            self.second_target = False
            return
        if self.third == card:
            self.third = False
            self.third_target = False
            return
