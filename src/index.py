from createdeck import CreateDeck
from gameboard import GameBoard
from gamelogic import GameLogic


def main():
    deck = CreateDeck()
    gameboard = GameBoard(deck)
    gamelogic = GameLogic(gameboard)


if __name__ == "__main__":

    main()
