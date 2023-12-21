from ui.homepage import HomePageView
from ui.add_book_page import AddBook
from ui.browse_books_page import BrowseBooks
from ui.wishlist_page import Wishlist


class UI:
    """Luokka, joka vataa sovelluksen käyttöliittymästä"""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root:
                TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """

        self._root = root
        self._root.geometry("900x1000")
        self._current_view = None

    def start(self):
        """Käynnistää sovelluksen"""

        self._show_homepage_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän"""

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_homepage_view(self):
        """Siirtää etusivunäkymään"""

        self._hide_current_view()

        self._current_view = HomePageView(
            self._root, self._show_add_book, self._show_browse_books, self._show_whislist, self._close)
        self._current_view.pack()

    def _show_add_book(self):
        """Siirtää kirjanlisäysnäkymään"""

        self._hide_current_view()
        self._current_view = AddBook(self._root, self._show_homepage_view)
        self._current_view.pack()

    def _show_browse_books(self):
        """Siirtää kirjojenselausnäkymään"""

        self._hide_current_view()
        self._current_view = BrowseBooks(self._root, self._show_homepage_view)
        self._current_view.pack()

    def _show_whislist(self):
        """Siirtää toivelistanäkymään"""

        self._hide_current_view()
        self._current_view = Wishlist(self._root, self._show_homepage_view)
        self._current_view.pack()

    def _close(self):
        """Ohjelman sulkeminen"""
        self._root.destroy()
