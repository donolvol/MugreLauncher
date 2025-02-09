# Lib

import minecraft_launcher_lib as mc
import os
import json

# Inicio

archivo_json = "src/saves/directory.json"

user_windows = os.environ['USERNAME']

default = f"C://Users//{user_windows}//AppData//Roaming//.Launcher//.minecraft"

infolder = f"//.minecraft"

minecraft_directory = ""

exist = ""

def Directory():
    with open(archivo_json, "r") as f:
        directory_json = json.load(f)
    directory_json = minecraft_directory
    return minecraft_directory
    
def Empty_Directory():
    # Falta opción de selección
    with open(archivo_json, "w") as f:
        json.dump(default, f)
     
    Directory()

def Directory_Check():
    if os.path.exists(archivo_json):
        Directory()
    else:
        Empty_Directory()

Directory_Check()