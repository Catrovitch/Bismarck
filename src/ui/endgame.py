class Player1Endgame:

    def __init__(self):

        self.first = False
        self.first_cordinates = (750, 635)
        self.second = False
        self.second_cordinates = (850, 635)
        self.third = False
        self.third_cordinates = (950, 635)

    def add_card(self, card, place):

        if place == "first":
            self.first = card
            return
        if place == "second":
            self.second = card
            return
        else:
            self.third = card
            return
    
    def use_card(self, place):

        self.place = False


class Player2Endgame:

    def __init__(self):

        self.first = False
        self.first_cordinates = (200, 380)
        self.second = False
        self.second_cordinates = (300, 380)
        self.third = False
        self.third_cordinates = (400, 380)

    def add_card(self, card, place):
        
        if place == "first":
            self.first = card
            return
        if place == "second":
            self.second = card
            return
        else:
            self.third = card
            return
    
    def use_card(self, place):

        self.place = False
