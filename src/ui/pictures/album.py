from ui.pictures.pictures import Picture


class Album:

    def __init__(self):

        self.images = {}
        self.create_all()

    def create_all(self):

        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for suit in suits:
            for number in numbers:
                name = f"{number}_of_{suit}"
                filename = name+".png"
                self.images[name] = Picture(filename)

        self.images["0_of_red-joker"] = Picture("0_of_red-joker.png")
        self.images["0_of_black-joker"] = Picture("0_of_black-joker.png")
        self.images["cardback"] = Picture("cardback.png")
        self.images["background"] = Picture("background.png")
