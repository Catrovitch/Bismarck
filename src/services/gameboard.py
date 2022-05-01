# The Gameboard class will be used to oversee all cards
# and where they are at all times of the game.

class GameBoard:

    """ This class is used to store the location of all cards at all times of the game.
        This is achieved by moving cards between different lists that represent various elements of the game.

    Attributes:
        reserve_deck: All cards are here in the beginning of the game. (list)
        field_deck: The "battlefield" of the game. Here players place cards that are played against the opponent. (list)
        trash_deck: All cards that are discarded are kept in this deck. (list)

        player1_hand: The cards that are in the hand of player1. (list)
        player1_endgame: The cards that are the endgame cards of player1. (list)
        player1_final: The final cards of player1. (list)
        player1_staged: Before committing one or more card to the field_deck they are staged to this deck. (list)

        player2_hand: The cards that are in the hand of player2. (list)
        player2_endgame: The cards that are the endgame cards of player2. (list)
        player2_final: The final cards of player2. (list)
        player2_staged: Before committing one or more card to the field_deck they are staged to this deck. (list)
    """

    def __init__(self, deck):
        """Constructor method of the class which initiates all the attributes.

        Args:
            deck: A deck of cards which is derived through the class CreateDeck.export() method. (list of items of type Card class)
        """

        # All of these are shared between both players
        self.reserve_deck = deck

        self.field_deck = []
        self.trash_deck = []

        # Player1 specific
        self.player1_hand = []
        self.player1_endgame = []
        self.player1_final = []
        self.player1_staged = []

        # Player2 specific
        self.player2_hand = []
        self.player2_endgame = []
        self.player2_final = []
        self.player2_staged = []
