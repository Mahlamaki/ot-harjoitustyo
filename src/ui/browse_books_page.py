from tkinter import Tk, ttk, constants, Text, WORD, END, DISABLED, NORMAL, RIGHT, Y, BOTH, StringVar
from tkinter import simpledialog
from services.book_service import BookService


class BrowseBooks:
    """Luokka joka vastaa kirjojen selausnäkymästä"""

    def __init__(self, root, homepage):
        """
        Luokan konstruktori. Alustaa AddBook näkymästä vastaavan luokan

        Args:
        - root : tkinter ikkuna
        - homepage : kotisivulle navigointia varten
        """

        self._root = root
        self._frame = None
        self._homepage = homepage
        self._bookservice = BookService()
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
            master=self._frame, text="Tässä listaus tallennetuista kirjoista", font=("Geneva", 16, "bold"))
        go_back_button = ttk.Button(
            master=self._frame, text="Takaisin", command=self._homepage)
        # Chatgpt- ajatus saatu chatgpt (tarkemmin Combobox toiminta), koodia muutettu ja siihe non tehty omia lisäyksiä, alkaa
        author_filter_label = ttk.Label(
            master=self._frame, text="Valitse kirjailija:")
        self._author_var = StringVar()
        authors = self._bookservice.all_authors()
        author_dropdown = ttk.Combobox(
            master=self._frame, textvariable=self._author_var, values=authors)
        author_dropdown.set("Kaikki")

        rating_filter_label = ttk.Label(
            master=self._frame, text="Valitse arvosana:")
        self._rating_var = StringVar()
        ratings = self._bookservice.all_ratings()
        rating_dropdown = ttk.Combobox(
            master=self._frame, textvariable=self._rating_var, values=ratings)
        rating_dropdown.set("Kaikki")
        filter_button = ttk.Button(
            master=self._frame, text="Suodata", command=self._filter_books)
        # Chatgpt- ajatus saatu chatgpt, koodia muutettu, loppuu

        self.scroll = ttk.Scrollbar(self._frame)
        self.text = Text(self._frame, wrap=WORD, undo=True,
                         yscrollcommand=self.scroll.set, font=("Geneva", 14), height=20)

        self.scroll.config(command=self.text.yview)
        self.text.configure(state=DISABLED)

        delete_message = ttk.Label(
            master=self._frame, text="Kirjoita tähän poistettavan kirja ID", font=("Geneva", 12))
        self._delete_book_entry = ttk.Entry(master=self._frame, width=40)
        delete_button = ttk.Button(
            master=self._frame, text="Poista", command=self._delete)

        welcome_label.pack(padx=(20, 20), pady=(10, 50))
        self.scroll.pack(side=RIGHT, fill=Y)
        author_filter_label.pack(padx=(20, 20), pady=(0, 10))
        author_dropdown.pack(padx=(20, 20), pady=(10, 10))
        rating_filter_label.pack(padx=(20, 20), pady=(10, 10))
        rating_dropdown.pack(padx=(20, 20), pady=(10, 10))
        filter_button.pack(padx=(20, 20), pady=(10, 10))
        self.text.pack(padx=(20, 20), expand=True, fill=BOTH)
        go_back_button.pack(padx=(0, 0), pady=(10, 10))
        delete_message.pack(padx=(0, 10), pady=(10, 10))
        self._delete_book_entry.pack(padx=(20, 20), pady=(10, 10))
        delete_button.pack(padx=(0, 0), pady=(10, 10))

        self._show_books()

    def _show_books(self):
        """ Näytetään tietokannassa olevat kirjat tekstikentässä"""

        # Chatgpt- ajatus saatu chatgpt, koodia muutettu alkaa
        if getattr(self, '_filter_used', False):
            self._filter_books()
        # Chatgpt- ajatus saatu chatgpt, koodia muutettu loppuu
        else:

            books = self._bookservice.browse_all_books()

            self.text.configure(state=NORMAL)
            self.text.delete(1.0, END)

            for book in books:
                self.text.insert(
                    END, f"ID: {book.key}\nKirjan nimi: {book.title}\nKirjailija: {book.author}\nArvosana: {book.rating}\n")
                self.text.insert(END, "\n")
            self.text.configure(state=DISABLED)

        books = self._bookservice.browse_all_books()

    def _delete(self):
        """ Poistetaan haluttu kirja kirjan nimen mukaan tietokannasta ja ikkunanäkymästä"""

        key = self._delete_book_entry.get()
        if key:
            bookservice = BookService()
            books = bookservice.browse_all_books()
            deleted = False

            for book in books:
                if book.key == key:
                    bookservice.delete_book(book.key)
                    deleted = True
                    break

            if deleted:
                self._show_books()
            else:
                print("Kirjaa ei löytynyt ID:llä {key}")

    def _filter_books(self):
        """Mahdollistaa kirjojen filtteröinnin joko arvosanan tai kirjoittajan mukaan"""

        # hain tkinteriin liittyen ideoita Chatgpt:stä, koodia muutettu, alku
        author = self._author_var.get()
        rating = self._rating_var.get()
        books = self._bookservice.browse_all_books()
        self.text.configure(state=NORMAL)
        self.text.delete(1.0, END)

        for book in books:
            if (author == "Kaikki" or not author or book.author == author) and \
                    (rating == "Kaikki" or not rating or str(book.rating) == str(rating)):
                self.text.insert(
                    END, f"Kirjan nimi: {book.title}\nKirjailija: {book.author}\nArvosana: {book.rating}\n")
                self.text.insert(END, "\n")

        self.text.configure(state=DISABLED)
        # hain tkinteriin liittyen ideoita Chatgpt:stä, koodia muutettu, loppu
