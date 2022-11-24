from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_create_user_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _go_home(self):
        self._show_homepage_view()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(self._root,self._go_home)


    def _show_homepage_view(self):
        self._hide_current_view()

        self._current_view = HomePageView(self._root)


class CreateUserView:
    def __init__(self,root,go_home):
        self._root= root
        self._username_entry = None
        self._name_entry = None
        self._frame = None
        self._go_home =go_home
        self._initialize()

  
    def destroy(self):
        self._frame.destroy()



    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._root, text = "Luo käyttäjätunnus")
        username_label = ttk.Label(master=self._root, text= "Username")
        self._username_entry = ttk.Entry(master=self._root)

        name_label = ttk.Label(master=self._root, text="Name")
        self._name_entry = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Luo", command=self._go_home)


        label.grid(columnspan=2)
        username_label.grid(padx=40, pady=50)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=40, pady=50)
        name_label.grid(padx=40, pady=50)
        self._name_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=40, pady=50)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=40, pady=50)

        self._root.grid_columnconfigure(1, weight=1, minsize=400)
    



class HomePageView:

    def __init__(self,root):
        self._root = root
        self._frame = None
        

        self._initialize()   
    
    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._root, text = "Hei {self._name}")
  
        create_card_button = ttk.Button(master=self._root, text="Luo kortti", command=None)
        edit_cards_button = ttk.Button(master=self._root, text="Muokkaa kortteja", command=None)
        practise_button = ttk.Button(master=self._root, text="Kertaa", command=None)
        log_out_button = ttk.Button(master=self._root, text="Kirjaudu ulos", command=None)

        label.grid(columnspan=2)
        create_card_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=40, pady=50)
        edit_cards_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=40, pady=50)
        practise_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=40, pady=50)
        log_out_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=40, pady=50)
    

        self._root.grid_columnconfigure(1, weight=1, minsize=400)
window = Tk()
window.title("Kertauskamu")

ui = UI(window)
ui.start()
window.mainloop()
