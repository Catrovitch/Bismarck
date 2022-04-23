import pygame

class Game:

    def __init__(self, gamelogic, gameboard_positions, player1, player2, renderer, card_pics, eventqueue, clock, player1_endgame, player1_final, player2_endgame, player2_final):

        self.gamelogic = gamelogic
        self.gameboard_positions = gameboard_positions

        self.player1 = player1
        self.player2 = player2
        
        self.renderer = renderer
        self.card_pics = card_pics
        self.eventqueue = eventqueue
        self.clock = clock

        self.player1_endgame = player1_endgame
        self.player1_final = player1_final
        self.player2_endgame = player2_endgame
        self.player2_final = player2_final
        
        self.target = None

        self.game_begun = False

        self.initial_deal()
        self.gameloop()

    def initial_deal(self):

        self.gamelogic.initial_deal()
        
        dealt = 0

        while dealt < 3:
            dealt += 1
            self.player1_final.add_card()
            self.player2_final.add_card()

    def gameloop(self):

        while True:

            if self.handle_events() is False:
                break

            self.renderer.render()

            self.clock.tick(60)

    def handle_events(self):

        for event in self.eventqueue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                pos = pygame.mouse.get_pos()
                for name, card in self.card_pics.items():
                    if card.x <= pos[0] <= card.x+card.width and card.y <= pos[1] <= card.y + card.height:
                        card.target = True
                        mouse_x, mouse_y = event.pos
                        self.offset_x = card.x - mouse_x
                        self.offset_y = card.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for name, card in self.card_pics.items():
                        
                        #Choose first endgame card
                        if card.target == True and self.player1_endgame.first == False and self.gameboard_positions.player1_endgame_first(pos):
                            
                            self.player1_endgame.add_card(card, "first")
                            self.player1_endgame.first = card
                            for real_card in self.gamelogic.gameboard.player1_hand:

                                if real_card.name == card.name:

                                    self.gamelogic.choose_endgame_cards(1, real_card)
                                    card.target = False
                                    if self.player1_endgame.first and self.player1_endgame.second and self.player1_endgame.third:
                                        self.game_begun = True
                                    return

                        #Choose second endgame card
                        if card.target == True and self.player1_endgame.second == False and self.gameboard_positions.player1_endgame_second(pos):
                            
                            self.player1_endgame.add_card(card, "second")
                            self.player1_endgame.second = card
                            for real_card in self.gamelogic.gameboard.player1_hand:
                                if real_card.name == card.name:
    
                                    self.gamelogic.choose_endgame_cards(1, real_card)
                                    card.target = False
                                    if self.player1_endgame.first and self.player1_endgame.second and self.player1_endgame.third:
                                        self.game_begun = True
                                    return
                        
                        #Choose third endgame card
                        if card.target == True and self.player1_endgame.third == False and self.gameboard_positions.player1_endgame_third(pos):
                            
                            self.player1_endgame.add_card(card, "third")
                            self.player1_endgame.third = card
                            for real_card in self.gamelogic.gameboard.player1_hand:
                                if real_card.name == card.name:
    
                                    self.gamelogic.choose_endgame_cards(1, real_card)
                                    card.target = False
                                    if self.player1_endgame.first and self.player1_endgame.second and self.player1_endgame.third:
                                        self.game_begun = True
                                    return
                        
                        #Stage a card
                        if card.target == True and self.gameboard_positions.player1_stage(pos) and self.game_begun == True:

                            for real_card in self.gamelogic.gameboard.player1_hand:
                                if real_card.name == card.name:                          
                                    self.gamelogic.stage_card_from_hand(1, real_card)

                        card.target = False

                        #Play_staged_cards
                        if self.gameboard_positions.play_button(pos):

                            self.gamelogic.play_staged_cards(1)


            
            elif event.type == pygame.MOUSEMOTION:
                for name, card in self.card_pics.items():
                    if card.target == True:
                        mouse_x, mouse_y = event.pos
                        card.x = mouse_x + self.offset_x
                        card.y = mouse_y + self.offset_y
                        card.cord = (card.x, card.y)

            if event.type == pygame.QUIT:
                return False
