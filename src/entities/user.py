class User:
    """Class which keeps information about a users account.

    Attributes:
        username: String which corresponds with the username the user has chosen.
        password: String which corresponds with the password the user has chosen.
    """
    def __init__(self, username, password, rating):
        """The class Constructor. Creates a new user.
        
        Args:
            username (str): String which corresponds with the username the user has chosen.
            password (str): String which corresponds with the password the user has chosen.
        """
        self.username = username
        self.password = password
        self.rating = rating
