class GameLogic:

    # The GameLogic class will be used to check that the rules are followed
    # by the Player class which also controls the Gameboard class through Gamelogic class
    def __init__(self, gameboard):

        self.gameboard = gameboard
        self.turn = 1

    def stage_card_from_hand(self, player, card):

        if player == 1:
            # Checks if card can be staged and stages it if possible.
            if len(self.gameboard.player1_staged) == 0 or card.number in (self.gameboard.player1_staged[-1].number, 0):
                self.gameboard.player1_staged.append(card)
                self.gameboard.player1_hand.remove(card)
                return True

            return False

        else:
            # Checks if card can be staged and stages it if possible.
            if len(self.gameboard.player2_staged) == 0 or card.number in (self.gameboard.player2_staged[-1].number, 0):
                self.gameboard.player2_staged.append(card)
                self.gameboard.player2_hand.remove(card)
                return True

            return False

    def stage_card_from_endgame(self, player, card):

        if player == 1:
            # Checks if card can be staged and stages it if possible.
            if len(self.gameboard.player1_staged) == 0 or card.number in (self.gameboard.player1_staged[-1].number, 0):
                self.gameboard.player1_staged.append(card)
                self.gameboard.player1_endgame.remove(card)
                return True

            return False

        else:
            # Checks if card can be staged and stages it if possible.
            if len(self.gameboard.player2_staged) == 0 or card.number in (self.gameboard.player1_staged[-1].number, 0):
                self.gameboard.player2_staged.append(card)
                self.gameboard.player2_endgame.remove(card)
                return True

            return False

    def play_staged_cards(self, player):

        if player == 1:
            amount_played = len(self.gameboard.player1_staged)
            self.gameboard.field_deck += self.gameboard.player1_staged
            self.gameboard.player1_staged.clear()

        if player == -1:
            amount_played = len(self.gameboard.player2_staged)
            self.gameboard.field_deck += self.gameboard.player2_staged
            self.gameboard.player2_staged.clear()

        return

    def check_card_hierarchy(self, player, amount_played):

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

        else:
            return False

    def pick_up_field_deck(self, player):

        if player == 1:

            self.gameboard.player1_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()

        if player == -1:

            self.gameboard.player2_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()

    def chance(self, player):

        self.gameboard.field_deck.append(self.gameboard.reserve_deck.pop())

        if player == 1 and self.turn == 1:
            return self.check_card_hierarchy(1, 1)

        if player == 1 and self.turn == -1:
            return self.check_chance(player)

        if player == -1 and self.turn == -1:
            return self.check_card_hierarchy(-1, 1)

        else:
            return self.check_chance(player)

    def check_chance(self, player):

        if self.gameboard.field_deck[-1].number in (self.gameboard.field_deck[-2].number, 0):
            return True

        self.pick_up_field_deck(player)

        return False

    def decide_turn_in_beginning(self):

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
            return

        else:
            self.turn *= -1
            return

    def initial_deal(self):

        self.gameboard.initial_deal()
