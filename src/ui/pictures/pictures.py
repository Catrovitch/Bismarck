from ui.pictures.load_images import load_image


class Picture:

    """The Picture class is used to keep track of various images used in the program.

    Attributes:
        image: through the function "load_image" the correct image is uploaded.
        name: the name of the picture
        target: keeps track of if the picture is targeted (True) by the player or not (False).
        x: x-cordinate
        y: y-cordinate
        cord: (x,y)-cordinate
        width: width of the picture
        heihgt: height of the picture
    """

    def __init__(self, name):
        """Constructor of the class. 

        Args:
            name: gives the name of the file which will be used to upload the correct image and to decide the name attribute.
        """

        self.image = load_image(name)
        self.name = name[:-4]

        self.target = False

        self.x = 0
        self.y = 0
        self.cord = (self.x, self.y)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
