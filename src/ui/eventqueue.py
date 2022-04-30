import pygame


class EventQueue:

    """The EventQueue class is used to get all the events in a pygame instance.
    """

    def get(self):
        """Gets the events.

        Returns:
            list: returns a list of pygame events that has happend in the current Gameloop (Game method) cycle.
        """

        return pygame.event.get()
