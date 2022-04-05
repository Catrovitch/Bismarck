from createdeck import CreateDeck
from gameboard import GameBoard
from gamelogic import GameLogic
from player import Player

create_deck = CreateDeck()
deck = create_deck.export()
gameboard = GameBoard(deck)
gamelogic = GameLogic(gameboard)
gamelogic.gameboard.initial_deal()

