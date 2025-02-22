import tkinter as tk
from utils.util_window import center_window
import utils.util_img as util_img
import utils.util_window as util_window

class FormProfiles(tk.Toplevel):
    def __init__(self, principal_panel):
        self.CreateWidgets(principal_panel)

    def CreateWidgets(self, principal_panel):
        self.upbarProfile = tk.Frame(principal_panel, height="75", width="1")
        self.upbarProfile.pack(side=tk.TOP, fill=tk.X)

        self.CreateProfile = tk.Button(self.upbarProfile, width="25", bg="BLUE")
        self.CreateProfile.pack(pady="10")