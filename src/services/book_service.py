from entities.book import Book
from repositories.book_repository import book_repository


class BookService:
    def __init__(self):
        self._book_repository = book_repository

    def add_new_book(self, title, author, rating):
        book = Book(title=title, author=author, rating=rating)
        self._book_repository.add(book)

    def browse_all_books(self):
        return self._book_repository.browse()

    def delete_book(self, book):
        return self._book_repository.delete_selected_book(book)

    def all_authors(self):
        return self._book_repository.get_authors()

    def all_ratings(self):
        return self._book_repository.get_ratings()


book_service = BookService()
