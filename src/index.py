import pygame

from services.createdeck import CreateDeck
from services.gameboard import GameBoard
from services.gamelogic import GameLogic
from services.player import Player
from ui.renderer import Renderer
from ui.scaled.scaling import Background
from ui.game import Game
from ui.eventqueue import EventQueue
from ui.finalcards import Player1Final
from ui.finalcards import Player2Final
from ui.endgame import Player1Endgame
from ui.endgame import Player2Endgame
from ui.scaled.card_pictures import CardPics
from ui.scaled.scaling import Cardback
from ui.gameboard_positions import GameboardPositions

def main_game():
    deck = CreateDeck()
    deck = deck.export()
    gameboard = GameBoard(deck)
    gamelogic = GameLogic(gameboard)
    player1 = Player(1, gamelogic)
    player2 = Player(-1, gamelogic)
    background = Background()

    display = pygame.display.set_mode((background.width,background.height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Bismarck")
    
    player1_endgame = Player1Endgame()
    player1_final = Player1Final()
    player2_endgame = Player2Endgame()
    player2_final = Player2Final()

    card_pics = CardPics().card_pics
    card_for_size = Cardback()
    card_width = card_for_size.width
    card_height = card_for_size.height

    gameboard_positions = GameboardPositions(card_width, card_height)
    
    renderer = Renderer(display, gameboard, gameboard_positions, card_pics, player1_endgame, player1_final, player2_endgame, player2_final)
    eventqueue = EventQueue()

    game = Game(gamelogic, gameboard_positions, player1, player2, renderer, card_pics, eventqueue, clock, player1_endgame, player1_final, player2_endgame, player2_final)

    game.gameloop()



if __name__ == "__main__":

    main_game()
