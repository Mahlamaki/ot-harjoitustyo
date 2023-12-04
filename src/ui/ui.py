from ui.homepage import HomePageView
from ui.add_book import AddBook
from ui.browse_books_page import BrowseBooks


class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x900")
        self._current_view = None

    def start(self):
        self._homepage()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _homepage(self):
        self._hide_current_view()
        self._show_homepage_view()

    def _show_homepage_view(self):
        self._hide_current_view()

        self._current_view = HomePageView(
            self._root, self._show_add_book, self._show_browse_books, self._close)
        self._current_view.pack()

    def _show_add_book(self):
        self._hide_current_view()
        self._current_view = AddBook(self._root, self._homepage)
        self._current_view.pack()

    def _show_browse_books(self):
        self._hide_current_view()
        self._current_view = BrowseBooks(self._root, self._homepage)
        self._current_view.pack()

    def _close(self):
        self._root.destroy()
