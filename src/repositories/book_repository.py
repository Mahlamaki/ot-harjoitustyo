from entities.book import Book
from database_connection import get_database_connection


def get_book_by_row(row):
    return Book(row["key"], row["title"], row["author"], row["rating"]) if row else None


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
        cursor.execute("select * from books where wishlist = ?", ("False", ))
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

        cursor.execute(
            "insert into books (key,title,author,rating,wishlist) values (?, ?, ?, ?, ?)",
            (book.key, book.title, book.author, str(book.rating), "False"))
        self._connection.commit()

        return book

    def browse(self):
        """Palauttaa kaikki kirjat.

        Returns:
            Palauttaa listan Book-olioita.
        """
        books = self.fetch_all()
        return books

    def delete_selected_book(self, key):
        """Poistaa kirjan tietokannasta.

        Args:
            title : Merkkijonoarvo, kirjan avain, jonka mukaan kirja poistetaan
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "delete from books where key = ? and wishlist = ?", (key, "False"))
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
        cursor.execute(
            "select distinct author from books where wishlist = ? order by author", ("False", ))
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
            if rating is not None:
                ratings.append(rating)

        return ratings

    def get_all_from_wishlist(self):
        """Palauttaa kaikki kirjat toivelistalta.

        Returns:
            Palauttaa listan kirjannimiä
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from books where wishlist = ?", ("True", ))
        rows = cursor.fetchall()
        books = [get_book_by_row(row) for row in rows]
        return books

    def add_to_wishlist(self, book):
        """Tallentaa kirjan nimen ja kirjoittajan tietokantaan

        Args:
            book : Book-olio, joka lisätään tietokantaan

        Returns: Book-olio

        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO books (key, title, author, rating, wishlist) "
            "VALUES (?, ?, ?, ?, ?)",
            (book.key, book.title, book.author, book.rating, "True")
        )

        return book

    def delete_from_wishlist(self, key):
        """Poistaa kirjan toivelistalta.

        Args:
            title : Merkkijonoarvo, kirjan avain, jonka mukaan kirja poistetaan
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "delete from books where key = ? and wishlist = ?", (key, "True"))
        self._connection.commit()


book_repository = BookRepository(get_database_connection())
