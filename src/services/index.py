from services.createdeck import CreateDeck
from services.gameboard import GameBoard
from services.gamelogic import GameLogic


def main():
    deck = CreateDeck()
    gameboard = GameBoard(deck)
    gamelogic = GameLogic(gameboard)


if __name__ == "__main__":

    main()
