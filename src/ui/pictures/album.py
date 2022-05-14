from ui.pictures.pictures import Picture


class Album:

    """The class Album is a that creates a dictionary of items of the Picture class where the Picture.name being the key and the value being the Picture itself.

    Attributes:
        images: dictionary
    """

    def __init__(self):
        """The constructor of the class which initiates the attribute images and calls on the method "create_all"
        """
        self.images = {}
        self.create_all()

    def create_all(self):
        """The create_all method creates all the pictures used in the program.
        """

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
        self.images["rule1"] = Picture("rule1.png")
        self.images["rule2"] = Picture("rule2.png")
        self.images["rule3"] = Picture("rule3.png")
