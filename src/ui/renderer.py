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

    def __init__(self, display, gameboard_positions, album, user_control, gamelogic=None, gameboard=None,  player1_endgame=None, player1_final=None, player2_endgame=None, player2_final=None):
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
        self.user_control = user_control
        self.background = album.images["background"]
        self.album = album.images

        self.player1_endgame = player1_endgame
        self.player1_final = player1_final
        self.player2_endgame = player2_endgame
        self.player2_final = player2_final

        self.gamelogic = gamelogic
        self.gameboard = gameboard
        self.gameboard_positions = gameboard_positions
                
        self.gamefont = pygame.font.SysFont("Arial", 25)
        self.font_colour = (255, 243, 158)
        self.button_colour = (98, 155, 115)
        self.button_frame_colour = (80, 30, 0)
        self.background_colour = (68, 134, 90)

    def render_login(self):

        self.render_login_screen()

        pygame.display.flip()
        return

    def render_create_account(self):

        self.render_create_account_screen()

        pygame.display.flip()
        return

    def render_main_menu(self):

        self.render_main_menu_screen()
        self.render_name_box()

        pygame.display.flip()
        return

    def render_rules(self):

        self.render_rules_screen()
        self.render_rules_pages()

        pygame.display.flip()
        return  

    def render_ratingboard(self):

        self.render_ratingboard_background()
        self.render_ratingboard_statistics()

        pygame.display.flip()
        return

    def render_game(self):
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
        self.render_name_box()

        if self.gamelogic.winner != None:
            self.render_gameover_screen()

        pygame.display.flip()
        return

    def render_login_screen(self):

        self.display.fill(self.background_colour)

        login_box_colour = (80, 90, 80)
        login_box_frame_colour = (192, 192, 192)
        entry_box_colour = (192, 210, 192)
        entry_box_frame_colour = (50, 70, 50)

        # Draw login box
        self.gameboard_positions.login_box.draw_box(self.display, login_box_colour, login_box_frame_colour, 3)
        self.gameboard_positions.account_box.render(self.display)
        self.gameboard_positions.password_box.render(self.display)

        # Draw login button
        self.gameboard_positions.login_button.draw_button(self.display, 3, 25)

        # Draw create_new_account button
        self.gameboard_positions.create_new_account_button.draw_button(self.display, 3, 25)

        # Draw exitbutton
        self.gameboard_positions.exitbutton.draw_button(self.display, 3, 25)
  
    def render_create_account_screen(self):
        
        self.render_login_screen()
        
        self.gameboard_positions.create_account_box.draw_box(self.display, self.button_colour, self.button_frame_colour, 3)

        self.gameboard_positions.accountname_box.render(self.display)
        self.gameboard_positions.password_enter_box.render(self.display)
        self.gameboard_positions.password_confirmation_box.render(self.display)

        self.gameboard_positions.create_account_button.draw_button(self.display, 3, 25)
        self.gameboard_positions.cancel_button.draw_button(self.display, 3, 25)

    def render_main_menu_screen(self):

        self.display.fill(self.background_colour)

        self.gameboard_positions.play_game_button.draw_button(self.display, 3, 40)
        self.gameboard_positions.rules_button.draw_button(self.display, 3, 40)
        self.gameboard_positions.ratingboard_button.draw_button(self.display, 3, 40)

        self.gameboard_positions.exitbutton.draw_button(self.display, 3, 25)

    def render_rules_screen(self):

        self.display.fill(self.background_colour)

        self.gameboard_positions.rules_header.draw_button(self.display, 4, 40)
        self.gameboard_positions.next_button.draw_button(self.display, 3, 25)
        self.gameboard_positions.exitbutton.draw_button(self.display, 3, 25)

    def render_rules_pages(self):
        
        image1 = self.album["rule1"].image
        image2 = self.album["rule2"].image
        image3 = self.album["rule3"].image

        self.display.blit(image1, (self.gameboard_positions.rules_text1))
        self.display.blit(image2, (self.gameboard_positions.rules_text2))
        self.display.blit(image3, (self.gameboard_positions.rules_text3))

        return

    def render_base(self):
        """ This function renders the actual Gameboard (not to be confused with the class Gameboard). 
            This consists of a background colour and some lines that indicate where things should be placed.
        """

        self.display.fill(self.background_colour)
    
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
        self.gameboard_positions.exitbutton.draw_button(self.display, 3, 25)
        # Draw Play button
        self.gameboard_positions.playbutton.draw_button(self.display, 3, 25)
        # Draw Unstage butto
        self.gameboard_positions.unstagebutton.draw_button(self.display, 3, 25)
        # Draw Sort button
        self.gameboard_positions.sortbutton.draw_button(self.display, 3, 25)
        # Draw Chance button
        self.gameboard_positions.chancebutton.draw_button(self.display, 3, 25)
        # Draw Turn button
        pygame.draw.rect(self.display, (self.button_colour), (self.gameboard_positions.turnbutton.x,
                         self.gameboard_positions.turnbutton.y, self.gameboard_positions.turnbutton.width, self.gameboard_positions.turnbutton.height))
        pygame.draw.rect(self.display, (self.button_frame_colour), (self.gameboard_positions.turnbutton.x,
                         self.gameboard_positions.turnbutton.y, self.gameboard_positions.turnbutton.width, self.gameboard_positions.turnbutton.height), 3)

        turn_text = self.gamefont.render("Turn:", True, (self.font_colour))
        self.display.blit(
            turn_text, (self.gameboard_positions.turnbutton_text.coordinates))

        if self.gamelogic.turn == 1:
            whos_turn = self.gamefont.render("Player 1", True, (self.font_colour))
        else:
            whos_turn = self.gamefont.render("Player 2", True, (self.font_colour))

        self.display.blit(
            whos_turn, (self.gameboard_positions.whos_turn_text.coordinates))

        # Draw endgamebutton
        self.gameboard_positions.endgamebutton.draw_button(self.display, 3, 25)

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

    def render_player2_staged(self):
        """Renders the cards staged by player1.
        """

        if len(self.gameboard.player1_staged) > 0:
            x = self.gameboard_positions.player2_staged.x
            y = self.gameboard_positions.player2_staged.y

            for card in self.gameboard.player2_staged:
                self.display.blit(self.album[card.name].image, (x, y))
                x -= 10
                y += 10

    def render_endgame_cards(self):
        """Renders the endgamecards of player1.
        """

        if self.player1_endgame.first != False:
            card = self.player1_endgame.first.image

            if self.player1_endgame.first_target == False:
                self.display.blit(
                    card, self.gameboard_positions.player1_endgame_first.coordinates)

            else:
                card = self.album[self.player1_endgame.first.name]
                self.display.blit(card.image, (card.x, card.y))

        if self.player1_endgame.second != False:
            card = self.player1_endgame.second.image

            if self.player1_endgame.second_target == False:
                self.display.blit(
                    card, self.gameboard_positions.player1_endgame_second.coordinates)

            else:
                card = self.album[self.player1_endgame.second.name]
                self.display.blit(card.image, (card.x, card.y))

        if self.player1_endgame.third != False:
            card = self.player1_endgame.third.image

            if self.player1_endgame.third_target == False:
                self.display.blit(
                    card, self.gameboard_positions.player1_endgame_third.coordinates)

            else:
                card = self.album[self.player1_endgame.third.name]
                self.display.blit(card.image, (card.x, card.y))

        if self.player2_endgame.first != False:
            card = self.player2_endgame.first.image

            self.display.blit(
                card, self.gameboard_positions.player2_endgame_first.coordinates)

        if self.player2_endgame.second != False:
            card = self.player2_endgame.second.image

            self.display.blit(
                card, self.gameboard_positions.player2_endgame_second.coordinates)

        if self.player2_endgame.third != False:
            card = self.player2_endgame.third.image

            self.display.blit(
                card, self.gameboard_positions.player2_endgame_third.coordinates)

    def render_name_box(self):

        self.gameboard_positions.name_box.draw_button(self.display, 3, 30)

    def render_gameover_screen(self):

        login_box_colour = (80, 90, 80)
        login_box_frame_colour = (192, 192, 192)
        
        self.gameboard_positions.gameover_box.draw_box(self.display, login_box_colour, login_box_frame_colour, 4)
        self.gameboard_positions.exitbutton2.draw_button(self.display, 3, 25)
        self.gameboard_positions.play_again_button.draw_button(self.display, 3, 25)

        self.gameboard_positions.winner_button.text = f"Winner: Player{self.gamelogic.winner}"
        self.gameboard_positions.winner_button.draw_button(self.display, 3, 35)

    def render_ratingboard_background(self):

        login_box_colour = (80, 90, 80)
        login_box_frame_colour = (192, 192, 192)

        self.display.fill(self.background_colour)
        
        self.gameboard_positions.login_box.draw_box(self.display, login_box_colour, login_box_frame_colour, 3)
        self.gameboard_positions.exitbutton.draw_button(self.display, 3, 25)
        self.gameboard_positions.ratingboard_header.draw_button(self.display, 4, 35)

    def render_ratingboard_statistics(self):

        top_ten = self.user_control.get_top_ten()

        number_coord = self.gameboard_positions.top_ten_number
        username_coord = self.gameboard_positions.top_ten_name
        rating_coord = self.gameboard_positions.top_ten_rating

        font = pygame.font.SysFont("Arial", 25)
        font_colour = (255, 243, 158)
        
        number = 1

        for item in top_ten:

            username = str(item.username)
            user_rating = str(item.rating)
            number_text = str(number)+"."

            number_text2 = font.render(number_text, True, font_colour)
            self.display.blit(number_text2, (number_coord))

            name = font.render(username, True, font_colour)
            self.display.blit(name, (username_coord))

            rating = font.render(user_rating, True, font_colour)
            self.display.blit(rating, (rating_coord))

            number_coord = (number_coord[0], number_coord[1]+30)
            username_coord = (username_coord[0], username_coord[1]+30)
            rating_coord = (rating_coord[0], rating_coord[1]+30)

            number += 1


        return