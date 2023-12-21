from tkinter import Tk, ttk, constants, Text, WORD, END, DISABLED, NORMAL, RIGHT, Y, BOTH, StringVar
from services.book_service import BookService
import re


from tkinter import ttk, constants


class Wishlist:
    """Luokka joka vastaa toivelistanäkymästä"""

    def __init__(self, root, homepage):
        """
        Luokan konstruktori. Alustaa toivelistanäkymästä vastaavan luokan

        Args:
        - root : tkinter ikkuna
        - homepage : kotisivulle navigointia varten
       """
        self._root = root
        self._frame = None
        self._homepage = homepage
        self.label_error = None
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
            master=self._frame, text="Tervetuloa toivelistanäkymään!", font=("Geneva", 16, "bold"))
        title_label = ttk.Label(
            master=self._frame, text="Kirjan nimi", font=("Geneva"))
        author_label = ttk.Label(
            master=self._frame, text="Kirjoittaja", font=("Geneva"))
        self.label_error = ttk.Label(
            self._frame, foreground='red', font=("Geneva"))
        delete_message = ttk.Label(
            master=self._frame, text="Kirjoita tähän poistettavan kirja ID", font=("Geneva", 12))

        self._title_entry = ttk.Entry(master=self._frame, width=40)
        self._author_entry = ttk.Entry(master=self._frame, width=40)
        self._delete_wishlist_entry = ttk.Entry(master=self._frame, width=40)

        go_back_button = ttk.Button(
            master=self._frame, text="Takaisin", command=self._homepage)
        add_wishlist_button = ttk.Button(
            master=self._frame, text="Lisää toivelistalle", command=self._add_to_wishlist)
        remove_wishlist_button = ttk.Button(
            master=self._frame, text="Poista toivelistalta", command=self._remove_from_wishlist)

        valid_command = (self._frame.register(self.validate), "%P", "%V", "%W")

        self._title_entry.config(
            validate="focusout", validatecommand=valid_command)
        self._author_entry.config(
            validate="focusout", validatecommand=valid_command)

        self.scroll = ttk.Scrollbar(self._frame)
        self.text = Text(self._frame, wrap=constants.WORD,
                         yscrollcommand=self.scroll.set, font=("Geneva", 14), height=10)

        self.scroll.config(command=self.text.yview)
        self.text.configure(state=constants.DISABLED)

        welcome_label.pack(padx=(20, 20), pady=(10, 50))
        title_label.pack()
        self._title_entry.pack(padx=(20, 20), pady=(10, 10))
        author_label.pack()
        self._author_entry.pack(padx=(20, 20), pady=(10, 10))
        self.label_error.pack(padx=(20, 20), pady=(10, 10))

        add_wishlist_button.pack(padx=(20, 20), pady=(10, 10))

        self.scroll.pack(side=constants.RIGHT, fill=constants.Y)
        self.text.pack(padx=(20, 20), expand=True, fill=constants.BOTH)
        go_back_button.pack(padx=(0, 0), pady=(10, 10))
        delete_message.pack(padx=(0, 10), pady=(10, 10))
        self._delete_wishlist_entry.pack(padx=(20, 20), pady=(10, 10))
        remove_wishlist_button.pack(padx=(20, 20), pady=(10, 10))

        self._show_wishlist()

    def _show_wishlist(self):
        """Näytetään toivelistalla olevat kirjat tekstikentässä"""
        wishlist = self._bookservice.get_wishlist()

        self.text.configure(state=constants.NORMAL)
        self.text.delete(1.0, constants.END)

        for book in wishlist:
            self.text.insert(
                constants.END, f"ID: {book.key}\nKirjan nimi: {book.title}\nKirjailija: {book.author}\n")
            self.text.insert(constants.END, "\n")
        self.text.configure(state=constants.DISABLED)

    def _add_to_wishlist(self):
        """Lisää kirjan toivelistalle"""
        title = self._title_entry.get()
        author = self._author_entry.get()

        if not self.validate(title, "focusout", str(self._title_entry)) or \
                not self.validate(author, "focusout", str(self._author_entry)):
            return

        if not title.strip() or not author.strip():
            self.show_message("", "Täytä kaikki kentät.", "red")
            return

        self._bookservice.add_to_wishlist(title, author)
        self._show_wishlist()

    def validate(self, value, reason, entry_type):
        """Syötteen validointi"""

        if reason == "focusout":

            if entry_type == str(self._title_entry):
                pattern = r'^.{1,35}$'
                error_message = "Kirjan nimen tulee olla 1-35 merkkiä."
            elif entry_type == str(self._author_entry):
                pattern = r'^.{2,35}$'
                error_message = "Kirjoittajan nimessä tulee olla 2-35 merkkiä"
            else:
                return True

            if re.fullmatch(pattern, value) is None:
                self.show_message(entry_type, error_message, "red")
                return False

            self.show_message(entry_type, "", "black")
            return True

    def show_message(self, entry, error="", color="black"):
        """Error viestin näyttäminen"""

        self.label_error["text"] = error

        if entry == str(self._title_entry):
            self._title_entry["foreground"] = color
        elif entry == str(self._author_entry):
            self._author_entry["foreground"] = color

    def _remove_from_wishlist(self):
        """Poistaa kirjan toivelistalta"""
        key = self._delete_wishlist_entry.get()

        if key:
            self._bookservice.remove_from_wishlist(key)
            self._show_wishlist()
