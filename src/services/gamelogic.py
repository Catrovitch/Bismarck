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
        self.player1_last_played = None
        self.player2_last_played = None

        self.stage_of_game = 0
        self.player1_locked = True
        self.player1_last_staged = None
        self.player2_locked = True
        self.player2_last_staged = None

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
            if self.player1_locked is True:
                return False

        if player == -1:
            if self.player2_locked is True:
                return False

        if player == 1:
            # Checks if card can be staged and stages it if possible.
            length = len(self.gameboard.player1_staged)

            if length > 0:
                self.player1_last_staged = self.gameboard.player1_staged[-1]

            if length == 0 or card.number in (self.player1_last_staged.number, 0) or self.player1_last_staged.number == 0:
                self.gameboard.player1_staged.append(card)
                self.gameboard.player1_hand.remove(card)
                self.sort_staged(1)

                self.player1_last_staged = self.gameboard.player1_staged[-1]

                return True

            return False

        length = len(self.gameboard.player2_staged)
        if length > 0:
            self.player2_last_staged = self.gameboard.player2_staged[-1]
        if length == 0 or card.number in (self.player2_last_staged.number, 0) or self.player2_last_staged.number == 0:
            self.gameboard.player2_staged.append(card)
            self.gameboard.player2_hand.remove(card)
            self.sort_staged(-1)

            self.player2_last_staged = self.gameboard.player2_staged[-1]
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
            if self.player1_locked is True:
                return False

        if player == -1:
            if self.player2_locked is True:
                return False

        if player == 1:
            # Checks if card can be staged and stages it if possible.
            length = len(self.gameboard.player1_staged)

            if length > 0:
                self.player1_last_staged = self.gameboard.player1_staged[-1]

            if length == 0 or card.number in (self.player1_last_staged.number, 0) or self.player1_last_staged.number == 0:
                self.gameboard.player1_staged.append(card)
                self.gameboard.player1_endgame.remove(card)
                self.sort_staged(1)

                self.player1_last_staged = self.gameboard.player1_staged[-1]

                return True

            return False

        length = len(self.gameboard.player2_staged)
        if length > 0:
            self.player2_last_staged = self.gameboard.player2_staged[-1]
        if length == 0 or card.number in (self.player2_last_staged.number, 0) or self.player2_last_staged.number == 0:
            self.gameboard.player2_staged.append(card)
            self.gameboard.player2_endgame.remove(card)
            self.sort_staged(-1)

            self.player2_last_staged = self.gameboard.player2_staged[-1]
            return True

        return False

    def unstage_cards(self):

        self.gameboard.player1_hand += self.gameboard.player1_staged
        self.gameboard.player1_staged.clear()

    def play_staged_cards(self, player):
        """Moves the cards in the player staged list to the field_deck. This also changes who's turn it is in the game.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
        """
        if player == 1:
            if self.player1_locked is True or len(self.gameboard.player1_staged) == 0:
                return False

        if player == -1:
            if self.player2_locked is True or len(self.gameboard.player2_staged) == 0:
                return False

        if player == 1:

            amount_played = len(self.gameboard.player1_staged)
            if self.gameboard.player1_staged[-1].number == 0:
                for card in self.gameboard.player1_staged:
                    self.gameboard.field_deck.insert(-1, card)
                self.gameboard.player1_staged.clear()
                self.player2_locked = False
                return self.check_card_hierarchy(1, 1)
            self.gameboard.field_deck += self.gameboard.player1_staged
            self.gameboard.player1_staged.clear()
            self.player2_locked = False
            return self.check_card_hierarchy(1, amount_played)

        amount_played = len(self.gameboard.player2_staged)
        if self.gameboard.player2_staged[-1].number == 0:
            for card in self.gameboard.player2_staged:
                self.gameboard.field_deck.insert(-1, card)
            self.gameboard.player2_staged.clear()
            self.player1_locked = False
            return self.check_card_hierarchy(-1, 1)
        self.gameboard.field_deck += self.gameboard.player2_staged
        self.gameboard.player2_staged.clear()
        self.player1_locked = False
        return self.check_card_hierarchy(-1, amount_played)

    def check_card_hierarchy(self, player, amount_played):
        """Checks that the card hierarchy in the field_deck is upheld.

        Args:
            amount_played: how many cards where played.

        Returns:
            True: if the card hierarchy is correct.
            False: if the card hierarchy is incorrect.
        """
        if len(self.gameboard.field_deck) >= 4:
            count = 1
            for i in range(2, 5):
                if self.gameboard.field_deck[-i].number in (self.gameboard.field_deck[-1].number, 0):
                    count += 1
                else:
                    break
            if count >= 4:
                self.gameboard.trash_deck += self.gameboard.field_deck
                self.gameboard.field_deck.clear()
                return True

        if len(self.gameboard.field_deck) == amount_played and player == 1:
            if self.gameboard.field_deck[-1].number == 10:
                self.gameboard.trash_deck += self.gameboard.field_deck
                self.gameboard.field_deck.clear()
                return True

            self.draw_cards(1)
            self.change_turn(1)
            self.player1_last_played = self.gameboard.field_deck[-1]
            return True

        if len(self.gameboard.field_deck) == amount_played and player == -1:
            if self.gameboard.field_deck[-1].number == 10:
                self.gameboard.trash_deck += self.gameboard.field_deck
                self.gameboard.field_deck.clear()
                return True

            self.draw_cards(-1)
            self.change_turn(-1)
            self.player2_last_played = self.gameboard.field_deck[-1]
            return True

        played_card = self.gameboard.field_deck[-1]

        opposed_card = self.gameboard.field_deck[-(amount_played+1)]

        if self.turn == 1 and player == 1:

            if played_card.number == 0:
                self.gameboard.field_deck.insert(-2, played_card)
                self.gameboard.field_deck.pop()
                self.draw_cards(1)
                self.change_turn(1)
                self.player1_last_played = self.gameboard.field_deck[-1]
                return True

            if played_card.number == 2:
                self.draw_cards(1)
                self.change_turn(1)
                self.player1_last_played = self.gameboard.field_deck[-1]
                return True

            if played_card.number == 10:

                self.gameboard.trash_deck += self.gameboard.field_deck
                self.gameboard.field_deck.clear()
                return True

            if played_card.number >= opposed_card.number:
                self.draw_cards(1)
                self.change_turn(1)
                self.player1_last_played = self.gameboard.field_deck[-1]
                return True

            self.change_turn(1)
            self.pick_up_field_deck(1)
            return False

        if player == -1 and self.turn == -1:

            if played_card.number == 0:
                self.gameboard.field_deck.insert(-2, played_card)
                self.gameboard.field_deck.pop()
                self.draw_cards(-1)
                self.change_turn(-1)
                self.player2_last_played = self.gameboard.field_deck[-1]
                return True

            if played_card.number == 2:
                self.draw_cards(-1)
                self.change_turn(-1)
                self.player2_last_played = self.gameboard.field_deck[-1]
                return True

            if played_card.number == 10:

                self.gameboard.trash_deck += self.gameboard.field_deck
                self.gameboard.field_deck.clear()
                return True

            if played_card.number >= opposed_card.number:
                self.draw_cards(-1)
                self.change_turn(-1)
                self.player2_last_played = self.gameboard.field_deck[-1]
                return True

            self.change_turn(-1)
            self.pick_up_field_deck(-1)
            return False

        if player == 1 and self.turn == -1:

            if played_card.number in (self.player1_last_played.number, 0):
                self.draw_cards(1)
                return True

            self.pick_up_field_deck(1)
            return False

        if played_card.number in (self.player2_last_played.number, 0):
            self.draw_cards(1)
            return True

        self.pick_up_field_deck(-1)
        return False

    def pick_up_field_deck(self, player):
        """Moves the cards from the field_deck to the hand_cards of a player. Used when a player wants or has to pick up the field_deck.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)
        """

        if player == 1:

            self.gameboard.player1_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()
            self.player1_locked = True
            self.change_turn(1)

        if player == -1:

            self.gameboard.player2_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()
            self.player2_locked = True
            self.change_turn(-1)

    def chance(self, player):
        """Takes to top card from the reserve_deck (reserve_deck[-1]) and places it on the field_deck. Checks the card_hierarchy.

        Args:
            player: If method is called by player1 it will be 1. If called by player2 it will be -1. (int)

        Returns:
            True: if the chance is successful.
            False: if the chance is unsuccessful.
        """
        if player == 1 and self.player1_locked is True or len(self.gameboard.reserve_deck) == 0:
            return False

        if player == -1 and self.player2_locked is True or len(self.gameboard.reserve_deck) == 0:
            return False

        self.gameboard.field_deck.append(self.gameboard.reserve_deck.pop())

        if self.turn == 1 and player == 1:
            result = self.check_card_hierarchy(1, 1)
            self.change_turn(player)
            return result

        if self.turn == -1 and player == 1:
            return self.check_card_hierarchy(1, 1)

        # if self.turn == -1 and player == -1:
        return self.check_card_hierarchy(-1, 1)

    def play_finalcard(self, player_id):

        if player_id == 1:

            self.gameboard.field_deck.append(
                self.gameboard.player1_final.pop())
            return self.check_card_hierarchy(1, 1)

        self.gameboard.field_deck.append(self.gameboard.player2_final.pop())
        return self.check_card_hierarchy(-1, 1)

    def decide_turn_in_beginning(self):
        """Called on in the beginning of a game after players have chosen their endgame_cards. Decides who has the first turn.
        """

        player1 = 0
        player2 = 0

        for card in self.gameboard.player1_hand:
            if card.number in (2, 10, 0):
                player1 += 14
                continue
            player1 += card.number

        for card in self.gameboard.player2_hand:
            if card.number in (2, 10, 0):
                player2 += 14
                continue
            player2 += card.number

        if player1 < player2:
            self.player1_locked = False
            self.turn = 1
            return

        self.player2_locked = False
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

        self.gameboard.player2_hand.sort(key=lambda x: x.number)

    def sort_staged(self, player):
        """Sorts a players staged_cards so that the joker is always at the bottom. This way it is much easier to keep track on what happens.

        Args:
            player: If method is called by player1 it will be 1. If caleld by player2 it will be -1. (int)
        """

        if player == 1:

            self.gameboard.player1_staged.sort(key=lambda x: x.number)

        if player == -1:

            self.gameboard.player2_staged.sort(key=lambda x: x.number)

    def change_turn(self, player_id):

        """This method is used to change the turn of the game. 

        Args:
            player_id: gives the id of the player which turn it is currently by which the method knows that it should be the opposite.
        """

        if player_id == 1:

            self.turn = -1

        if player_id == -1:

            self.turn = 1

    def draw_cards(self, player):

        """Used by a player to draw cards from the reserve deck.

        Args:
            player: gives the id of the player so the method knows who calls on it.
        """

        if player == 1:

            while len(self.gameboard.player1_hand) < 3 and len(self.gameboard.reserve_deck) > 0:
                self.gameboard.player1_hand.append(
                    self.gameboard.reserve_deck.pop())

            return

        if player == -1:

            while len(self.gameboard.player2_hand) < 3 and len(self.gameboard.reserve_deck) > 0:
                self.gameboard.player2_hand.append(
                    self.gameboard.reserve_deck.pop())
