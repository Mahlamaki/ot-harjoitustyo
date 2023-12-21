from tkinter import ttk, constants


class HomePageView:
    """Luokka joka vastaa kotisivunäkymästä"""

    def __init__(self, root, add_book, browse_books, show_whislist, close):
        """
        Luokan konstruktori. Alustaa kotisivunäkymästä vastaavan luokan

        Args:
        - root : tkinter ikkuna
        - add_book : kirjanlisäysnäkymään navigointia varten
        - browse_books : kirjojenselausnäkymään navigointia varten
        - close : sovelluksen sulkemista varten
        """
        self._root = root
        self._frame = None
        self._show_add_book = add_book
        self._show_browse_books = browse_books
        self._show_wishlist = show_whislist
        self._close = close

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(
            master=self._frame, text="Tervetuloa kirjakerhomme kirjalogiin!", font=("Geneva", 16, "bold"))
        menu_label = ttk.Label(
            master=self._frame, text="Mitä haluaisit tehdä seuraavaksi?", font=("Geneva", 14))

        add_book_button = ttk.Button(
            master=self._frame, text="Lisää uusi kirja", command=self._show_add_book)
        browse_books_button = ttk.Button(
            master=self._frame, text="Selaa login kirjoja", command=self._show_browse_books)
        wishlist_button = ttk.Button(
            master=self._frame, text="Toivekirjat", command=self._show_wishlist)
        close_button = ttk.Button(
            master=self._frame, text="Sulje", command=self._close)

        welcome_label.pack(padx=(0, 10), pady=(10, 10))
        menu_label.pack(padx=(0, 10), pady=(40, 10))
        add_book_button.pack(padx=(0, 10), pady=(60, 10))
        browse_books_button.pack(padx=(0, 10), pady=(10, 10))
        wishlist_button.pack(padx=(0, 10), pady=(10, 10))
        close_button.pack(padx=(0, 10), pady=(10, 10))
