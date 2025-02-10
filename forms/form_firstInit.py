import tkinter as tk
import json
import utils.util_img as util_img
import utils.util_window as util_window
from forms.form_master_design import masterDesign

class User:
    
    def userWrite(self):
        userjson = "src/saves/user.json"
        user = self.usu.get()
        with open(userjson, "w") as f:
            json.dump(user, f)
        self.window.destroy()
        masterDesign()
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("MugreLauncher")
        self.window.iconbitmap("assets/launcher.ico")
        self.config = self.window.config(bg="#000000")
        
        frameUser = tk.Frame(self.window, width=385, height=185, padx=15, pady=15, bg="#131a21")
        
        LabelUser = tk.Label(frameUser, text="Nombre de usuario", bg="#131a21", font=("Minecraft Rus Regular", 18), fg="WHITE", anchor= "center")
 
        self.button = tk.Button(frameUser, text="Guardar", width=25, bg="#131a21", font=("Minecraft Dungeons Regular",8), fg="WHITE", command=self.userWrite)
        self.button.bind("<Return>", (lambda event: self.userWrite()))

        def max_characters(P):    
            if len(P) > 16:
                return False
            else:
                return True

        valuecharacters = self.window.register(max_characters)
        
        self.usu = tk.Entry(frameUser, bg="#131a21", bd=3, font=("Nunito Extralight", 15), fg="WHITE", justify="center", validate="key", validatecommand=(valuecharacters, "%P"))

        frameUser.pack(fill=tk.BOTH, expand=tk.TRUE, padx=15, pady=15)
        
        LabelUser.grid(row=0, column=0, padx=35, pady=8)
        
        self.usu.grid(row=1, column=0, padx=35, pady=8)
        
        self.button.grid(row=2, column=0, padx=35, pady=8)
        
        self.window.resizable(0, 0)
        util_window.center_window(self.window, 400, 200)
        self.window.mainloop()

