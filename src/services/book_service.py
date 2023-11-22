from entities.book import Book
from repositories.book_repository import BookRepository

class BookService:
    
    def __init__(self,BookRepository):
        self._book_repository = BookRepository()
    
    def add_new_book(self,title, author, rating): 
        book = Book(title=title, author=author, rating=rating)
        self._book_repository.add(book)
        
    def browse_all_books(self):
        self._book_repository.browse()

book_service = BookService()