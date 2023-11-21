from tkinter import Tk, ttk, constants
from services.book_service import BookService

class UI:
    def __init__(self, root):
        self._root = root
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
        

        self._current_view = HomePageView(self._root,self._show_add_book,self._close)
        self._current_view.pack()

    def _show_add_book(self):
        self._hide_current_view()
        

        self._current_view = AddBook(self._root,self._homepage)
        self._current_view.pack()
        
    def _close(self):
        self._root.destroy()        



      
    
class HomePageView:

    def __init__(self,root,add_book, close):
        self._root = root
        self._frame = None
        self._show_add_book = add_book
        self._close = close
        

        self._initialize()  


    def pack(self):

        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(master=self._frame, text="Tervetuloa kirjakerhomme kirjalogiin!", font=("Helvetica", 16, "bold"))
        menu_label = ttk.Label(master=self._frame, text="Mitä haluaisit tehdä seuraavaksi?", font=("Helvetica", 14))
  
        add_book_button = ttk.Button(master=self._frame, text="Lisää uusi kirja", command = self._show_add_book)
        browse_books_button = ttk.Button(master=self._frame, text="Selaa login kirjoja")


        welcome_label.pack(padx=(0, 10), pady=(10, 10))
        menu_label.pack(padx=(0, 10), pady=(40, 10))
        add_book_button.pack(padx=(0, 10), pady=(60, 10))
        browse_books_button.pack(padx=(0, 10), pady=(10, 10))
        
        
class AddBook:
    def __init__(self,root,homepage):
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
        welcome_label = ttk.Label(master=self._frame, text="Täytä uuden kirjan tiedot", font=("Helvetica", 16, "bold"))
        title_label = ttk.Label(master=self._frame, text = "Kirjan nimi")
        author_label = ttk.Label(master=self._frame, text="Kirjoittaja")
        rating_label = ttk.Label(master=self._frame, text="Arvosana")        
        go_back_button = ttk.Button(master=self._frame, text="Takaisin", command=self._homepage)
        add_button = ttk.Button(master=self._frame, text="Tallenna", command=self._create_book)

        self._title_entry=ttk.Entry(master=self._frame,width=40)
        self._author_entry=ttk.Entry(master=self._frame,width=40)
        self._rating_entry=ttk.Entry(master=self._frame,width=40)
        
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
        bookservice =BookService()
        
        bookservice.add_new_book(title, author, rating)
        self._homepage()
        
