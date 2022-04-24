import pygame
import ui.pictures.pictures
from ui.pictures.load_images import load_image
from ui.pictures.album import Album


class Renderer:

    def __init__(self, display, gameboard, gameboard_positions, album, player1_endgame, player1_final, player2_endgame, player2_final):

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

        gamefont = pygame.font.SysFont("Arial", 25)
        font_colour = (255, 243, 158)
        button_colour = (98, 155, 115)
        button_frame_colour = (80, 30, 0)
        background_colour = (68, 134, 90)

        self.display.fill(background_colour)

        # Draw reserve_deck_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.reserve_deck_frame_x,
                         self.gameboard_positions.reserve_deck_frame_y, 125, 90), 2)
        # Draw player1_stage_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.player1_stage_frame_x,
                         self.gameboard_positions.player1_stage_frame_y, 95, 125), 1)
        # Draw player2_stage_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.player2_stage_frame_x,
                         self.gameboard_positions.player2_stage_frame_y, 95, 125), 1)
        # Draw green rec to block stage squares from vision
        pygame.draw.rect(self.display, (70, 135, 94), (self.gameboard_positions.field_deck_frame_x,
                         self.gameboard_positions.field_deck_frame_y, 95, 125))
        # Draw field_deck_frame
        pygame.draw.rect(self.display, (255, 255, 255), (self.gameboard_positions.field_deck_frame_x,
                         self.gameboard_positions.field_deck_frame_y, 95, 125), 2)

        # Draw Exit button
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.exitbutton_x,
                         self.gameboard_positions.exitbutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.exitbutton_x,
                         self.gameboard_positions.exitbutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height), 3)
        exit_text = gamefont.render("Exit", True, (font_colour))
        self.display.blit(exit_text, (self.gameboard_positions.exit_text_cord))
        # Draw Play button
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.playbutton_x,
                         self.gameboard_positions.playbutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.playbutton_x,
                         self.gameboard_positions.playbutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height), 3)
        play_text = gamefont.render("Play", True, (font_colour))
        self.display.blit(play_text, (self.gameboard_positions.play_text_cord))
        # Draw Unstage button
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.unstagebutton_x,
                         self.gameboard_positions.unstagebutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.unstagebutton_x,
                         self.gameboard_positions.unstagebutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height), 3)
        unstage_text = gamefont.render("Unstage", True, (font_colour))
        self.display.blit(
            unstage_text, (self.gameboard_positions.unstage_text_cord))
        # Draw Sort button
        pygame.draw.rect(self.display, (button_colour), (self.gameboard_positions.sortbutton_x,
                         self.gameboard_positions.sortbutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height))
        pygame.draw.rect(self.display, (button_frame_colour), (self.gameboard_positions.sortbutton_x,
                         self.gameboard_positions.sortbutton_y, self.gameboard_positions.button_width, self.gameboard_positions.button_height), 3)
        sort_text = gamefont.render("Sort", True, (font_colour))
        self.display.blit(sort_text, (self.gameboard_positions.sort_text_cord))

    def render_reserve_deck(self):

        # render reserve_deck
        if len(self.gameboard.reserve_deck) > 0:
            reserve_deck = pygame.transform.rotate(
                self.album["cardback"].image, 90)
            self.display.blit(
                reserve_deck, (self.gameboard_positions.reserve_deck_cord))

    def render_finalcards(self):

        if self.player1_final.first:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player1_final_first_cord)

        if self.player1_final.second:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player1_final_second_cord)

        if self.player1_final.third:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player1_final_third_cord)

        if self.player2_final.first:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player2_final_first_cord)

        if self.player2_final.second:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player2_final_second_cord)

        if self.player2_final.third:
            self.display.blit(
                self.album["cardback"].image, self.gameboard_positions.player2_final_third_cord)

    def render_player1_hand(self):

        card_index = 0

        for card in self.gameboard.player1_hand:

            self.display.blit(self.album[card.name].image, (
                self.gameboard_positions.decide_player1_hand_card_position(card, card_index)))

            card_index += 1

    def render_player2_hand(self):

        card_index = 0

        for card in self.gameboard.player2_hand:

            self.display.blit(self.album[card.name].image, (
                self.gameboard_positions.decide_player2_hand_card_position(card, card_index)))

            card_index += 1

    def render_field_deck(self):

        if len(self.gameboard.field_deck) > 0:
            top_card = self.album[self.gameboard.field_deck[-1].name].image
            self.display.blit(
                top_card, (self.gameboard_positions.field_deck_cord))

    def render_player1_staged(self):

        if len(self.gameboard.player1_staged) > 0:
            x = self.gameboard_positions.player1_stage_x
            y = self.gameboard_positions.player1_stage_y

            for card in self.gameboard.player1_staged:
                self.display.blit(self.album[card.name].image, (x, y))
                x -= 10
                y += 10

    def render_endgame_cards(self):

        if self.player1_endgame.first != False:
            card = self.player1_endgame.first.image

            self.display.blit(
                card, self.gameboard_positions.player1_endgame_first_cord)

        if self.player1_endgame.second != False:
            card = self.player1_endgame.second.image

            self.display.blit(
                card, self.gameboard_positions.player1_endgame_second_cord)

        if self.player1_endgame.third != False:
            card = self.player1_endgame.third.image

            self.display.blit(
                card, self.gameboard_positions.player1_endgame_third_cord)
