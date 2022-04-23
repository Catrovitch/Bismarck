from ui.load_images import load_image
import pygame


class Cardback:

    def __init__(self):

        self.image = load_image("card_back.png")
        self.x = 0
        self.y = 0
        self.target = False
        self.cord = (self.x, self.y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()



class Background:

    def __init__(self):

        self.image = load_image("background.png")
        self.width = self.image.get_width()*1.5
        self.height = self.image.get_height()*1.3

class CardPicture:

    def __init__(self, card):

        self.image = load_image(card)
        self.name = card[:-4]
        self.target = False
        self.x = 0
        self.y = 0
        self.cord = (self.x, self.y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        
class PlayButton:

    def __init__(self):

        self.image = load_image("play_button.png")

        self.name = "play_button"

        self.x = 0
        self.y = 0
        self.cord = (self.x, self.y)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
