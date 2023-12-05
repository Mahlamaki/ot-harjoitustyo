from tkinter import ttk, constants
from services.book_service import BookService


class AddBook:
    def __init__(self, root, homepage):
        self._root = root
        self._frame = None
        self._homepage = homepage

        self._title_entry = None
        self._author_entry = None
        self._rating_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(
            master=self._frame, text="Täytä uuden kirjan tiedot", font=("Geneva", 16, "bold"))
        title_label = ttk.Label(master=self._frame, text="Kirjan nimi")
        author_label = ttk.Label(master=self._frame, text="Kirjoittaja")
        rating_label = ttk.Label(master=self._frame, text="Arvosana")
        go_back_button = ttk.Button(
            master=self._frame, text="Takaisin", command=self._homepage)
        add_button = ttk.Button(
            master=self._frame, text="Tallenna", command=self._create_book)

        self._title_entry = ttk.Entry(master=self._frame, width=40)
        self._author_entry = ttk.Entry(master=self._frame, width=40)
        self._rating_entry = ttk.Entry(master=self._frame, width=40)

        welcome_label.pack(padx=(20, 20), pady=(10, 50))
        title_label.pack()
        self._title_entry.pack(padx=(20, 20), pady=(10, 10))
        author_label.pack()
        self._author_entry.pack(padx=(20, 20), pady=(10, 10))
        rating_label.pack()
        self._rating_entry.pack(padx=(20, 20), pady=(10, 10))

        add_button.pack(padx=(0, 0), pady=(10, 10))
        go_back_button.pack(padx=(0, 0), pady=(10, 10))

    def _create_book(self):
        title = self._title_entry.get()
        author = self._author_entry.get()
        rating = self._rating_entry.get()
        bookservice = BookService()

        bookservice.add_new_book(title, author, rating)
        self._homepage()
