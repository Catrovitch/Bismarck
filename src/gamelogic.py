from gameboard import GameBoard


class GameLogic:


    #The GameLogic class will be used to check that the rules are followed 
    #by the Player class which also controls the Gameboard class through Gamelogic class
    def __init__(self, gameboard):

        self.gameboard = gameboard

    def stage_card(self, player, card):

        if player == 1:

            if len(self.gameboard.player1_staged) == 0 or card in self.gameboard.player1_staged:
                self.gameboard.player1_staged.append(self.gameboard.player1_hand.pop(card))
            else:
                return False

        if player == 2:

            if len(self.gameboard.player2_staged) == 0 or card in self.gameboard.player2_staged:
                self.gameboard.player2_staged.append(self.gameboard.player2_hand.pop(card))
            else:
                return False