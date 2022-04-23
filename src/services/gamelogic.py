class GameLogic:

    # The GameLogic class will be used to check that the rules are followed
    # by the Player class which also controls the Gameboard class through Gamelogic class
    def __init__(self, gameboard):

        self.gameboard = gameboard
        self.turn = 1

    def choose_endgame_cards(self, player, card):

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

        if player == 1:
            self.gameboard.field_deck += self.gameboard.player1_staged
            self.gameboard.player1_staged.clear()
            self.turn *= -1

        if player == -1:
            self.gameboard.field_deck += self.gameboard.player2_staged
            self.gameboard.player2_staged.clear()
            self.turn *= -1

    def check_card_hierarchy(self, amount_played):

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

        if player == 1:

            self.gameboard.player1_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()

        if player == -1:

            self.gameboard.player2_hand += self.gameboard.field_deck
            self.gameboard.field_deck.clear()

    def chance(self, player):

        self.gameboard.field_deck.append(self.gameboard.reserve_deck.pop())

        if player == 1 and self.turn == 1:
            return self.check_card_hierarchy(1)

        if player == 1 and self.turn == -1:
            return self.check_chance(player)

        if player == -1 and self.turn == -1:
            return self.check_card_hierarchy(1)

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

        self.turn *= -1
        return

    def initial_deal(self):

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
