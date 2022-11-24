from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._go_home()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _go_home(self):
        self._show_homepage_view()


    def _show_homepage_view(self):
        self._hide_current_view()
        

        self._current_view = HomePageView(self._root)
      
    
class HomePageView:

    def __init__(self,root):
        self._root = root
        self._frame = None
        

        self._initialize()   
    
    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        
        self._frame = ttk.Frame(master=self._root)
        
        
  
        create_card_button = ttk.Button(master=self._root, text="Luo kortti", command=None)
        edit_cards_button = ttk.Button(master=self._root, text="Muokkaa kortteja", command=None)
        practise_button = ttk.Button(master=self._root, text="Kertaa", command=None)
        log_out_button = ttk.Button(master=self._root, text="Lopeta", command=None)

        
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
