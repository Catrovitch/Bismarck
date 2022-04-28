class Card:
    """This class is used to express all cards used in the program.

    Attributes:
        suit: suit of each card (string)
        number: the numberic value of each card (integer)
        name: a combination of suit and number; ex. suit = hearts, number = 2 --> "2_of_hearts" (string)

    """

    def __init__(self, suit, number):

        """Constructor which is used in the creation of a new card.

        Args:
            suit: the suit of the card
            nunmber: the numberic value of the card
        """

        self.suit = suit
        self.number = number
        self.name = f"{number}_of_{suit}"