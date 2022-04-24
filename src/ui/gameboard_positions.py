class GameboardPositions:

    def __init__(self, gameboard, album, display_size, card_width, card_height):

        self.gameboard = gameboard
        self.album = album.images

        # Dimensions
        self.display_size = display_size
        self.card_width = card_width
        self.card_height = card_height

        # Reserve_deck position
        self.reserve_deck_x = (self.display_size.width/4)-(self.card_height/2)
        self.reserve_deck_y = (self.display_size.height/2)-(self.card_width/2)
        self.reserve_deck_cord = (self.reserve_deck_x, self.reserve_deck_y)

        # Field_deck position
        self.field_deck_x = (self.display_size.width/2)-(self.card_width/2)
        self.field_deck_y = (self.display_size.height/2)-(self.card_height/2)
        self.field_deck_cord = (self.field_deck_x, self.field_deck_y)

        # Player1 stage position
        self.player1_stage_x = self.field_deck_x - self.card_width*0.7
        self.player1_stage_y = self.field_deck_y + self.card_height*0.7
        self.player1_stage_cord = (self.player1_stage_x, self.player1_stage_y)

        # Player2 stage position
        self.player2_stage_x = self.field_deck_x + self.card_width*0.7
        self.player2_stage_y = self.field_deck_y - self.card_height*0.7
        self.player2_stage_cord = (self.player2_stage_x, self.player2_stage_y)

        # Player1 endgame first, second, third
        self.player1_endgame_second_x = self.display_size.width/2-self.card_width/2
        self.player1_endgame_second_y = self.player1_stage_y + self.card_height*1.5
        self.player1_endgame_second_cord = (
            self.player1_endgame_second_x, self.player1_endgame_second_y)

        self.player1_endgame_first_x = self.player1_endgame_second_x - self.card_width*1.5
        self.player1_endgame_first_y = self.player1_endgame_second_y
        self.player1_endgame_first_cord = (
            self.player1_endgame_first_x, self.player1_endgame_first_y)

        self.player1_endgame_third_x = self.player1_endgame_second_x + self.card_width*1.5
        self.player1_endgame_third_y = self.player1_endgame_second_y
        self.player1_endgame_third_cord = (
            self.player1_endgame_third_x, self.player1_endgame_third_y)

        # Player2 endgame first, second, third
        self.player2_endgame_second_x = self.player1_endgame_second_x
        self.player2_endgame_second_y = self.player2_stage_y - self.card_height*2
        self.player2_endgame_second_cord = (
            self.player2_endgame_second_x, self.player2_endgame_second_y)

        self.player2_endgame_first_x = self.player2_endgame_second_x - self.card_width*1.5
        self.player2_endgame_first_y = self.player2_endgame_second_y
        self.player2_endgame_first_cord = (
            self.player2_endgame_first_x, self.player2_endgame_first_y)

        self.player2_endgame_third_x = self.player2_endgame_second_x + self.card_width*1.5
        self.player2_endgame_third_y = self.player2_endgame_first_y
        self.player21_endgame_third_cord = (
            self.player2_endgame_third_x, self.player2_endgame_third_y)

        # Player1 final first, second, third
        self.player1_final_first_x = self.player1_endgame_first_x
        self.player1_final_first_y = self.player1_endgame_first_y + self.card_height*0.2
        self.player1_final_first_cord = (
            self.player1_final_first_x, self.player1_final_first_y)

        self.player1_final_second_x = self.player1_endgame_second_x
        self.player1_final_second_y = self.player1_final_first_y
        self.player1_final_second_cord = (
            self.player1_final_second_x, self.player1_final_second_y)

        self.player1_final_third_x = self.player1_endgame_third_x
        self.player1_final_third_y = self.player1_final_first_y
        self.player1_final_third_cord = (
            self.player1_final_third_x, self.player1_final_third_y)

        # Player2 final first, second, third
        self.player2_final_first_x = self.player2_endgame_first_x
        self.player2_final_first_y = self.player2_endgame_first_y - self.card_height*0.2
        self.player2_final_first_cord = (
            self.player2_final_first_x, self.player2_final_first_y)

        self.player2_final_second_x = self.player2_endgame_second_x
        self.player2_final_second_y = self.player2_final_first_y
        self.player2_final_second_cord = (
            self.player2_final_second_x, self.player2_final_second_y)

        self.player2_final_third_x = self.player2_endgame_third_x
        self.player2_final_third_y = self.player2_final_first_y
        self.player2_final_third_cord = (
            self.player2_final_third_x, self.player2_final_third_y)

        # Player hand mid card position
        self.player1_hand_mid_card_x = self.display_size.width/2
        self.player1_hand_mid_card_y = self.display_size.height-self.card_height*1.1
        self.player1_hand_mid_card_cord = (
            self.player1_hand_mid_card_x, self.player1_hand_mid_card_y)

        self.player2_hand_mid_card_x = self.display_size.width/2
        self.player2_hand_mid_card_y = self.card_height*0.1
        self.player2_hand_mid_card_cord = (
            self.player2_hand_mid_card_x, self.player2_hand_mid_card_y)

        # Gameboard graphics
        self.reserve_deck_frame_x = self.reserve_deck_x - self.card_height*0.05
        self.reserve_deck_frame_y = self.reserve_deck_y - self.card_width*0.10
        self.reserve_deck_frame_cord = (
            self.reserve_deck_frame_x, self.reserve_deck_frame_y)

        self.field_deck_frame_x = self.field_deck_x - self.card_width*0.10
        self.field_deck_frame_y = self.field_deck_y - self.card_height*0.05
        self.field_deck_frame_cord = (
            self.field_deck_frame_x, self.field_deck_frame_y)

        self.player1_stage_frame_x = self.player1_stage_x - self.card_width*0.10
        self.player1_stage_frame_y = self.player1_stage_y - self.card_height*0.05
        self.player1_stage_frame_cord = (
            self.player1_stage_frame_x, self.player1_stage_frame_y)

        self.player2_stage_frame_x = self.player2_stage_x - self.card_width*0.10
        self.player2_stage_frame_y = self.player2_stage_y - self.card_height*0.05
        self.player2_stage_frame_cord = (
            self.player2_stage_frame_x, self.player2_stage_frame_y)

        self.button_width = self.card_width*1.5
        self.button_height = self.card_height/2.8

        self.playbutton_x = self.player1_stage_x + self.card_width + 10
        self.playbutton_y = self.player1_stage_y + self.card_width - 10
        self.playbutton_cord = (self.playbutton_x, self.playbutton_y)

        self.play_text_x = self.playbutton_x + 40
        self.play_text_y = self.playbutton_y + 10
        self.play_text_cord = (self.play_text_x, self.play_text_y)

        self.exitbutton_x = self.card_width/3
        self.exitbutton_y = self.display_size.height - self.card_width/1.5
        self.exitbutton_cord = (self.exitbutton_x, self.exitbutton_y)

        self.exit_text_x = self.exitbutton_x + 40
        self.exit_text_y = self.exitbutton_y + 10
        self.exit_text_cord = (self.exit_text_x, self.exit_text_y)

        self.unstagebutton_x = self.player1_stage_frame_x - self.button_width*1.05
        self.unstagebutton_y = self.playbutton_y
        self.unstagebutton_cord = (self.unstagebutton_x, self.unstagebutton_y)

        self.unstage_text_x = self.unstagebutton_x + 10
        self.unstage_text_y = self.unstagebutton_y + 10
        self.unstage_text_cord = (self.unstage_text_x, self.unstage_text_y)

        self.sortbutton_x = self.display_size.width - \
            self.exitbutton_x - self.button_width
        self.sortbutton_y = self.exitbutton_y
        self.sortbutton_cord = (self.sortbutton_x, self.sortbutton_y)

        self.sort_text_x = self.sortbutton_x + 40
        self.sort_text_y = self.sortbutton_y + 10
        self.sort_text_cord = (self.sort_text_x, self.sort_text_y)

    def player1_stage(self, position):

        if self.player1_stage_x <= position[0] <= self.player1_stage_x+self.card_width and self.player1_stage_y <= position[1] <= self.player1_stage_y + self.card_height:
            return True

        return False

    def player1_endgame_first(self, position):

        if self.player1_final_first_x <= position[0] <= self.player1_final_first_x + self.card_width and self.player1_final_first_y <= position[1] <= self.player1_final_first_y + self.card_height:
            return True

        return False

    def player1_endgame_second(self, position):

        if self.player1_final_second_x <= position[0] <= self.player1_final_second_x + self.card_width and self.player1_final_second_y <= position[1] <= self.player1_final_second_y + self.card_height:
            return True

        return False

    def player1_endgame_third(self, position):

        if self.player1_final_third_x <= position[0] <= self.player1_final_third_x + self.card_width and self.player1_final_third_y <= position[1] <= self.player1_final_third_y + self.card_height:
            return True

        return False

    def decide_player1_hand_card_position(self, card, card_index):

        ui_card = self.album[card.name]

        if ui_card.target == False:

            ui_card.x = ((self.player1_hand_mid_card_x) -
                         (len(self.gameboard.player1_hand)/2)*self.card_width)+(100*card_index)
            ui_card.y = (self.player1_hand_mid_card_y)

            return (ui_card.x, ui_card.y)

        return (ui_card.x, ui_card.y)

    def decide_player2_hand_card_position(self, card, card_index):

        ui_card = self.album[card.name]

        if ui_card.target == False:

            x = ((self.player2_hand_mid_card_x) -
                 (len(self.gameboard.player2_hand)/2)*self.card_width)+(100*card_index)
            y = (self.player2_hand_mid_card_y)

            return (x, y)

        return (ui_card.x, ui_card.y)

    def exit_button(self, position):

        if self.exitbutton_x <= position[0] <= self.exitbutton_x + self.button_width and self.exitbutton_y <= position[1] <= self.exitbutton_y + self.button_height:
            return True

        return False

    def sort_button(self, position):

        if self.sortbutton_x <= position[0] <= self.sortbutton_x + self.button_width and self.sortbutton_y <= position[1] <= self.sortbutton_y + self.button_height:
            return True

        return False

    def play_button(self, position):

        if self.playbutton_x <= position[0] <= self.playbutton_x + self.card_width and self.playbutton_y <= position[1] <= self.playbutton_y + self.card_height:
            return True

        return False
