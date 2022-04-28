class GameLogic:

    """The class GameLogic is used to controll the various aspects of the game. For example if it takes a commands from a player (class) it checks what the approriate response to the command is and performs this task.

    Attributes:
        gameboard: An instance of the Gameboard class.
        turn: Keeps account of who's turn it is.
    """
    def __init__(self, gameboard):

        """Constructor of the class.

        Args:
            gameboard: An instance of the Gameboard class.
        """
        self.gameboard = gameboard
        self.turn = 0

    def choose_endgame_cards(self, player, card):

        """Used in the beginning of a game by players to choose their endgame cards. Moves one card from the player's hand to the player-specific endgame_card's list. Checks that the rules are followed.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
            card: The chosen card. (class: Card)

        Returns:
            True: If the card is chosen and moved from the player's hand to his/her endgame_card's list successfully.
            False: If the cards is not moved successfully. For example in the case where a player has already chosen the max amount of three endgame_cards.
        """
        if player == 1 and len(self.gameboard.player1_endgame) < 3:

            self.gameboard.player1_endgame.append(card)
            self.gameboard.player1_hand.remove(card)
            return True

        if player == -1 and len(self.gameboard.player2_endgame) < 3:

            self.gameboard.player2_endgame.append(card)
            self.gameboard.player2_hand.remove(card)
            return True

        return False

    def stage_card_from_hand(self, player, card):

        """Takes a card from a players hand and moves it to his/her player-specific staged list. Checks that the rules are followed.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
            card: The chosen card. (class: Card)

        Returns:
            True: if the card is staged succsessfully.
            False: if the card is not staged succsessfully.
        """
        if player == 1:
            # Checks if card can be staged and stages it if possible.
            length = len(self.gameboard.player1_staged)

            for staged_card in self.gameboard.player1_staged:
                if staged_card.number > 0:
                    last_staged = staged_card
                    break

                last_staged = staged_card

            if length == 0 or card.number in (last_staged.number, 0) or last_staged.number == 0:
                self.gameboard.player1_staged.append(card)
                self.gameboard.player1_hand.remove(card)
                return True

            return False

        length = len(self.gameboard.player2_staged)
        if length > 0:
            last_staged = self.gameboard.player2_staged[-1]
        if length == 0 or card.number in (last_staged.number, 0):
            self.gameboard.player2_staged.append(card)
            self.gameboard.player2_hand.remove(card)
            return True

        return False

    def stage_card_from_endgame(self, player, card):

        """Very similar to the method "stage_card_form_hand", but is used in case the player wants to stage a card from his/her endgame_cards. It takes a card from the player-specific endgame_card's list and moves it to the player-specific staged list.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
            card: The chosen card. (class: Card)

        Returns:
            True: if the card is staged succsessfully.
            False: if the card is not staged succsessfully.
        """

        if player == 1:
            # Checks if card can be staged and stages it if possible.
            length = len(self.gameboard.player1_staged)
            if length > 0:
                last_staged = self.gameboard.player1_staged[-1]
            if length == 0 or card.number in (last_staged.number, 0):
                self.gameboard.player1_staged.append(card)
                self.gameboard.player1_endgame.remove(card)
                return True

            return False

        length = len(self.gameboard.player2_staged)
        if length > 0:
            last_staged = self.gameboard.player2_staged[-1]
        if length == 0 or card.number in (last_staged.number, 0):
            self.gameboard.player2_staged.append(card)
            self.gameboard.player2_endgame.remove(card)
            return True

        return False

    def play_staged_cards(self, player):

        """Moves the cards in the player staged list to the field_deck. This also changes who's turn it is in the game.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
        """

        if player == 1:
            self.gameboard.field_deck += self.gameboard.player1_staged
            self.gameboard.player1_staged.clear()
            self.turn *= -1

        if player == -1:
            self.gameboard.field_deck += self.gameboard.player2_staged
            self.gameboard.player2_staged.clear()
            self.turn *= -1

    def check_card_hierarchy(self, amount_played):

        """Checks that the card hierarchy in the field_deck is upheld.

        Args:
            amount_played: how many cards where played.

        Returns:
            True: if the card hierarchy is correct.
            False: if the card hierarchy is incorrect.
        """

        if len(self.gameboard.field_deck) == amount_played:
            return True

        top_card = self.gameboard.field_deck[-1]
        last_card = self.gameboard.field_deck[-(amount_played+1)]

        if top_card.number == 2:

            return True

        if top_card.number == 10:

            self.gameboard.trash_deck += self.gameboard.field_deck
            self.gameboard.field_deck.clear()

            return True

        if top_card.number >= last_card.number:

            return True

        return False

    def pick_up_field_deck(self, player):

        """Moves the cards from the field_deck to the hand_cards of a player. Used when a player wants or has to pick up the field_deck. 

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
        """

        if player == 1:

            self.gameboard.player1_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()

        if player == -1:

            self.gameboard.player2_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()

    def chance(self, player):

        """Takes to top card from the reserve_deck (reserve_deck[-1]) and places it on the field_deck. Checks the card_hierarchy.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)

        Returns:
            True: if the chance is successful.
            False: if the chance is unsuccessful.
        """

        if len(self.gameboard.reserve_deck) == 0:
            return False

        self.gameboard.field_deck.append(self.gameboard.reserve_deck.pop())

        if player == 1 and self.turn == 1:
            return self.check_card_hierarchy(1)

        if player == 1 and self.turn == -1:
            return self.check_chance(player)

        if player == -1 and self.turn == -1:
            return self.check_card_hierarchy(1)

        return self.check_chance(player)

    def check_chance(self, player):

        """Used when a player chances on his/her off-turn

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)

        Returns:
            True: if the chance is successful
            False: if it is unsuccsessful
        """

        if self.gameboard.field_deck[-1].number in (self.gameboard.field_deck[-2].number, 0):
            return True

        self.pick_up_field_deck(player)

        return False

    def decide_turn_in_beginning(self):

        """Called on in the beginning of a game after players have chosen their endgame_cards. Decides who has the first turn.
        """

        player1 = 0
        player2 = 0

        for card in self.gameboard.player1_hand:
            if card.number in (2, 10):
                player1 += 14
                continue
            player1 += card.number

        for card in self.gameboard.player2_hand:
            if card.number in (2, 10):
                player2 += 14
                continue
            player2 += card.number

        if player1 < player2:
            self.turn = 1

        self.turn = -1
        return

    def initial_deal(self):

        """Called on in the beginning of a game which gives players 3 randomly selected final_cards and six randomly selected hand_cards from which the players will choose three endgame_cards.
        """

        dealt = 0

        while dealt < 3:
            dealt += 1
            self.gameboard.player1_final.append(
                self.gameboard.reserve_deck.pop())
            self.gameboard.player2_final.append(
                self.gameboard.reserve_deck.pop())

        dealt = 0

        while dealt < 6:
            dealt += 1
            self.gameboard.player1_hand.append(
                self.gameboard.reserve_deck.pop())
            self.gameboard.player2_hand.append(
                self.gameboard.reserve_deck.pop())

    def sort_hand(self, player):

        """Used to sort a players hand_cards in order according to the cards' numeric value.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
        """

        if player == 1:

            self.gameboard.player1_hand.sort(key=lambda x: x.number)

        if player == -1:

            self.gameboard.player2_hand.sort(key=lambda x: x.number)
