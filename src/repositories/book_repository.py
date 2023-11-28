from entities.book import Book
from database_connection import get_database_connection


def get_book_by_row(row):
    return Book(row["title"], row["author"], row["rating"]) if row else None


class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def fetch_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from books")
        rows = cursor.fetchall()
        books = [get_book_by_row(row) for row in rows]
        return books

    def add(self, book):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO books (title,author,rating) values (?, ?, ?)",
                       (book.title, book.author, book.rating))
        self._connection.commit()
        print(f"Tallensit kirjan nimeltä {book.title}")
        return book

    def browse(self):
        books = self.fetch_all()
        return books

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute("delete from books")

        self._connection.commit()


book_repository = BookRepository(get_database_connection())
