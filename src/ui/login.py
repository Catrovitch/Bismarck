import pygame

class Login:

    def __init__(self, renderer, eventqueue, clock, gameboard_positions, user_control):

        self.renderer = renderer
        self.eventqueue = eventqueue
        self.clock = clock
        self.gameboard_positions = gameboard_positions
        self.user_control = user_control

        self.main_menu = False
        self.create_account = False

        self.login_loop()


    def login_loop(self):

        while True:

            if self.handle_events() is False:
                break
            
            if self.create_account:
                return 2
            if self.main_menu:
                return 3

            self.renderer.render_login()

            self.clock.tick(60)


    def handle_events(self):

        for event in self.eventqueue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if self.gameboard_positions.exitbutton.in_position(pos):
                    return False

                if self.gameboard_positions.create_new_account_button.in_position(pos):
                    self.create_account = True

                if self.gameboard_positions.login_button.in_position(pos):
                    self.login(self.gameboard_positions.account_box.text, self.gameboard_positions.password_box.text)

                if self.gameboard_positions.exitbutton.in_position(pos):
                    return False

                if self.gameboard_positions.account_box.in_position(pos):
                    self.gameboard_positions.account_box.selected = True
                    self.gameboard_positions.password_box.selected = False

                if self.gameboard_positions.password_box.in_position(pos):
                    self.gameboard_positions.password_box.selected = True
                    self.gameboard_positions.account_box.selected = False

            if event.type == pygame.KEYDOWN:

                if self.gameboard_positions.account_box.selected:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameboard_positions.account_box.delete()
                        continue
                    else:
                        self.gameboard_positions.account_box.add(event.unicode)

                if self.gameboard_positions.password_box.selected:
                    if event.key == pygame.K_BACKSPACE:
                        self.gameboard_positions.password_box.delete()
                        continue
                    self.gameboard_positions.password_box.add(event.unicode)

            if event.type == pygame.QUIT:
                return False

    def login(self, username=None, password=None):
        
        if self.user_control.login(username, password):
            self.gameboard_positions.name_box.text = username
            self.main_menu = True