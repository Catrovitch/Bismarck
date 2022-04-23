from ui.scaled.scaling import CardPicture, Cardback

class CardPics:

    def __init__(self):

        self.card_pics = {}
        self.create_all()

    def create_all(self):

        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]

        for suit in suits:
            for number in numbers:
                name = f"{number}_of_{suit}"
                filename = name+".png"
                self.card_pics[name] = CardPicture(filename)


        self.card_pics["0_of_red-joker"] = CardPicture("0_of_red-joker.png")
        self.card_pics["0_of_black-joker"] = CardPicture("0_of_black-joker.png")
        self.card_pics["cardback"] = Cardback()