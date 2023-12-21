import unittest
from repositories.book_repository import book_repository
from services.book_service import book_service
from entities.book import Book


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        book_repository.delete_all()
        self.testbook1 = Book("00000", "Seitsemän Veljestä", "Aleksis Kivi", 3)
        self.testbook2 = Book("11111", "Päiväkirja", "Salailija", 5)
        self.testbook3 = Book("22222", "Testikirja", "Testaaja", 2)
        self.testbook4 = Book(
            "00001", "Muumilaakson tarinoita", "Tove Janson", None)
        self.testbook5 = Book("11112", "Oppikija", "Professori", None)
        self.testbook6 = Book(
            "22223", "Talo taivaansinisellä rannalla", "T.J Kulne", None)

    def test_add_new_book(self):
        new_book = book_repository.add(self.testbook1)
        self.assertEqual(new_book.title, self.testbook1.title)

    def test_fetch_all(self):
        book_repository.add(self.testbook1)
        book_repository.add(self.testbook2)
        book_repository.add(self.testbook3)
        booklist = book_repository.fetch_all()

        self.assertEqual(booklist[0].title, self.testbook1.title)
        self.assertEqual(booklist[1].title, self.testbook2.title)
        self.assertEqual(booklist[2].title, self.testbook3.title)

    def test_service_get_wishlist(self):
        book_repository.add_to_wishlist(self.testbook4)
        book_repository.add_to_wishlist(self.testbook5)
        book_repository.add_to_wishlist(self.testbook6)
        booklist = book_service.get_wishlist()
        print(booklist)

        self.assertEqual(booklist[0].title, self.testbook4.title)
        self.assertEqual(booklist[1].title, self.testbook5.title)
        self.assertEqual(booklist[2].title, self.testbook6.title)

    def test_service_add(self):
        title = "Kirjan nimi"
        author = "Kirjailija"
        rating = 1
        book = book_service.add_new_book(title, author, rating)

        self.assertEqual("Kirjan nimi", book.title)

    def test_service_add_wishlist(self):
        title = "Kirjan nimi"
        author = "Kirjailija"
        book = book_service.add_to_wishlist(title, author)

        self.assertEqual("Kirjan nimi", book.title)

    def test_service_browse(self):
        book_repository.add(self.testbook1)
        book_repository.add(self.testbook2)
        book_repository.add_to_wishlist(self.testbook5)

        book_list = book_service.browse_all_books()

        self.assertEqual(book_list[0].title, self.testbook1.title)
        self.assertEqual(book_list[1].title, self.testbook2.title)
        self.assertEqual(len(book_list), 2)

    def test_service_remove_from_wishlist(self):
        book_repository.add_to_wishlist(self.testbook4)
        book_repository.add_to_wishlist(self.testbook5)

        booklist1 = book_repository.get_all_from_wishlist()
        deleted_book_key = self.testbook4.key
        book_service.remove_from_wishlist(deleted_book_key)
        booklist2 = book_repository.get_all_from_wishlist()

        self.assertEqual(len(booklist1), len(booklist2)+1)

    def test_service_get_authors(self):
        book_repository.add(self.testbook1)
        book_repository.add(self.testbook2)
        book_repository.add(self.testbook3)
        right_list = sorted([self.testbook1.author,
                             self.testbook2.author, self.testbook3.author])
        right_list.insert(0, "Kaikki")
        final_list = [str(item) for item in right_list]

        test_list = book_service.all_authors()

        self.assertEqual(test_list, final_list)

    def test_service_get_ratings(self):
        book_repository.add(self.testbook1)
        book_repository.add(self.testbook2)
        book_repository.add(self.testbook3)
        book_repository.add_to_wishlist(self.testbook5)

        right_list = ["Kaikki", self.testbook3.rating,
                      self.testbook1.rating, self.testbook2.rating]

        test_list = book_service.all_ratings()
        print(test_list)

        self.assertEqual(test_list, right_list)

    def test_service_delete_book(self):
        book_repository.add(self.testbook1)
        book_repository.add(self.testbook2)

        booklist1 = book_repository.fetch_all()
        deleted_book_key = self.testbook1.key
        book_service.delete_book(deleted_book_key)
        booklist2 = book_repository.fetch_all()

        self.assertEqual(len(booklist1), len(booklist2)+1)
