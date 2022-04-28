import pygame

class Renderer:

    """The Renderer class handles all rendering in the program.

    Attributes:
        display: instance pygame display
        background: Picture class object "background"
        album: instance of class Album shared across multiply classes in the architecture as a whole.
        player1_endgame: instance of class Endgame corresponding to player1.
        player1_final: instance of class Finalcards corresponding to player1.
        player2_endgame: instance of class Endgame corresponding to player2.
        player2_final: instance of class Finalcards corresponding to player2.
        gameboard: instance of class Gameboard.
        gameboard_positions: instance of class GameboardPositions.
    """

    def __init__(self, display, gameboard, gameboard_positions, album, player1_endgame, player1_final, player2_endgame, player2_final):

        """The constructor of the class. 

        Args:
            display: instance pygame display
            background: Picture class object "background"
            album: instance of class Album shared across multiply classes in the architecture as a whole.
            player1_endgame: instance of class Endgame corresponding to player1.
            player1_final: instance of class Finalcards corresponding to player1.
            player2_endgame: instance of class Endgame corresponding to player2.
            player2_final: instance of class Finalcards corresponding to player2.
            gameboard: instance of class Gameboard.
            gameboard_positions: instance of class GameboardPositions.
        """
        pygame.init()
        self.display = display
        self.background = album.images["background"]
        self.album = album.images

        self.player1_endgame = player1_endgame
        self.player1_final = player1_final
        self.player2_endgame = player2_endgame
        self.player2_final = player2_final

        self.gameboard = gameboard
        self.gameboard_positions = gameboard_positions

    def render(self):

        """This function calls on all that shall be rendered.
        """

        self.render_base()
        self.render_reserve_deck()
        self.render_field_deck()
        self.render_player1_staged()
        self.render_finalcards()
        self.render_endgame_cards()
        self.render_player1_hand()
        self.render_player2_hand()

        pygame.display.flip()
        return

    def render_base(self):

        """ This function renders the actual Gameboard (not to be confused with the class Gameboard). 
            This consists of a background colour and some lines that indicate where things should be placed.
        """

        gamefont = pygame.font.SysFont("Arial", 25)
        font_colour = (255, 243, 158)
        button_colour = (98, 155, 115)
        button_frame_colour = (80, 30, 0)
        background_colour = (68, 134, 90)

        self.display.fill(background_colour)

        # Draw reserve_deck_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.reserve_deck_frame.x,
                         self.gameboard_positions.reserve_deck_frame.y, self.gameboard_positions.reserve_deck_frame.width, self.gameboard_positions.reserve_deck_frame.height), 2)
        # Draw player1_stage_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.player1_stage_frame.x,
                         self.gameboard_positions.player1_stage_frame.y, self.gameboard_positions.player1_stage_frame.width, self.gameboard_positions.player1_stage_frame.height), 1)
        # Draw player2_stage_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.player2_stage_frame.x,
                         self.gameboard_positions.player2_stage_frame.y, self.gameboard_positions.player2_stage_frame.width, self.gameboard_positions.player2_stage_frame.height), 1)
        # Draw green rec to block stage squares from vision
        pygame.draw.rect(self.display, (70, 135, 94), (self.gameboard_positions.field_deck_frame.x,
                         self.gameboard_positions.field_deck_frame.y, self.gameboard_positions.field_deck_frame.width, self.gameboard_positions.field_deck_frame.height))
        # Draw field_deck_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.field_deck_frame.x,
                         self.gameboard_positions.field_deck_frame.y, self.gameboard_positions.field_deck_frame.width, self.gameboard_positions.field_deck_frame.height), 2)

        # Draw Exit button
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.exitbutton.x,
                         self.gameboard_positions.exitbutton.y, self.gameboard_positions.exitbutton.width, self.gameboard_positions.exitbutton.height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.exitbutton.x,
                         self.gameboard_positions.exitbutton.y, self.gameboard_positions.exitbutton.width, self.gameboard_positions.exitbutton.height), 3)
        exit_text = gamefont.render("Exit", True, (font_colour))
        self.display.blit(exit_text, (self.gameboard_positions.exitbutton_text.coordinates))
        # Draw Play button
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.playbutton.x,
                         self.gameboard_positions.playbutton.y, self.gameboard_positions.playbutton.width, self.gameboard_positions.playbutton.height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.playbutton.x,
                         self.gameboard_positions.playbutton.y, self.gameboard_positions.playbutton.width, self.gameboard_positions.playbutton.height), 3)
        play_text = gamefont.render("Play", True, (font_colour))
        self.display.blit(play_text, (self.gameboard_positions.playbutton_text.coordinates))
        # Draw Unstage butto
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.unstagebutton.x,
                         self.gameboard_positions.unstagebutton.y, self.gameboard_positions.unstagebutton.width, self.gameboard_positions.unstagebutton.height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.unstagebutton.x,
                         self.gameboard_positions.unstagebutton.y, self.gameboard_positions.unstagebutton.width, self.gameboard_positions.unstagebutton.height), 3)
        unstage_text = gamefont.render("Unstage", True, (font_colour))
        self.display.blit(
            unstage_text, (self.gameboard_positions.unstagebutton_text.coordinates))
        # Draw Sort button
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.sortbutton.x,
                         self.gameboard_positions.sortbutton.y, self.gameboard_positions.sortbutton.width, self.gameboard_positions.sortbutton.height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.sortbutton.x,
                         self.gameboard_positions.sortbutton.y, self.gameboard_positions.sortbutton.width, self.gameboard_positions.sortbutton.height), 3)
        sort_text = gamefont.render("Sort", True, (font_colour))
        self.display.blit(sort_text, (self.gameboard_positions.sortbutton_text.coordinates))

    def render_reserve_deck(self):

        """Renders the field_deck.
        """
        if len(self.gameboard.reserve_deck) > 0:
            reserve_deck = pygame.transform.rotate(
                self.album["cardback"].image, 90)
            self.display.blit(
                reserve_deck, (self.gameboard_positions.reserve_deck.coordinates))

    def render_finalcards(self):

        """Renders the finalcards of player1 and player2 if they are in place"""

        if self.player1_final.first:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player1_final_first.coordinates)

        if self.player1_final.second:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player1_final_second.coordinates)

        if self.player1_final.third:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player1_final_third.coordinates)

        if self.player2_final.first:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player2_final_first.coordinates)

        if self.player2_final.second:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player2_final_second.coordinates)

        if self.player2_final.third:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player2_final_third.coordinates)

    def render_player1_hand(self):

        """Renders the cards in held in the hand of player1. (attriute "player1_hand" in Gameboard class)
        """
        card_index = 0

        for card in self.gameboard.player1_hand:

            self.display.blit(self.album[card.name].image, (
                self.gameboard_positions.decide_player1_hand_card_position(card, card_index)))

            card_index += 1

    def render_player2_hand(self):

        """Renders the cards held in the hand of player2. (attribute "player2_hand" in Gameboard class)"""
        card_index = 0

        for card in self.gameboard.player2_hand:

            self.display.blit(self.album[card.name].image, (
                self.gameboard_positions.decide_player2_hand_card_position(card, card_index)))

            card_index += 1

    def render_field_deck(self):

        """Renders the field_deck
        """

        if len(self.gameboard.field_deck) > 0:
            top_card = self.album[self.gameboard.field_deck[-1].name].image
            self.display.blit(
                top_card, (self.gameboard_positions.field_deck.coordinates))

    def render_player1_staged(self):

        """Renders the cards staged by player1.
        """

        if len(self.gameboard.player1_staged) > 0:
            x = self.gameboard_positions.player1_staged.x
            y = self.gameboard_positions.player1_staged.y

            for card in self.gameboard.player1_staged:
                self.display.blit(self.album[card.name].image, (x, y))
                x -= 10
                y += 10

    def render_endgame_cards(self):

        """Renders the endgamecards of player1.
        """

        if self.player1_endgame.first != False:
            card = self.player1_endgame.first.image

            self.display.blit(
                card, self.gameboard_positions.player1_endgame_first.coordinates)

        if self.player1_endgame.second != False:
            card = self.player1_endgame.second.image

            self.display.blit(
                card, self.gameboard_positions.player1_endgame_second.coordinates)

        if self.player1_endgame.third != False:
            card = self.player1_endgame.third.image

            self.display.blit(
                card, self.gameboard_positions.player1_endgame_third.coordinates)
