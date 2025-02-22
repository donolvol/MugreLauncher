import tkinter as tk
from tkinter import font
from tkinter import ttk

from src.functions.startmc import *
import utils.util_img as util_img
import utils.util_window as util_window
from forms.form_profiles import FormProfiles
from forms.form_firstInit import User

class masterDesign(tk.Tk):
    def  __init__(self):
        super().__init__()
        self.perfil= util_img.leer_imagen("./assets/img/add.png", (42, 42))
        self.menu= util_img.leer_imagen("./assets/img/menu.png", (42, 42))
        self.home = util_img.leer_imagen("./assets/img/home.png", (42, 42))
        self.installations = util_img.leer_imagen("./assets/img/installations.png", (42, 42))
        self.settingimg = util_img.leer_imagen("./assets/img/settingimg.png", (42, 42))
        self.rosaimg = util_img.leer_imagen("./assets/img/LARO.png", (854, 480))
        self.icono = "./assets/launcher.ico"      
        self.config_window()
        self.panels()
        self.homeWidgets()
        self.sidebarbuttons()
        self.mainloop()
    
    def config_window(self):
        self.title("MugreLauncher")
        self.iconbitmap("./assets/launcher.ico")
        w, h = 1024, 600
        util_window.center_window(self, w, h)

    def panels(self):
        self.sidebar = tk.Frame(self, width=175, bg="BLACK")
        self.upbar = tk.Frame(self.sidebar, width=64, bg="BLACK", height=1)
        self.sidebarwidgets = tk.Frame(self.sidebar, width=175, bg="BLACK")
        self.sidebarwidgetsmini = tk.Frame(self.sidebar, width=64, bg="BLACK")
        self.sidebar.pack(side=tk.LEFT, fill=tk.BOTH)
        self.upbar.pack(side=tk.TOP, anchor="w", fill="x")
        self.sidebarwidgets.pack(side=tk.LEFT, fill=tk.BOTH)

        self.body = tk.Frame(self, bg="RED")
        self.body.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.TRUE)

    def toggle_panel(self):
        if self.sidebarwidgets.winfo_ismapped():
            self.sidebarwidgets.pack_forget()
            self.sidebarwidgetsmini.pack(side=tk.LEFT, fil=tk.BOTH)
        else:
            self.sidebarwidgetsmini.pack_forget()
            self.sidebarwidgets.pack(side=tk.LEFT, fill="y")
    
    def homeWidgets(self):
        self.Laroimagen = tk.Label(self.body, image=self.rosaimg, width="1", height="1")
        self.Laroimagen.pack(expand=tk.TRUE, fill=tk.BOTH)
        
        self.playButton = tk.Button(self.body)

        ancho_menu = 128
        alto_menu = 128
        
        button_info = [
            ("Play", "", self.playButton, self.mcStart, tk.BOTTOM, tk.BOTH),
        ]
        for text, icon, button, commandButton, side, fill in button_info:
            self.config_button_menu(button, text, icon, commandButton, side, fill, ancho_menu, alto_menu)
        
    def sidebarbuttons(self):
        
        ancho_menu = 128
        alto_menu = 128

        self.sidebarhideButton = tk.Button(self.upbar)
        self.homeButton = tk.Button(self.sidebarwidgets)
        self.insButton = tk.Button(self.sidebarwidgets)
        self.settingButton = tk.Button(self.sidebarwidgets)

        self.homeButtonmini = tk.Button(self.sidebarwidgetsmini)
        self.insButtonmini = tk.Button(self.sidebarwidgetsmini)
        self.settingButtonmini = tk.Button(self.sidebarwidgetsmini)

        button_info = [
            ("", self.menu, self.sidebarhideButton, self.toggle_panel, tk.TOP, tk.Y),
            ("Inicio", self.home, self.homeButton, self.homePanel, tk.TOP, tk.BOTH),
            ("Instalaciones", self.installations, self.insButton, self.InstallationsPanel, tk.TOP, tk.BOTH),
            ("Configs", self.settingimg, self.settingButton, self.configPanel, tk.BOTTOM, tk.BOTH),

            ("", self.home, self.homeButtonmini, "", tk.TOP, tk.BOTH),
            ("", self.installations, self.insButtonmini, "", tk.TOP, tk.BOTH),
            ("", self.settingimg, self.settingButtonmini, "", tk.BOTTOM, tk.BOTH)
        ]

        for text, icon, button, commandButton, side, fill in button_info:
            self.config_button_menu(button, text, icon, commandButton, side, fill, ancho_menu, alto_menu)

    def mcStart(self):
        Start()
    
    def bind_hover_event(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
    
    def on_enter(self, event, button):
        button.config(bg="BLUE")

    def on_leave(self, event, button):
        button.config(bg="WHITE")

    def config_button_menu(self, button, text, icon, commandButton, side, fill, ancho_menu, alto_menu):
        button.config(anchor="w",text=f"{text}", bd=0, font=("Minecraft Dungeons Regular",9), command=commandButton)
        button.config(anchor="w",image=f"{icon}", compound=tk.LEFT, padx=5, pady=5)
        button.pack(anchor="w", side=side, fill=fill, pady=10, padx=20)
        self.bind_hover_event(button)

    def homePanel(self):
        self.limpiar_panel(self.body)
        self.homeWidgets()

    def InstallationsPanel(self):
        self.limpiar_panel(self.body)
        FormProfiles(self.body)

    def configPanel(self):
        User(self.frameUser)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()