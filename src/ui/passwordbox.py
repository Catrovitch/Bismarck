import pygame


class PasswordBox:

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.text = ""
        self.max_length = 16
        self.selected = False

    def add(self, character):

        allowed = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ1234567890!#¤%&/()=?"

        if len(self.text) < self.max_length and character in allowed:
            self.text += character
            return True

        else:
            return False

    def delete(self):

        if len(self.text) > 0:
            self.text = self.text[0:-1]
            return True
        else:
            return False

    def in_position(self, position):
        """Checks if the mouse-cursor is within the object.

        Args:
            position: gives the position of the mouse-cursor as coordinates. (tuple)

        Returns:
            True: if the position of the mouse-cursor is within the object
            False: if the position of the mouse-cursor is not within the object.
        """

        if self.x <= position[0] <= self.x + self.width and self.y <= position[1] <= self.y + self.height:
            return True

        return False

    def render(self, display):

        box_colour = (192, 210, 192)
        frame_colour = (50, 70, 50)

        if self.selected:
            box_colour = (210, 220, 210)

        font = pygame.font.SysFont("Arial", 35)
        font_colour = (20, 20, 20)
        text = "*"*len(self.text)
        text = font.render(text, True, font_colour)
        text_x = self.x + 10
        text_y = self.y + 10
        text_coordinates = (text_x, text_y)

        frame_size = 2
        
        if self.selected:
            frame_size = 3
            frame_colour = (211, 154, 0)

        pygame.draw.rect(display, (box_colour),
                         (self.x, self.y, self.width, self.height))
        pygame.draw.rect(display, (frame_colour),
                         (self.x, self.y, self.width, self.height), frame_size)

        display.blit(
            text, (text_coordinates))
