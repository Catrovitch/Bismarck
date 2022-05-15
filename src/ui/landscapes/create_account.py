import pygame


class CreateAccount:

    def __init__(self, renderer, eventqueue, clock, gameboard_positions, user_control):

        self.renderer = renderer
        self.eventqueue = eventqueue
        self.clock = clock
        self.gameboard_positions = gameboard_positions
        self.user_control = user_control

        self.login = False
        self.main_menu = False

        self.create_account_loop()

    def create_account_loop(self):

        while True:

            if self.handle_events() is False:
                break

            if self.login:
                return 1

            if self.main_menu:
                return 3

            self.renderer.render_create_account()

            self.clock.tick(60)

    def handle_events(self):

        for event in self.eventqueue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                self.click = True
                pos = pygame.mouse.get_pos()

                if self.gameboard_positions.create_account_button.in_position(pos):
                    self.create_an_account(self.gameboard_positions.accountname_box.text,
                                           self.gameboard_positions.password_enter_box.text,
                                           self.gameboard_positions.password_confirmation_box.text)

                if self.gameboard_positions.cancel_button.in_position(pos):
                    self.login = True

                if self.gameboard_positions.accountname_box.in_position(pos):
                    self.gameboard_positions.accountname_box.selected = True
                    self.gameboard_positions.password_enter_box.selected = False
                    self.gameboard_positions.password_confirmation_box.selected = False

                if self.gameboard_positions.password_enter_box.in_position(pos):
                    self.gameboard_positions.accountname_box.selected = False
                    self.gameboard_positions.password_enter_box.selected = True
                    self.gameboard_positions.password_confirmation_box.selected = False

                if self.gameboard_positions.password_confirmation_box.in_position(pos):
                    self.gameboard_positions.accountname_box.selected = False
                    self.gameboard_positions.password_enter_box.selected = False
                    self.gameboard_positions.password_confirmation_box.selected = True

            if event.type == pygame.KEYDOWN:

                if self.gameboard_positions.accountname_box.selected:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameboard_positions.accountname_box.delete()
                        continue
                    else:
                        self.gameboard_positions.accountname_box.add(
                            event.unicode)

                if self.gameboard_positions.password_enter_box.selected:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameboard_positions.password_enter_box.delete()
                        continue
                    self.gameboard_positions.password_enter_box.add(
                        event.unicode)

                if self.gameboard_positions.password_confirmation_box.selected:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameboard_positions.password_confirmation_box.delete()
                        continue
                    self.gameboard_positions.password_confirmation_box.add(
                        event.unicode)

            if event.type == pygame.QUIT:
                return False

    def create_an_account(self, username, password1, password2):

        if self.user_control.create_user(username, password1, password2):
            self.gameboard_positions.name_box.text = username
            self.main_menu = True
