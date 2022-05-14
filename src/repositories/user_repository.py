from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"], row["rating"]) if row else None

class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki käyttäjät.
        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.
        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.
        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen omaava käyttäjä on tietokannassa.
            Muussa tapauksessa None.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """Tallentaa käyttäjän tietokantaan.
        Args:
            todo: Tallennettava käyttäjä User-oliona.
        Returns:
            Tallennettu käyttjä User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password, rating) values (?, ?, ?)",
            (user.username, user.password, user.rating)
        )

        self._connection.commit()

        return True

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()

    def update_rating(self, user):

        cursor = self._connection.cursor()

        cursor.execute(
            "update users set rating = (?) where username = (?)",
            [user.rating, user.username]
        )

        self._connection.commit()

        return True

    def get_top_ten(self):

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM 'users' ORDER BY rating DESC LIMIT 10")

        top_ten = cursor.fetchall()

        return list(map(get_user_by_row, top_ten))


user_repository = UserRepository(get_database_connection())