from gameboard import GameBoard


class GameLogic:


    #The GameLogic class will be used to check that the rules are followed 
    #by the Player class which also controls the Gameboard class through Gamelogic class
    def __init__(self, gameboard):

        self.gameboard = gameboard

    def stage_card(self, player, card):

        if player == 1:

            if len(self.gameboard.player1_staged) == 0 or self.gameboard.player1_hand[card].number == self.gameboard.player1_staged[-1].number or self.gameboard.player1_hand[card].number == 0:
                self.gameboard.move(self.gameboard.player1_hand, self.gameboard.player1_staged, card)
                return True
            else:
                return False

        else:

            if len(self.gameboard.player2_staged) == 0 or self.gameboard.player2_hand[card].number == self.gameboard.player2_staged[-1].number or self.gameboard.player2_hand[card].number == 0:
                self.gameboard.move(self.gameboard.player2_hand, self.gameboard.player2_staged, card)
                return True
            else:
                return False

    def initial_deal(self):

        self.gameboard.initial_deal()