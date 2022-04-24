class BismarckAI:

    def __init__(self, gamelogic):

        self.name = "BismarckAI"
        self.gamelogic = gamelogic
        self.gameboard = self.gamelogic.gameboard
        self.hand = self.gamelogic.gameboard.player2_hand
        self.staged = self.gamelogic.gameboard.player2_staged
        self.endgame = self.gamelogic.gameboard.player2_endgame
        self.final = self.gamelogic.gameboard.player2_final

    def choose_endgame_cards(self):

        for card in self.hand:
            if card.number in (2, 10, 14) and len(self.endgame) < 3:
                self.gamelogic.choose_endgame_cards(-1, card)

        self.gamelogic.sort_hand(-1)

        while len(self.endgame) < 3:
            self.gamelogic.choose_endgame_cards(-1,
                                                self.gamelogic.player2_hand.pop())

    def choose_played_cards(self):

        self.gamelogic.sort_hand(-1)

        top_card = 0

        if len(self.gameboard.field_deck) > 0:
            top_card = self.gamelogic.field_deck[-1].number

        special = (0, 2, 10)

        for card in self.hand:
            dif = card.number-top_card
            if dif >= 0 and card.number not in special:
                self.gamelogic.stage_card_from_hand(-1, card)

        if len(self.staged) == 0:
            for card in self.hand:
                if card.number in special:
                    self.gamelogic.stage_card_from_hand(-1, card)

        if len(self.staged) == 0:
            self.gamelogic.chance(-1)

        self.gamelogic.play_staged_cards(-1)

    def choose_played_cards_endgame(self):

        top_card = 0

        if len(self.gameboard.field_deck) > 0:
            top_card = self.gamelogic.field_deck[-1].number

        special = (0, 2, 10)

        for card in self.endgame:
            dif = card.number-top_card
            if dif >= 0 and card.number not in special:
                self.gamelogic.stage_card_from_hand(-1, card)

        if len(self.staged) == 0:
            for card in self.hand:
                if card.number in special:
                    self.gamelogic.stage_card_from_hand(-1, card)
