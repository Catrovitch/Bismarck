class GameboardPositions:

    def __init__(self, card_width, card_height):

        self.card_width = card_width
        self.card_height = card_height

        self.reserve_deck_x = ""
        self.reserve_deck_y = ""
        self.reserve_deck_cord = (self.reserve_deck_x, self.reserve_deck_y)

        self.field_deck_x = ""
        self.field_deck_y = ""
        self.field_deck_cord = (self.field_deck_x, self.field_deck_y)

        self.player1_stage_x = 810
        self.player1_stage_y = 490
        self.player1_stage_cord = (self.player1_stage_x, self.player1_stage_y)

        self.player2_stage_x = ""
        self.player2_stage_y = ""
        self.player2_stage_cord = (self.player2_stage_x, self.player2_stage_y)
        
        #Player1 endgame first, second, third
        self.player1_endgame_first_x = 750
        self.player1_endgame_first_y = 635
        self.player1_endgame_first_cord = (self.player1_endgame_first_x, self.player1_endgame_first_y)

        self.player1_endgame_second_x = 850
        self.player1_endgame_second_y = 635
        self.player1_endgame_second_cord = (self.player1_endgame_second_x, self.player1_endgame_second_y)

        self.player1_endgame_third_x = 950
        self.player1_endgame_third_y = 635
        self.player1_endgame_third_cord = (self.player1_endgame_third_x, self.player1_endgame_third_y)

        #Player2 endgame first, second, third
        self.player2_endgame_first_x = 200
        self.player2_endgame_first_y = 380
        self.player2_endgame_first_cord = (self.player2_endgame_first_x, self.player2_endgame_first_y)

        self.player2_endgame_second_x = 300
        self.player2_endgame_second_y = 380
        self.player2_endgame_second_cord = (self.player2_endgame_second_x, self.player2_endgame_second_y)

        self.player2_endgame_third_x = 400
        self.player2_endgame_third_y = 380
        self.player21_endgame_third_cord = (self.player2_endgame_third_x, self.player2_endgame_third_y)

        #Player1 final first, second, third
        self.player1_final_first_x = 750
        self.player1_final_first_y = 650
        self.player1_final_first_cord = (self.player1_final_first_x, self.player1_final_first_y)

        self.player1_final_second_x = 850
        self.player1_final_second_y = 650
        self.player1_final_second_cord = (self.player1_final_second_x, self.player1_final_second_y)

        self.player1_final_third_x = 950
        self.player1_final_third_y = 650
        self.player1_final_third_cord = (self.player1_final_third_x, self.player1_final_third_y)

        #Player2 final first, second, third
        self.player2_final_first_x = 750
        self.player2_final_first_y = 150
        self.player2_final_first_cord = (self.player2_final_first_x, self.player2_final_first_y)

        self.player2_final_second_x = 850
        self.player2_final_second_y = 150
        self.player2_final_second_cord = (self.player2_final_second_x, self.player2_final_second_y)

        self.player2_final_third_x = 950
        self.player2_final_third_y = 150
        self.player2_final_third_cord = (self.player2_final_third_x, self.player2_final_third_y)


        self.player1_hand_x = ""
        self.player1_hand_y = ""
        self.player1_hand_cord = (self.player1_hand_x, self.player1_hand_y)

        self.player2_hand_x = ""
        self.player2_hand_y = ""
        self.player2_hand_cord = (self.player2_hand_x, self.player2_hand_y)

        self.play_button_x = 879
        self.play_button_y = 505
        self.play_button_cord = (self.play_button_x, self.play_button_y)

    def player1_stage(self, position):

        if self.player1_stage_x <= position[0] <= self.player1_stage_x+self.card_width and self.player1_stage_y <= position[1] <= self.player1_stage_y + self.card_height:
            return True
        
        return False

    def play_button(self, position):

        if self.play_button_x <= position[0] <= self.play_button_x+self.card_width and self.play_button_y <= position[1] <= self.play_button_y+self.card_height:
            return True
        
        return False

    def player1_endgame_first(self, position):

        if self.player1_final_first_x <= position[0] <= self.player1_final_first_x + self.card_width and self.player1_final_first_y <= position[1] <= self.player1_final_first_y+ self.card_height:
            return True

        return False

    def player1_endgame_second(self, position):

        if self.player1_final_second_x <= position[0] <= self.player1_final_second_x + self.card_width and self.player1_final_second_y <= position[1] <= self.player1_final_second_y+ self.card_height:
            return True

        return False

    def player1_endgame_third(self, position):

        if self.player1_final_third_x <= position[0] <= self.player1_final_third_x + self.card_width and self.player1_final_third_y <= position[1] <= self.player1_final_third_y+ self.card_height:
            return True

        return False
