class Player:


    def __init__(self, account_name, reserve, field):

        self.account_name = account_name
        
        self.reserve = reserve
        self.field = field

        self.hand = []
        self.endgame_cards = []
        self.final_cards = []
        
        self.staged = []

    def stage_hand_card(self, card_index):

        self.staged.append(self.hand.pop(card_index))

    def stage_endgame_card(self, card_index):

        self.staged.append(self.endgame_cards.pop(card_index))

    def play_final_card(self, card_index):

        self.field.deck.append(self.final_cards.pop(card_index))

    def play_staged_cards(self):

        for card in self.staged:
            self.field.deck.append(self.staged.pop())

    def chance(self):

        self.reserve.draw(self.field.deck)

    def draw_from_reserve(self, number_of_cards):

        while len(self.hand) < 3:
            if self.reserve.empty():
                break
            else:
                self.reserve.draw(self.hand)

    def lift_field_deck(self):

        while True:
            if self.field.empty():
                break
            else:
                self.field.draw(self.hand)

