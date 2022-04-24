import unittest
import os
import pygame
from ui.pictures.load_images import load_image


class TestLoadimage(unittest.TestCase):

    def setUp(self):

        pass

    def test_load_image(self):

        dirname = os.path.dirname(__file__)

        self.assertAlmostEqual((type(pygame.image.load(os.path.join(
            "src", "ui", "pictures", "assets", "0_of_black-joker.png")))), (type(load_image("0_of_black-joker.png"))))
