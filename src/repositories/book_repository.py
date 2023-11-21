from entities.book import Book

class BookRepository:
    def __init__(self):

        self._temporary_books = [] #tämä korvataan jollakin reitillä tietokantaan

    def add(self, book):
        self._temporary_books.append(book)
        print(f"Tallensit kirjan nimeltä {book.title}")
        return book
    
    def browse(self):
        for book in self._temporary_books:
            print(book.title)
        return  self._temporary_books
