import pygame
import ui.scaled.scaling
from ui.load_images import load_image
from ui.scaled.card_pictures import CardPics
from ui.scaled.scaling import PlayButton
class Renderer:

    def __init__(self, display, gameboard, gameboard_positions, card_pics, player1_endgame, player1_final, player2_endgame, player2_final):

        self.display = display
        self.background_pic = ui.scaled.scaling.Background()
        self.play_button = PlayButton()
        self.card_pics = card_pics
      
        self.player1_endgame = player1_endgame
        self.player1_final = player1_final
        self.player2_endgame = player2_endgame
        self.player2_final = player2_final
    
        self.gameboard = gameboard
        self.gameboard_positions = gameboard_positions

    def render(self):

        self.render_background()
        self.render_reserve_deck()
        self.render_field_deck()
        self.render_player1_staged()
        self.render_finalcards()
        self.render_endgame_cards()
        self.render_player1_hand()
        self.render_player2_hand()


        pygame.display.flip()
        return

    def render_background(self):

        self.display.fill((51,102,0))

        #Draw player1_stage_position
        pygame.draw.rect(self.display, (255, 255, 255), (805, 485, 90, 125), 1)
        #Draw player2_stage_position
        pygame.draw.rect(self.display, (255, 255, 255), (875, 375, 90, 125), 1)
        #Draw green rec to block stage squares from vision
        pygame.draw.rect(self.display, (51, 102, 0), (840, 430, 90, 125))
        #Draw field_deck_position
        pygame.draw.rect(self.display, (255, 255, 255), (840, 430, 90, 125), 2)

        self.display.blit(self.play_button.image, (self.gameboard_positions.play_button_cord))
        

    def render_reserve_deck(self):

        #render reserve_deck
        if len(self.gameboard.reserve_deck) > 0:
            reserve_deck = pygame.transform.rotate(self.card_pics["cardback"].image, 90)
            self.display.blit(reserve_deck, (450, 450))

    def render_finalcards(self):

        if self.player1_final.first:
            self.display.blit(self.card_pics["cardback"].image, self.player1_final.first_cordinates)

        if self.player1_final.second:
            self.display.blit(self.card_pics["cardback"].image, self.player1_final.second_cordinates)
        
        if self.player1_final.third:
            self.display.blit(self.card_pics["cardback"].image, self.player1_final.third_cordinates)

        if self.player2_final.first:
            self.display.blit(self.card_pics["cardback"].image, self.player2_final.first_cordinates)

        if self.player2_final.second:
            self.display.blit(self.card_pics["cardback"].image, self.player2_final.second_cordinates)
        
        if self.player2_final.third:
            self.display.blit(self.card_pics["cardback"].image, self.player2_final.third_cordinates)

    def render_player1_hand(self):

        x = (self.background_pic.width/2)-(len(self.gameboard.player1_hand))*50
        y = (self.background_pic.height-200)

        for card in self.gameboard.player1_hand:
            if self.card_pics[card.name].target == False:
                self.display.blit(self.card_pics[card.name].image, (x, y))
                self.card_pics[card.name].x = x
                self.card_pics[card.name].y = y
                self.card_pics[card.name].cord = (x,y)

                x += 100
                if x > 3000:
                    x = 0.3*self.background_pic.width
                    y = 0.8*self.background_pic.height
                continue
            x += 100
            self.display.blit(self.card_pics[card.name].image, (self.card_pics[card.name].x, self.card_pics[card.name].y))

    def render_player2_hand(self):

        x = (self.background_pic.width/2)-(len(self.gameboard.player2_hand))*50
        y = 20

        for card in self.gameboard.player2_hand:
            self.display.blit(self.card_pics[card.name].image, (x, y))
            self.card_pics[card.name].x = x
            self.card_pics[card.name].y = y
            self.card_pics[card.name].cord = (x,y)

            x += 100
            if x > 3000:
                x = 0.3*self.background_pic.width
                y = 0.8*self.background_pic.height

    def render_field_deck(self):

        

        if len(self.gameboard.field_deck) > 0:
            top_card = self.card_pics[self.gameboard.field_deck[-1].name].image
            self.display.blit(top_card, (845, 435))

    def render_player1_staged(self):
        
        if len(self.gameboard.player1_staged) > 0:
            x = self.gameboard_positions.player1_stage_x
            y = self.gameboard_positions.player1_stage_y

            for card in self.gameboard.player1_staged:
                self.display.blit(self.card_pics[card.name].image, (x, y))
                x -= 10
                y += 10


    def render_endgame_cards(self):

        if self.player1_endgame.first != False:
            card = self.player1_endgame.first.image

            self.display.blit(card, self.player1_endgame.first_cordinates)


        if self.player1_endgame.second != False:
            card = self.player1_endgame.second.image

            self.display.blit(card, self.player1_endgame.second_cordinates)

        if self.player1_endgame.third != False:
            card = self.player1_endgame.third.image

            self.display.blit(card, self.player1_endgame.third_cordinates)