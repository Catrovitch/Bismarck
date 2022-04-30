import pygame


class Game:

    """The class Game is used to run the various stages of the main Game. 

    Attributes:
        gamelogic: instance of the class GameLogic
        gameboard_positions: instance of the class GameboardPositions

        player1: instance of the class Player corresponding to Player 1 in the game.
        player2: instance of the class Player corresponding to Player 2 in the game.

        renderer: instance of the class Renderer which is used to render everything.
        album: instance of the class Album which contains all pictures used in the game.
        eventqueue: instance of the class EventQueue which stores a list of events occuring in the game.
        clock: instance of the class Clock which keeps track of time.

        player1_endgame: instance of the class EndGame which keeps track of player1 endgame_cards.
        player1_final: instance of the class FinalCards which keeps track of player1 final_cards.
        player2_endgame: instance of the class EndGame which keeps track of player2 endgame_cards.
        player2_final: instance of the class FinalCards which keeps track of player2 final_cards.

        target: keeps track of if a card is targeted by a player.

        game_begun: keeps track on if the game has begun.
    """

    def __init__(self, gamelogic, gameboard_positions, player1, player2, renderer, album, eventqueue, clock, player1_endgame, player1_final, player2_endgame, player2_final, bismarck):
        """The constructor of the class. After assigning the corresponding arguments with their attributes it initiates the first stage of the game with the method initial_deal(). After this initiates the Gameloop method.

        Args:
            gamelogic: instance of the class GameLogic
            gameboard_positions: instance of the class GameboardPositions

            player1: instance of the class Player corresponding to Player 1 in the game.
            player2: instance of the class Player corresponding to Player 2 in the game.

            renderer: instance of the class Renderer which is used to render everything.
            album: instance of the class Album which contains all pictures used in the game.
            eventqueue: instance of the class EventQueue which stores a list of events occuring in the game.
            clock: instance of the class Clock which keeps track of time.

            player1_endgame: instance of the class EndGame which keeps track of player1 endgame_cards.
            player1_final: instance of the class FinalCards which keeps track of player1 final_cards.
            player2_endgame: instance of the class EndGame which keeps track of player2 endgame_cards.
            player2_final: instance of the class FinalCards which keeps track of player2 final_cards.
        """

        self.gamelogic = gamelogic
        self.gameboard_positions = gameboard_positions

        self.player1 = player1
        self.player2 = player2
        self.bismarck = bismarck

        self.renderer = renderer
        self.album = album.images
        self.eventqueue = eventqueue
        self.clock = clock

        self.player1_endgame = player1_endgame
        self.player1_final = player1_final
        self.player2_endgame = player2_endgame
        self.player2_final = player2_final

        self.target = None

        self.game_begun = False

        self.initial_deal()
        self.gamelogic.decide_turn_in_beginning()
        self.bismarck.choose_endgame_cards()
        self.gameloop()

    def initial_deal(self):
        """The method initial_deal calls on the gamelogic method inital_deal and sees that the corresponding response is met on the UI side of the program.
        """

        self.gamelogic.initial_deal()

        dealt = 0

        while dealt < 3:
            dealt += 1
            self.player1_final.add_card()
            self.player2_final.add_card()

    def gameloop(self):
        """This is the main loop of the game. It checks for events that has occured each loop and calls on the renderer to render stuff. The clock ticks 60/second.
        """

        while True:

            if self.handle_events() is False:
                break

            if self.game_begun == True:
                self.bismarck.choose_played_cards()
            self.renderer.render()

            self.clock.tick(60)

    def handle_events(self):
        """Handle_events gets a list of events that has occured and desides the corresponding result of these events.

        Returns:
            False: event = QUIT. I.E. if the user exits the program.
        """

        for event in self.eventqueue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                self.click = True
                pos = pygame.mouse.get_pos()

                if self.gameboard_positions.endgamebutton.in_position(pos):
                    self.game_begun = True
                    self.gamelogic.player1_locked = False
                    self.gamelogic.player2_locked = False
                    self.gamelogic.gameboard.reserve_deck.clear()
                    self.gamelogic.gameboard.player1_hand.clear()
                    self.gamelogic.gameboard.player2_hand.clear()
                    self.gamelogic.gameboard.player1_staged.clear()
                    self.gamelogic.gameboard.player2_staged.clear()
                    self.gamelogic.turn = 1

                if self.gameboard_positions.exitbutton.in_position(pos):
                    return False

                if len(self.gamelogic.gameboard.player1_endgame) == 0 and len(self.gamelogic.gameboard.player1_hand) == 0:

                    if self.gameboard_positions.player1_final_first.in_position(pos) and self.player1_final.first == True:
                        self.player1_final.first = False
                        self.player1.play_finalcard()

                    if self.gameboard_positions.player1_final_second.in_position(pos) and self.player1_final.second == True:
                        self.player1_final.second = False
                        self.player1.play_finalcard()

                    if self.gameboard_positions.player1_final_third.in_position(pos) and self.player1_final.third == True:
                        self.player1_final.third = False
                        self.player1.play_finalcard()

                for card in self.gamelogic.gameboard.player1_hand:
                    ui_card = self.album[card.name]

                    if ui_card.x <= pos[0] <= ui_card.x + ui_card.width and ui_card.y <= pos[1] <= ui_card.y + ui_card.height:

                        ui_card.target = True
                        mouse_x, mouse_y = event.pos
                        self.offset_x = ui_card.x - mouse_x
                        self.offset_y = ui_card.y - mouse_y

                if len(self.gamelogic.gameboard.reserve_deck) == 0 and len(self.gamelogic.gameboard.player1_hand) == 0:

                    for card in self.gamelogic.gameboard.player1_endgame:
                        ui_card = self.album[card.name]

                        if self.gameboard_positions.player1_endgame_first.in_position(pos) and self.player1_endgame.first != False:

                            self.player1_endgame.first_target = True
                            ui_card.x = self.gameboard_positions.player1_endgame_first.x
                            ui_card.y = self.gameboard_positions.player1_endgame_first.y
                            ui_card.target = True
                            mouse_x, mouse_y = event.pos
                            self.offset_x = ui_card.x - mouse_x
                            self.offset_y = ui_card.y - mouse_y

                        if self.gameboard_positions.player1_endgame_second.in_position(pos) and self.player1_endgame.second != False:

                            self.player1_endgame.second_target = True
                            ui_card.x = self.gameboard_positions.player1_endgame_second.x
                            ui_card.y = self.gameboard_positions.player1_endgame_second.y
                            ui_card.target = True
                            mouse_x, mouse_y = event.pos
                            self.offset_x = ui_card.x - mouse_x
                            self.offset_y = ui_card.y - mouse_y

                        if self.gameboard_positions.player1_endgame_third.in_position(pos) and self.player1_endgame.third != False:

                            self.player1_endgame.third_target = True
                            ui_card.x = self.gameboard_positions.player1_endgame_third.x
                            ui_card.y = self.gameboard_positions.player1_endgame_third.y
                            ui_card.target = True
                            mouse_x, mouse_y = event.pos
                            self.offset_x = ui_card.x - mouse_x
                            self.offset_y = ui_card.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for name, card in self.album.items():

                        # Choose first endgame card
                        if card.target == True and self.player1_endgame.first == False and self.gameboard_positions.player1_endgame_first.in_position(pos):

                            self.player1_endgame.add_card(card, "first")
                            self.player1_endgame.first = card
                            for real_card in self.gamelogic.gameboard.player1_hand:

                                if real_card.name == card.name:

                                    self.gamelogic.choose_endgame_cards(
                                        1, real_card)
                                    card.target = False
                                    if self.player1_endgame.first and self.player1_endgame.second and self.player1_endgame.third:
                                        self.game_begun = True
                                    return

                        # Choose second endgame card
                        if card.target == True and self.player1_endgame.second == False and self.gameboard_positions.player1_endgame_second.in_position(pos):

                            self.player1_endgame.add_card(card, "second")
                            self.player1_endgame.second = card
                            for real_card in self.gamelogic.gameboard.player1_hand:
                                if real_card.name == card.name:

                                    self.gamelogic.choose_endgame_cards(
                                        1, real_card)
                                    card.target = False
                                    if self.player1_endgame.first and self.player1_endgame.second and self.player1_endgame.third:
                                        self.game_begun = True
                                    return

                        # Choose third endgame card
                        if card.target == True and self.player1_endgame.third == False and self.gameboard_positions.player1_endgame_third.in_position(pos):

                            self.player1_endgame.add_card(card, "third")
                            self.player1_endgame.third = card
                            for real_card in self.gamelogic.gameboard.player1_hand:
                                if real_card.name == card.name:

                                    self.gamelogic.choose_endgame_cards(
                                        1, real_card)
                                    card.target = False
                                    if self.player1_endgame.first and self.player1_endgame.second and self.player1_endgame.third:
                                        self.game_begun = True
                                    return

                        # Stage a card
                        if card.target == True and self.gameboard_positions.player1_staged.in_position(pos) and self.game_begun == True:

                            for real_card in self.gamelogic.gameboard.player1_hand:
                                if real_card.name == card.name:
                                    self.gamelogic.stage_card_from_hand(
                                        1, real_card)

                            for real_card in self.gamelogic.gameboard.player1_endgame:
                                if real_card.name == card.name:

                                    if self.player1_endgame.first == card and self.player1_endgame.first_target is True:
                                        self.gamelogic.stage_card_from_endgame(
                                            1, real_card)
                                        self.player1_endgame.use_card(card)
                                    if self.player1_endgame.second == card and self.player1_endgame.second_target is True:
                                        self.gamelogic.stage_card_from_endgame(
                                            1, real_card)
                                        self.player1_endgame.use_card(card)
                                    if self.player1_endgame.third == card and self.player1_endgame.third_target is True:
                                        self.gamelogic.stage_card_from_endgame(
                                            1, real_card)
                                        self.player1_endgame.use_card(card)

                        card.target = False

                        if self.player1_endgame.first == card:
                            card.x = self.gameboard_positions.player1_endgame_first.x
                            card.y = self.gameboard_positions.player1_endgame_first.y
                            self.player1_endgame.first_target = False

                        if self.player1_endgame.second == card:
                            card.x = self.gameboard_positions.player1_endgame_second.x
                            card.y = self.gameboard_positions.player1_endgame_second.y
                            self.player1_endgame.second_target = False

                        if self.player1_endgame.third == card:
                            card.x = self.gameboard_positions.player1_endgame_third.x
                            card.y = self.gameboard_positions.player1_endgame_third.y
                            self.player1_endgame.third_target = False

                    # Play_staged_cards
                    if self.gameboard_positions.playbutton.in_position(pos) and self.click == True:

                        self.click = False
                        self.gamelogic.play_staged_cards(1)
                    # Sort player hand
                    if self.gameboard_positions.sortbutton.in_position(pos):

                        self.gamelogic.sort_hand(1)
                    # Chance
                    if self.gameboard_positions.chancebutton.in_position(pos) and self.click == True:

                        self.click = False
                        self.gamelogic.chance(1)

                    # Unstage
                    if self.gameboard_positions.unstagebutton.in_position(pos):

                        self.gamelogic.unstage_cards(1)

            elif event.type == pygame.MOUSEMOTION:
                for name, card in self.album.items():
                    if card.target == True:
                        mouse_x, mouse_y = event.pos
                        card.x = mouse_x + self.offset_x
                        card.y = mouse_y + self.offset_y
                        card.cord = (card.x, card.y)

                if self.player1_final.first_target:
                    mouse_x, mouse_y = event.pos
                    self.player1_final.first_x = mouse_x + self.offset_x
                    self.player1_final.first_y = mouse_y + self.offset_y
                    card.cord = (card.x, card.y)

            if event.type == pygame.QUIT:
                return False
