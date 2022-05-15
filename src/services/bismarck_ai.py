import random
from ui.pictures.album import Album


class BismarckAI:
    """Class which functions as the AI which is used in the main game.

    Attributes:
        gamelogic: instance of GameLogic class
        gameboard: instance of Gameboard class
        hand: the hand of the bismarck AI (also player2 hand
        staged: the staged of the bismarck AI (also player2_staged)
        endgame: the endgame cards of the bismarck AI (also player2_endgame)
        final: the final cards of the bismarck AI (also player2_final
        endgame_ui: instance of EndgameUI class
        final_ui: instance of FinalUI class
        album: instance of Album class
        player: instance of Player class))
    """

    def __init__(self, gamelogic, endgame, final, player):
        """Constructor of the class.

        Args:
            gamelogic (class): instance of GameLogic class
            endgame (class): instance of EndgameUI class
            final (class): instance of FinalUI class
            player (class): instance of Player class
        """

        self.gamelogic = gamelogic
        self.gameboard = self.gamelogic.gameboard
        self.hand = self.gamelogic.gameboard.player2_hand
        self.staged = self.gamelogic.gameboard.player2_staged
        self.endgame = self.gamelogic.gameboard.player2_endgame
        self.final = self.gamelogic.gameboard.player2_final
        self.endgame_ui = endgame
        self.final_ui = final
        self.final_list = ["first", "second", "third"]
        self.album = Album().images
        self.player = player

    def choose_endgame_cards(self):
        """Used in the beginning of the game to choose the endgame cards.
        """

        for card in self.hand:

            if card.number in (2, 10, 14) and len(self.endgame) < 3:
                self.player.choose_endgame_cards(card)
                if self.endgame_ui.first is False:
                    self.endgame_ui.add_card(self.album[card.name], "first")
                    self.endgame_ui.first = self.album[card.name]
                    self.choose_endgame_cards()
                    continue
                if self.endgame_ui.second is False:
                    self.endgame_ui.add_card(self.album[card.name], "second")
                    self.endgame_ui.second = self.album[card.name]
                    self.choose_endgame_cards()
                    continue
                # if self.endgame_ui.third is False:
                self.endgame_ui.add_card(self.album[card.name], "third")
                self.endgame_ui.third = self.album[card.name]
                self.choose_endgame_cards()
                continue

        index = 0
        while len(self.endgame) < 3:
            card = max(self.gameboard.player2_hand,
                       key=lambda card: card.number)
            self.player.choose_endgame_cards(card)

            if self.endgame_ui.first is False:
                self.endgame_ui.add_card(self.album[card.name], "first")
                self.endgame_ui.first = self.album[card.name]
                index += 1
                continue
            if self.endgame_ui.second is False:
                self.endgame_ui.add_card(self.album[card.name], "second")
                self.endgame_ui.second = self.album[card.name]
                index += 1
                continue
            # if self.endgame_ui.third is False:
            self.endgame_ui.add_card(self.album[card.name], "third")
            self.endgame_ui.third = self.album[card.name]
            index += 1
            continue

    def choose_least_valuable_card(self, deck, top_card):
        """Used to choose the least valuable card that still defeats the top_card in a given deck.

        Args:
            deck (list): the deck from which to search the least valueable card. Ex. self.hand or self.endgame
            top_card (list): the current top_card of the field_deck.

        Returns:
            True: if card is found
            False: if no card is found"""

        minimi = 14
        chosen = True

        for card in deck:
            if top_card <= card.number <= minimi and card.number not in (0, 2, 10):
                minimi = card.number
                chosen = card

        if chosen is True:
            for card in deck:
                if card.number in (0, 2, 10):
                    chosen = card

        if chosen is True:
            return False

        return chosen

    def chance(self):
        """Used by BismarckAI to chance"""

        self.player.chance()

    def play_from_hand(self, top_card):
        """Used to play a card from the hand

        Args:
            top_card: the current top card of the field_deck

        Returns:
            True: if card is found in the hand.
            False: if no card is found in the hand."""

        self.player.sort_hand()

        chosen_card = self.choose_least_valuable_card(self.hand, top_card)

        if chosen_card is False:
            return False

        self.player.stage_card_from_hand(chosen_card)
        self.player.play_staged_cards()
        return True

    def play_from_endgame(self, top_card):
        """Used to play a card from the endgame cards

        Args:
            top_card: The current top card of the field_deck

        Returns:
            True: if a card is found in the endgame cards
            False: if no card is found in the endgame cards
        """

        chosen_card = self.choose_least_valuable_card(self.endgame, top_card)

        if chosen_card is False:
            return False

        self.player.stage_card_from_endgame(chosen_card)
        self.endgame_ui.use_card(self.album[chosen_card.name])
        self.player.play_staged_cards()
        return True

    def choose_played_cards(self):
        """Used to see from which card-set BismarckAI should play a card from.
        """

        if self.gamelogic.turn == 1:
            return

        top_card = 0

        if len(self.gameboard.field_deck) > 0:
            index = 1
            while top_card == 0 and index <= len(self.gameboard.field_deck):
                top_card = self.gameboard.field_deck[-index].number
                index += 1

        if len(self.hand) > 0:
            if self.play_from_hand(top_card):
                return

        if len(self.gameboard.reserve_deck) > 0:
            self.chance()
            return

        if len(self.endgame) > 0 and len(self.hand) == 0:
            if self.play_from_endgame(top_card):
                return

        if len(self.endgame) == 0 and len(self.hand) == 0 and len(self.final) > 0:
            self.player.play_finalcard()
            choice = random.choice(self.final_list)
            self.final_list.remove(choice)
            self.final_ui.use_card(choice)
            return

        if len(self.endgame) == 0 and len(self.hand) == 0 and len(self.final) == 0:
            return

        self.player.pick_up_field_deck()
