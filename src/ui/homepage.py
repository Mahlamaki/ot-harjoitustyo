from tkinter import ttk, constants


class HomePageView:

    def __init__(self, root, add_book, browse_books, close):
        self._root = root
        self._frame = None
        self._show_add_book = add_book
        self._show_browse_books = browse_books
        self._close = close

        self._initialize()

    def pack(self):

        self._frame.pack(fill=constants.X)

    def destroy(self):
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

        welcome_label.pack(padx=(0, 10), pady=(10, 10))
        menu_label.pack(padx=(0, 10), pady=(40, 10))
        add_book_button.pack(padx=(0, 10), pady=(60, 10))
        browse_books_button.pack(padx=(0, 10), pady=(10, 10))
