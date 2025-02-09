import tkinter as tk

import utils.util_img as util_img
import utils.util_window as util_window

class masterDesign(tk.Tk):
    def  __init__(self):
        super().__init__()
        #self.perfil= util_img.leer_imagen("FALTA IMAGEN", (256, 256))
        self.window = tk.Tk
        self.window.title("MugreLauncher")
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenmmheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.window.resizable(True, True) 
        util_window.center_window(self.window, 800, 500)
        self.window.mainloop()
    
    def config_window(self):
        self.title("MugreLauncher")
        self.iconbitmap("./assets/launcher.ico")
