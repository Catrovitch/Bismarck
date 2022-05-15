from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"], row["rating"]) if row else None


class UserRepository:
    """A class which controls the information that is stored about users in local sqlite database.

    Attributes:
        connection: connection to a sql database on the local computer.
    """

    def __init__(self, connection):
        """The constructor of the class.
        Args:
            connection: connection to the database-object.
        """

        self._connection = connection

    def get_all_users(self):
        """Returns a list of the user-objects found in the local database.
        Returns:
            List of user-objects.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def get_by_username(self, username):
        """Find a user according to username.
        Args:
            username: username attribute of a User-object.
        Returns:
            User-object corresponding to the searched for username.
            If no User with said username exist in the local database it returns None.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """Saves information about a new user in the local database.
        Args:
            user: User-object.
        Returns:
            True.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password, rating) values (?, ?, ?)",
            (user.username, user.password, user.rating)
        )

        self._connection.commit()

        return True

    def delete_all(self):
        """Deletes all users from the database. I.E. resetting it.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()

    def update_rating(self, user):
        """Updates the rating for a user to the current rating of that user.

        Args:
            user (class): User-object with already updated current rating.

        Returns:
            True
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "update users set rating = (?) where username = (?)",
            [user.rating, user.username]
        )

        self._connection.commit()

        return True

    def get_top_ten(self):
        """Get the top ten highest rated players found in the local database.

        Returns:
            list of user-objects.
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM 'users' ORDER BY rating DESC LIMIT 10")

        top_ten = cursor.fetchall()

        return list(map(get_user_by_row, top_ten))


user_repository = UserRepository(get_database_connection())
