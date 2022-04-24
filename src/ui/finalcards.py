class Player1Final:

    def __init__(self):

        self.first = False
        self.first_cordinates = (750, 650)
        self.second = False
        self.second_cordinates = (850, 650)
        self.third = False
        self.third_cordinates = (950, 650)

    def add_card(self):

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

        self.place = False

        return


class Player2Final:

    def __init__(self):

        self.first = False
        self.first_cordinates = (750, 150)
        self.second = False
        self.second_cordinates = (850, 150)
        self.third = False
        self.third_cordinates = (950, 150)

    def add_card(self):

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

        self.place = False

        return
