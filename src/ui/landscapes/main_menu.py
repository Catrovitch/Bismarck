import pygame


class MainMenu:

    def __init__(self, renderer, eventqueue, clock, gameboard_positions):

        self.renderer = renderer
        self.eventqueue = eventqueue
        self.clock = clock
        self.gameboard_positions = gameboard_positions

        self.login = False
        self.game = False
        self.rules = False
        self.ratingboard = False

        self.create_account = False

        self.main_menu_loop()

    def main_menu_loop(self):

        while True:

            if self.handle_events() is False:
                break

            if self.login:
                return 1

            if self.game:
                return 4

            if self.rules:
                return 5

            if self.ratingboard:
                return 6

            self.renderer.render_main_menu()

            self.clock.tick(60)

    def handle_events(self):

        for event in self.eventqueue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if self.gameboard_positions.exitbutton.in_position(pos):
                    self.login = True

                if self.gameboard_positions.play_game_button.in_position(pos):
                    self.game = True

                if self.gameboard_positions.rules_button.in_position(pos):
                    self.rules = True

                if self.gameboard_positions.ratingboard_button.in_position(pos):
                    self.ratingboard = True

            if event.type == pygame.QUIT:
                return False
