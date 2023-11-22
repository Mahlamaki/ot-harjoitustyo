from database_connection import get_database_connection


def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE books (id SERIAL PRIMARY KEY, title TEXT, author TEXT, rating INT);""")

    connection.commit()


def initialize_database():

    connection = get_database_connection()
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
