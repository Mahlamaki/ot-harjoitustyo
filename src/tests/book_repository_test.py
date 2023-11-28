import unittest
from repositories.book_repository import book_repository
from entities.book import Book


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        book_repository.delete_all()
        self.testbook1 = Book("Seitsemän Veljestä", "Aleksis Kivi", 3)
        self.testbook2 = Book("Päiväkirja", "Salailija", 5)
        self.testbook3 = Book("Testikirja", "Testaaja", 2)

    def test_add_new_book(self):
        new_book = book_repository.add(self.testbook1)
        self.assertEqual(new_book.title, self.testbook1.title)

    def test_browse_books(self):
        book_repository.add(self.testbook1)
        book_repository.add(self.testbook2)
        book_repository.add(self.testbook3)

        booklist_browse = book_repository.browse()

        self.assertEqual(booklist_browse[0].title, self.testbook1.title)
        self.assertEqual(booklist_browse[2].title, self.testbook3.title)

    def test_fetch_all(self):
        book_repository.add(self.testbook1)
        book_repository.add(self.testbook2)
        book_repository.add(self.testbook3)
        booklist = book_repository.fetch_all()

        self.assertEqual(booklist[0].title, self.testbook1.title)
        self.assertEqual(booklist[1].title, self.testbook2.title)
        self.assertEqual(booklist[2].title, self.testbook3.title)
