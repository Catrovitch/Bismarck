class User:
    """Class which keeps information about a users account.

    Attributes:
        username: String which corresponds with the username the user has chosen.
        password: String which corresponds with the password the user has chosen.
        rating: Integer that corresponds with the current rating of the user.
    """

    def __init__(self, username, password, rating):
        """The class Constructor. Creates a new user.

        Args:
            username (str): String which corresponds with the username the user has chosen.
            password (str): String which corresponds with the password the user has chosen.
            rating (int): Integer that corresponds with the current rating of the user. Updated after each game. +/- 15 for win or loss.
        """
        self.username = username
        self.password = password
        self.rating = rating
