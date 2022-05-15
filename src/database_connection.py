import sqlite3
from sqlite3 import Error
from config import DATABASE_FILE_PATH

connection = None

try:
    connection = sqlite3.connect(DATABASE_FILE_PATH)
    connection.row_factory = sqlite3.Row
except Error as e:
    print(e)


def get_database_connection():
    return connection
