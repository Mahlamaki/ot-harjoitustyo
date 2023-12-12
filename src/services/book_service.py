from entities.book import Book
from repositories.book_repository import book_repository


class BookService:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun."""

        self._book_repository = book_repository

    def add_new_book(self, title, author, rating):
        """Luo uuden kirjan Book-olio muodossa

        Args:
            title: Merkkijonoarvo, jossa kirja nimi
            author: Merkkijonoarvo, jossa kirjoittajan nimi
            rating: Merkkijonoarvo, jossa arvosana 1-5
        """
        book = Book(title=title, author=author, rating=rating)
        self._book_repository.add(book)

    def browse_all_books(self):
        """Palauttaa kaikki kirjat"""

        return self._book_repository.browse()

    def delete_book(self, book):
        """ Poistaa halutun kirjan
        Args:
            book: Merkkijonoarvo, jossa kirja nimi
        """
        self._book_repository.delete_selected_book(book)

    def all_authors(self):
        """ Palauttaa listan kaikista tietokannan kirjailijoita"""

        return self._book_repository.get_authors()

    def all_ratings(self):
        """ Palauttaa listan kaikista tietokannan arvosanoista"""

        return self._book_repository.get_ratings()


book_service = BookService()
