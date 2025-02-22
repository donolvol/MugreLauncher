import tkinter as tk
import json
import utils.util_img as util_img
import utils.util_window as util_window

class User(tk.Toplevel):
    
    def userWrite(self):
        userjson = "src/saves/user.json"
        user = self.usu.get()
        with open(userjson, "w") as f:
            json.dump(user, f)
    
    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        frameUser = tk.Frame(self, width=385, height=185, padx=15, pady=15, bg="#131a21")
        
        LabelUser = tk.Label(frameUser, text="Nombre de usuario", bg="#131a21", font=("Minecraft Rus Regular", 18), fg="WHITE", anchor= "center")
 
        self.button = tk.Button(frameUser, text="Guardar", width=25, bg="#131a21", font=("Minecraft Dungeons Regular",8), fg="WHITE", command=self.userWrite)
        self.button.bind("<Return>", (lambda event: self.userWrite()))

        def max_characters(P):    
            if len(P) > 16:
                return False
            else:
                return True

        valuecharacters = self.register(max_characters)
        
        self.usu = tk.Entry(frameUser, bg="#131a21", bd=3, font=("Nunito Extralight", 15), fg="WHITE", justify="center", validate="key", validatecommand=(valuecharacters, "%P"))

        frameUser.pack(fill=tk.BOTH, expand=tk.TRUE, padx=15, pady=15)
        
        LabelUser.grid(row=0, column=0, padx=35, pady=8)
        
        self.usu.grid(row=1, column=0, padx=35, pady=8)
        
        self.button.grid(row=2, column=0, padx=35, pady=8)
        
        
    def config_window(self):
        self.title("MugreLauncher")
        self.iconbitmap("./assets/launcher.ico")
        self.resizable(0, 0)
        w, h = 400, 200
        util_window.center_window(self, w, h)

