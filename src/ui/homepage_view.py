from tkinter import ttk, constants


class HomePage:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)

        self._root.title("Kirjakerho")

        welcome_label = ttk.Label(
            master=self._root, text="Tervetuloa kirjakerhomme kirjalogiin!", font=("Helvetica", 16, "bold"))
        welcome_label.grid(row=0, column=0, columnspan=4, pady=(10, 20))

        menu_label = ttk.Label(
            master=self._root, text="Mitä haluaisit tehdä seuraavaksi?", font=("Helvetica", 12))
        menu_label.grid(row=1, column=0, columnspan=4, pady=(40, 10))

        add_book_button = ttk.Button(
            master=self._root, text="Lisää kirja logiin", command=None)
        add_book_button.grid(row=2, column=1, padx=(0, 10), pady=(10, 10))

        browse_books_button = ttk.Button(
            master=self._root, text="Selaa kirjoja", command=None)
        browse_books_button.grid(row=2, column=2, padx=(0, 10), pady=(10, 10))

        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(3, weight=1)
