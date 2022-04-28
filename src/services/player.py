class Player:

    """It is through this class that a player does any action that he/she wants to do in the game.

    Attributes:
        player_id: a specific id for each player in the game. Player1 corresponds with 1 while player2 corresponds with -1. (int)
        gamelogic: An instance of the class GameLogic
    """

    def __init__(self, player_id, gamelogic):

        """Constructor of the class. 

        Args:
            player_id: if player1 it will be 1. If player2 it will be -1. (int)
            gamelogic: instance of GameLogic class.
        """     

        self.player_id = player_id
        self.gamelogic = gamelogic

    def stage_card_from_hand(self, card):

        """Used by a player to move a card from his hand_cards to staged_card. Calls on GameLogic method "stage_card_from_hand with arguments self.player_id and a specific card.

        Args:
            card: The selected card.
        """

        self.gamelogic.stage_card_from_hand(self.player_id, card)

    def stage_card_from_endgame(self, card):

        """Used by a player to move a card from his endgame_cards to staged_card. Calls on GameLogic method "stage_card_from_endgame with arguments self.player_id and a specific card.

        Args:
            card: The selected card.
        """

        self.gamelogic.stage_card_from_endgame(self.player_id, card)

    def play_staged_cards(self):

        """Commits the cards that have been staged by a player. Calls on GameLogic method "play_staged_cards" with argument self.player_id.
        """

        self.gamelogic.play_staged_cards(self.player_id)

    def pick_up_field_deck(self):

        """Used by the player when he/she wants or has to pick up the field_deck. Calls on the GameLogic method "pick_up_field_deck" with argument self.player_id".
        """

        self.gamelogic.pick_up_field_deck(self.player_id)

    def chance(self):

        """Used by the player when he/she wants to chance. Calls on the GameLogic method "chance" with the argument self.player_id.
        """

        self.gamelogic.chance(self.player_id)
