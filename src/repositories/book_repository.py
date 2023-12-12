from entities.book import Book
from database_connection import get_database_connection


def get_book_by_row(row):
    return Book(row["title"], row["author"], row["rating"]) if row else None


class BookRepository:
    """Luokka joka vastaa tietokantaoperaatioista"""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def fetch_all(self):
        """Palauttaa kaikki kirjat.

        Returns:
            Palauttaa listan Book-olioita.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from books")
        rows = cursor.fetchall()
        books = [get_book_by_row(row) for row in rows]
        return books

    def add(self, book):
        """Tallentaa kirjan tietokantaan

        Args:
            book : Book-olio, joka lisätään tietokantaan

        Returns: Book-olio

        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO books (title,author,rating) values (?, ?, ?)",
                       (book.title, book.author, str(book.rating)))
        self._connection.commit()

        return book

    def browse(self):
        """Palauttaa kaikki kirjat.

        Returns:
            Palauttaa listan Book-olioita.
        """
        books = self.fetch_all()
        return books

    def delete_selected_book(self, title):
        """Poistaa kirjan tietokannasta.

        Args:
            title : Merkkijonoarvo, kirjan nimi, jonka mukaan kirja poistetaan
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from books where title = ?", (title, ))
        self._connection.commit()

    def delete_all(self):
        """Poistaa kaikki kirjat tietokannasta."""

        cursor = self._connection.cursor()
        cursor.execute("delete from books")
        self._connection.commit()

    def get_authors(self):
        """Hakee kaikki tietokannan kirjailijat

        Returns:
            Palauttaa listan kaikista kirjailijoista (jokainen vain kerran)

        """
        cursor = self._connection.cursor()
        authors = ["Kaikki",]
        cursor.execute("select distinct author from books order by author")
        rows = cursor.fetchall()
        for book in rows:
            author = book[0]
            authors.append(author)

        return authors

    def get_ratings(self):
        """Hakee kaikki tietokannan arvosanat

        Returns:
            Palauttaa listan kaikista arvosanoista(jokainen vain kerran)

        """
        cursor = self._connection.cursor()
        ratings = ["Kaikki",]
        cursor.execute("select distinct rating from books order by rating")
        rows = cursor.fetchall()
        for book in rows:
            rating = book[0]
            ratings.append(rating)

        return ratings


book_repository = BookRepository(get_database_connection())
