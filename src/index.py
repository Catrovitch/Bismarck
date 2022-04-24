import pygame

from services.createdeck import CreateDeck
from services.gameboard import GameBoard
from services.gamelogic import GameLogic
from services.player import Player
from ui.renderer import Renderer
from ui.game import Game
from ui.eventqueue import EventQueue
from ui.finalcards import Player1Final
from ui.finalcards import Player2Final
from ui.endgame import Player1Endgame
from ui.endgame import Player2Endgame
from ui.gameboard_positions import GameboardPositions
from ui.pictures.album import Album


def main_game():
    deck = CreateDeck()
    deck = deck.export()
    gameboard = GameBoard(deck)
    gamelogic = GameLogic(gameboard)
    player1 = Player(1, gamelogic)
    player2 = Player(-1, gamelogic)
    album = Album()
    display_size = album.images["background"]

    display = pygame.display.set_mode(
        (display_size.width, display_size.height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Bismarck")

    player1_endgame = Player1Endgame()
    player1_final = Player1Final()
    player2_endgame = Player2Endgame()
    player2_final = Player2Final()

    # Deciding some dimensions
    card_for_size = album.images["cardback"]
    card_width = card_for_size.width
    card_height = card_for_size.height

    gameboard_positions = GameboardPositions(
        gameboard, album, display_size, card_width, card_height)

    renderer = Renderer(display, gameboard, gameboard_positions, album,
                        player1_endgame, player1_final, player2_endgame, player2_final)
    eventqueue = EventQueue()

    game = Game(gamelogic, gameboard_positions, player1, player2, renderer, album,
                eventqueue, clock, player1_endgame, player1_final, player2_endgame, player2_final)

    game.gameloop()


if __name__ == "__main__":

    main_game()
