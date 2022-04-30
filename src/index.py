import pygame
from services.createdeck import CreateDeck
from services.gameboard import GameBoard
from services.gamelogic import GameLogic
from services.player import Player
from ui.renderer import Renderer
from ui.game import Game
from ui.eventqueue import EventQueue
from ui.finalcards import PlayerFinal
from ui.endgame import PlayerEndgame
from ui.gameboard_positions import GameboardPositions
from ui.pictures.album import Album
from ui.pictures.display_size import DisplaySize
from services.bismarck_ai import BismarckAI
    

def main_game():
    deck = CreateDeck()
    deck = deck.export()
    gameboard = GameBoard(deck)
    gamelogic = GameLogic(gameboard)
    player1 = Player(1, gamelogic)
    player2 = Player(-1, gamelogic)
    album = Album()
    display_size = DisplaySize()

    display = pygame.display.set_mode(
        (display_size.width, display_size.height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Bismarck")

    player1_endgame = PlayerEndgame()
    player1_final = PlayerFinal()
    player2_endgame = PlayerEndgame()
    player2_final = PlayerFinal()

    bismarck = BismarckAI(gamelogic, player2_endgame, player2_final, player2)
    # Deciding some dimensions
    card_for_size = album.images["cardback"]
    card_width = card_for_size.width
    card_height = card_for_size.height

    gameboard_positions = GameboardPositions(
        gameboard, album, display_size, card_width, card_height)

    renderer = Renderer(display, gamelogic, gameboard, gameboard_positions, album,
                        player1_endgame, player1_final, player2_endgame, player2_final)
    eventqueue = EventQueue()

    game = Game(gamelogic, gameboard_positions, player1, player2, renderer, album,
                eventqueue, clock, player1_endgame, player1_final, player2_endgame, player2_final, bismarck)

    game.gameloop()


if __name__ == "__main__":

    main_game()
