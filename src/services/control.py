import pygame
from services.createdeck import CreateDeck
from services.gameboard import GameBoard
from services.gamelogic import GameLogic
from services.player import Player
from ui.landscapes.create_account import CreateAccount
from ui.landscapes.main_menu import MainMenu

from ui.ui_services.renderer import Renderer
from ui.landscapes.game import Game
from ui.ui_services.eventqueue import EventQueue
from ui.ui_services.finalcards import PlayerFinal
from ui.ui_services.endgame import PlayerEndgame
from ui.ui_services.gameboard_positions import GameboardPositions
from ui.pictures.album import Album
from ui.pictures.display_size import DisplaySize
from ui.landscapes.login import Login
from ui.landscapes.rules import Rules
from ui.landscapes.ratingboard import RatingBoard
from services.user_control import UserControl

from services.bismarck_ai import BismarckAI


class Control:
    """Class which controls the whole program."""

    def __init__(self):

        self.album = Album()
        self.display_size = DisplaySize()

        self.display = pygame.display.set_mode(
            (self.display_size.width, self.display_size.height), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        # Deciding some dimensions
        self.card_for_size = self.album.images["cardback"]
        self.card_width = self.card_for_size.width
        self.card_height = self.card_for_size.height

        self.user_control = UserControl()
        self.gameboard_positions = GameboardPositions(
            self.album, self.display_size, self.card_width, self.card_height)
        self.renderer = Renderer(
            self.display, self.gameboard_positions, self.album, self.user_control)
        self.eventqueue = EventQueue()

    def login(self):

        login = Login(self.renderer, self.eventqueue, self.clock,
                      self.gameboard_positions, self.user_control)

        next = login.login_loop()

        self.next_window(next)

    def create_account(self):

        create_account = CreateAccount(
            self.renderer, self.eventqueue, self.clock, self.gameboard_positions, self.user_control)

        next = create_account.create_account_loop()

        self.next_window(next)

    def main_menu(self):

        main_menu = MainMenu(self.renderer, self.eventqueue,
                             self.clock, self.gameboard_positions)

        next = main_menu.main_menu_loop()

        self.next_window(next)

    def game(self):

        self.deck = CreateDeck()
        self.deck = self.deck.export()
        self.gameboard = GameBoard(self.deck)
        self.gamelogic = GameLogic(self.gameboard)
        self.player1 = Player(1, self.gamelogic)
        self.player2 = Player(-1, self.gamelogic)

        self.player1_endgame = PlayerEndgame()
        self.player1_final = PlayerFinal()
        self.player2_endgame = PlayerEndgame()
        self.player2_final = PlayerFinal()

        self.bismarck = BismarckAI(
            self.gamelogic, self.player2_endgame, self.player2_final, self.player2)

        self.gameboard_positions.gameboard = self.gameboard

        self.renderer = Renderer(self.display, self.gameboard_positions, self.album, self.user_control, self.gamelogic,
                                 self.gameboard, self.player1_endgame, self.player1_final, self.player2_endgame, self.player2_final)

        game = Game(self.gamelogic, self.gameboard_positions, self.player1, self.player2, self.renderer, self.album,
                    self.eventqueue, self.clock, self.player1_endgame, self.player1_final, self.player2_endgame, self.player2_final, self.bismarck, self.user_control)

        game.game_begun = False

        next = game.gameloop()

        self.next_window(next)

    def rules(self):

        rules = Rules(self.renderer, self.eventqueue,
                      self.clock, self.gameboard_positions)

        next = rules.rule_loop()

        self.next_window(next)

    def ratingboard(self):

        ratingboard = RatingBoard(
            self.renderer, self.eventqueue, self.clock, self.gameboard_positions)

        next = ratingboard.ratingboard_loop()

        self.next_window(next)

    def next_window(self, number):

        if number == 1:
            self.login()

        if number == 2:
            self.create_account()

        if number == 3:
            self.main_menu()

        if number == 4:
            self.game()

        if number == 5:
            self.rules()

        if number == 6:
            self.ratingboard()
