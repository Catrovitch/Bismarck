from ui.pictures.load_images import load_image


class Picture:

    def __init__(self, name):

        self.image = load_image(name)
        self.name = name[:-4]

        self.target = False

        self.x = 0
        self.y = 0
        self.cord = (self.x, self.y)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
