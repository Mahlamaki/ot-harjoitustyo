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
        self._hide_current_view()
        self._show_homepage_view()


    def _show_homepage_view(self):
        self._hide_current_view()
        

        self._current_view = HomePageView(self._root,self._show_new_card_view,self._show_edit_view,self._show_practise_view,self._close)
        self._current_view.pack()

    def _show_new_card_view(self):
        self._hide_current_view()
        

        self._current_view = NewCardView(self._root,self._go_home,self._show_edit_view)
        self._current_view.pack()

    def _show_edit_view(self):
        self._hide_current_view()
        

        self._current_view = EditCardView(self._root, self._show_homepage_view)   
        self._current_view.pack() 

    def _show_practise_view(self):
        self._hide_current_view()
        

        self._current_view = PractiseView(self._root, self._show_homepage_view)  
        self._current_view.pack()  

    
    def _close(self):
        self._root.destroy()
      
    
class HomePageView:

    def __init__(self,root,new_card,edit,practise,close):
        self._root = root
        self._frame = None
        self._go_new_card=new_card
        self._go_edit = edit
        self._go_practise =practise
        self._close = close
        

        self._initialize()  


    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        
        self._frame = ttk.Frame(master=self._root)
        
        
  
        create_card_button = ttk.Button(master=self._frame, text="Luo kortti", command=self._go_new_card)
        edit_cards_button = ttk.Button(master=self._frame, text="Muokkaa kortteja", command=self._go_edit)
        practise_button = ttk.Button(master=self._frame, text="Kertaa", command=self._go_practise)
        log_out_button = ttk.Button(master=self._frame, text="Lopeta", command=self._close)

        
        create_card_button.pack(padx=50, pady=50)
        edit_cards_button.pack(padx=50, pady=50)
        practise_button.pack(padx=50, pady=50)
        log_out_button.pack(padx=50, pady=50)

       

class NewCardView:
    def __init__(self,root,go_home,card_list):
        self._root = root
        self._frame = None
        self._go_home = go_home
        self._card_list = card_list
        self._question_entry = None
        self._answer_entry = None
        self._initialize()   

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        question_label = ttk.Label(master=self._frame, text = "Kirjoita kysymys")
        answer_label = ttk.Label(master=self._frame, text="Kirjoita vastaus")
        
        back_home_button = ttk.Button(master=self._frame, text="Takaisin", command=self._go_home)
        save_button = ttk.Button(master=self._frame, text="Tallenna", command=self._card_list)

        
        self._question_entry=ttk.Entry(master=self._frame,width=40)
        self._answer_entry=ttk.Entry(master=self._frame,width=40)
        
        question_label.pack()
        self._question_entry.pack(padx=100, pady=100)
        answer_label.pack()
        self._answer_entry.pack(padx=100, pady=100)  
        back_home_button.pack(side=constants.LEFT)
        save_button.pack(side=constants.RIGHT)

        self._frame.grid_columnconfigure(0, weight=1)



class EditCardView:
    def __init__(self,root,go_home):
        self._root = root
        self._frame = None
        self._go_home = go_home
        self._initialize()   

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text = "Tähän tulee lista luoduista korteista,joita klikkaamalla pääsee muokkaamaan niitä tai poistamaan ne")
        back_home_button = ttk.Button(master=self._frame, text="Takaisin", command=self._go_home)
        label.pack()
        back_home_button.pack(side=constants.LEFT)


class PractiseView:
    def __init__(self,root,go_home):
        self._root = root
        self._frame = None
        self._go_home = go_home
        self._initialize()   

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text = "Luultavasti pitää jakaa kolmeen osaan (näyttö kysymykselle, ")
        label2 = ttk.Label(master=self._frame, text = "näyttö vastaukselle, ja näyttö että kysymykset ovat loppuneet")
        back_home_button = ttk.Button(master=self._frame, text="Lopeta kertaus", command=self._go_home)
        label.pack()
        label2.pack()
        back_home_button.pack(side=constants.LEFT)

window = Tk()
window.geometry("700x550")
window.title("Kertauskamu")
ui = UI(window)
ui.start()
window.mainloop()
