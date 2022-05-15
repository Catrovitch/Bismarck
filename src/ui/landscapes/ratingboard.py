import pygame


class RatingBoard:

    def __init__(self, renderer, eventqueue, clock, gameboard_positions):

        self.renderer = renderer
        self.eventqueue = eventqueue
        self.clock = clock
        self.gameboard_positions = gameboard_positions

        self.main_menu = False

        self.create_account = False

        self.ratingboard_loop()

    def ratingboard_loop(self):

        while True:

            if self.handle_events() is False:
                break

            if self.main_menu:
                return 3

            self.renderer.render_ratingboard()

            self.clock.tick(60)

    def handle_events(self):

        for event in self.eventqueue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if self.gameboard_positions.exitbutton.in_position(pos):
                    self.main_menu = True

            if event.type == pygame.QUIT:
                return False
