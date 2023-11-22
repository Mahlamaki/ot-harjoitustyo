import unittest
from repositories.book_repository import BookRepository
from entities.book import Book


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.book_repository = BookRepository()
        self.testbook = Book("Seitsemän Veljestä", "Aleksis Kivi", 3)

    def test_creating_new_book_works_correctly(self):
        new_book = self.book_repository.add(self.testbook)
        self.assertEqual(new_book, self.testbook)
