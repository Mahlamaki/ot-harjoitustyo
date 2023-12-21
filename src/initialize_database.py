from database_connection import get_database_connection


def drop_tables(connection):
    """ Poista kaikki taulut tietokannasta"""

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists books;
    """)

    connection.commit()


def create_tables(connection):
    """Luo sovelluksen tietokantataulut.

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute(
    """
    create table books (
        id SERIAL PRIMARY KEY,
        key TEXT,
        title TEXT,
        author TEXT,
        rating INT,
        wishlist TEXT CHECK (wishlist IN ('True', 'False'))
    );
    """
)

    connection.commit()

    cursor = connection.cursor()


def initialize_database():
    """Alustaa sovelluksen tietokantataulut"""

    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
