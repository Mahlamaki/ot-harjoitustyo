import hashlib
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
        Returns: Book-olio
        """
        key = self.generate_key(title, author)
        book = Book(key=key, title=title, author=author, rating=rating)
        self._book_repository.add(book)
        return book

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

    def get_wishlist(self):
        """Palauttaa kaikki toivelistan kirjat"""

        return self._book_repository.get_all_from_wishlist()

    def add_to_wishlist(self, book_title, author):
        """Luo uuden kirjan toivelistalle Book-olio muodossa

        Args:
            title: Merkkijonoarvo, jossa kirja nimi
            author: Merkkijonoarvo, jossa kirjoittajan nimi
        Returns: Book-olio
        """
        key = self.generate_key(book_title, author)
        book = Book(key=key, title=book_title, author=author, rating=None)
        self._book_repository.add_to_wishlist(book)
        return book

    def remove_from_wishlist(self, key):
        """ Poistaa halutun kirjan toivelistalta
        Args:
            book: Merkkijonoarvo, jossa kirja nimi
        """
        self._book_repository.delete_from_wishlist(key)

    def generate_key(self, title, author):
        """Generoi kirjalle avaimen"""
        # idea toteutukseen saatu Chatgpt alku
        data = f"{title}{author}"
        book_key = hashlib.md5(data.encode()).hexdigest()[:5]
        # chatgpt loppuu
        return book_key


book_service = BookService()
