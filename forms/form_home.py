import tkinter as tk
import utils.util_img as util_img
import utils.util_window as util_window
from forms.form_master_design import masterDesign

class Home:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(1, 1)
        util_window.center_window(self.window, 800, 500) 
        self.window.mainloop()