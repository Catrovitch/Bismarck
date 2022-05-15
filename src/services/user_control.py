from entities.user import User
from repositories.user_repository import UserRepository
from repositories.user_repository import get_database_connection


class UserControl:
    """Class which is used to control information stored in the local database which is connected to the program.
    """

    def __init__(self):
        """Constructor of the class

        Args:
            repository: instance of class UserRepository which holds a connection to the relevant database.
        """

        user_repository = get_database_connection()
        self.repository = UserRepository(user_repository)

    def create_user(self, username, password1, password2):
        """Creates a new user if the information given passes all demands. Initiates users rating at 0.

        Args:
            username (str): chosen username by the player
            password1 (_type_): chosen password of the player
            password2 (_type_): should match password1

        Returns:
            True: if username is not taken and password1 and password2 match.
        """

        if self.repository.get_by_username(username) != None:
            return False

        if password1 != password2 or None in (password1, password2):
            return False

        else:
            self.user = User(username, password1, 0)
            self.repository.create(self.user)
        return True

    def login(self, username, password):
        """Used to log in on an existing account. If username doesn't exist or password doesn't correlate with the given username it returns False.
        Args:
            username: username of the user
            password: password correlating to that account.
        Returns:
            True: if username exists and password is correct
            False: if username doesn't exist or password is wrong"""

        user = self.repository.get_by_username(username)

        if user == None:
            return False

        if user.password == password:
            self.user = user
            return True

        return False

    def update_rating(self, change):
        """Used to update the rating after a played game. If it's a win for the player increase by 15. If it's a loss decrease by 15.

        Args:
            Change: +/-15
        Returns:
            False: if user doesn't exist
            None: in other cases"""

        user = self.repository.get_by_username(self.user.username)

        if user == None:
            return False

        user.rating += change

        self.repository.update_rating(user)

    def get_top_ten(self):
        """Used to get the currently top ten rated players in the local database.

        Returns:
            list: list of user-objects with top ten user.rating
        """

        return self.repository.get_top_ten()
