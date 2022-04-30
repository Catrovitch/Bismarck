import os
import pygame


def load_image(filename):
    """Used to upload images related to the program.

    Returns:
        image: returns an image relating to the filename given as an argument.
    """

    dirname = os.path.dirname(__file__)

    return pygame.image.load(os.path.join(dirname, "assets", filename))
