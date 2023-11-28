from tkinter import Tk, ttk, constants, Text, WORD, END, DISABLED, NORMAL, RIGHT, Y, BOTH
from services.book_service import BookService

class BrowseBooks:
    def __init__(self, root, homepage):
        self._root = root
        self._frame = None
        self._homepage = homepage
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(
            master=self._frame, text="Tässä listaus tallennetuista kirjoista", font=("Geneva", 16, "bold"))

        go_back_button = ttk.Button(
            master=self._frame, text="Takaisin", command=self._homepage)

        welcome_label.pack(padx=(20, 20), pady=(10, 50))
        self.scroll = ttk.Scrollbar(self._frame)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.text = Text(self._frame, wrap=WORD, undo=True,
                         yscrollcommand=self.scroll.set, font=("Geneva", 14))
        self.text.pack(padx=(20, 20), expand=True, fill=BOTH)

        self.scroll.config(command=self.text.yview)
        self.text.configure(state=DISABLED)

        books = self._show_books()

        go_back_button.pack(padx=(0, 0), pady=(10, 10))

    def _show_books(self):
        bookservice = BookService()
        books = bookservice.browse_all_books()

        self.text.configure(state=NORMAL)
        self.text.delete(1.0, END)

        for book in books:
            self.text.insert(
                END, f"Kirjan nimi: {book.title}\nKirjailija: {book.author}\nArvosana: {book.rating}\n")
            self.text.insert(END, "\n")
        self.text.configure(state=DISABLED)

        return books 
