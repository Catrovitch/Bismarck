from database_connection import get_database_connection


def drop_tables(connection):
    """Deletes the tables in the database.
    Args:
        connection: connection to database object
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)

    connection.commit()


def create_tables(connection):
    """Creates the tables which are used by the program.
    Args:
        connection: connection to database object
    """

    cursor = connection.cursor()

    cursor.execute("""
        create table users (
            username text primary key,
            password text,
            rating int
        );
    """)

    connection.commit()


def initialize_database():
    """Initializes a connection to the database or resets it if needed."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
