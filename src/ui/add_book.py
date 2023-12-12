from tkinter import ttk, constants
import re
from services.book_service import BookService


class AddBook:
    """ Luokka vastaa uuden kirjan luomisnäkymästä"""

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

        self._title_entry = None
        self._author_entry = None
        self._rating_entry = None
        self.label_error = None
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
            master=self._frame, text="Täytä uuden kirjan tiedot", font=("Geneva", 16, "bold"))
        title_label = ttk.Label(
            master=self._frame, text="Kirjan nimi", font=("Geneva"))
        author_label = ttk.Label(
            master=self._frame, text="Kirjoittaja", font=("Geneva"))
        rating_label = ttk.Label(
            master=self._frame, text="Arvosana", font=("Geneva"))
        self.label_error = ttk.Label(
            self._frame, foreground='red', font=("Geneva"))
        go_back_button = ttk.Button(
            master=self._frame, text="Takaisin", command=self._homepage)
        add_button = ttk.Button(
            master=self._frame, text="Tallenna", command=self._create_book)

        self._title_entry = ttk.Entry(master=self._frame, width=40)
        self._author_entry = ttk.Entry(master=self._frame, width=40)
        self._rating_entry = ttk.Entry(master=self._frame, width=40)

        valid_command = (self._frame.register(self.validate), "%P", "%V", "%W")

        self._title_entry.config(
            validate="focusout", validatecommand=valid_command)
        self._author_entry.config(
            validate="focusout", validatecommand=valid_command)
        self._rating_entry.config(
            validate="focusout", validatecommand=valid_command)

        welcome_label.pack(padx=(20, 20), pady=(10, 50))
        title_label.pack()
        self._title_entry.pack(padx=(20, 20), pady=(10, 10))
        author_label.pack()
        self._author_entry.pack(padx=(20, 20), pady=(10, 10))
        rating_label.pack()
        self._rating_entry.pack(padx=(20, 20), pady=(10, 10))
        self.label_error.pack(padx=(20, 20), pady=(10, 10))

        add_button.pack(padx=(0, 0), pady=(10, 10))
        go_back_button.pack(padx=(0, 0), pady=(10, 10))

    def _create_book(self):
        """Syötteen lähetys validoitavaksi ja lopulta hyväksytty syöte BookServicelle lisättäväksi"""

        title = self._title_entry.get()
        author = self._author_entry.get()
        rating = self._rating_entry.get()

        if not self.validate(title, "focusout", str(self._title_entry)) or \
                not self.validate(author, "focusout", str(self._author_entry)) or \
                not self.validate(rating, "focusout", str(self._rating_entry)):
            return

        if not title.strip() or not author.strip() or not rating.strip():
            self.show_message("", "Täytä kaikki kentät.", "red")
            return

        bookservice = BookService()
        bookservice.add_new_book(title, author, rating)
        self._homepage()

    def validate(self, value, reason, entry_type):
        """Uuden kirjan syötteen validointi"""

        if reason == "focusout":

            if entry_type == str(self._title_entry):
                pattern = r'^.{1,35}$'
                error_message = "Kirjan nimen tulee olla 1-35 merkkiä."
            elif entry_type == str(self._author_entry):
                pattern = r'^.{2,35}$'
                error_message = "Kirjoittajan nimessä tulee olla 2-35 merkkiä"
            elif entry_type == str(self._rating_entry):
                pattern = r'^[1-5]$'
                error_message = "Arvosanan tulee kokonaisluku 1-5."
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
        elif entry == str(self._rating_entry):
            self._rating_entry["foreground"] = color
