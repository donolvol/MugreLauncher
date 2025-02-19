# Lib

import minecraft_launcher_lib as mc
import json
import os

# Inicio

archivo_json = "src/saves/directory.json"

user_windows = os.environ['USERNAME']

default = mc.utils.get_minecraft_directory()

infolder = f"./.minecraft"

def Directory():
    with open(archivo_json, "r") as f:
        directory_json = json.load(f)
    minecraft_directory = directory_json
    if os.path.exists(minecraft_directory):
        pass
    else:
        os.makedirs(minecraft_directory)
    
def Empty_Directory():
    # Falta opción de selección
    with open(archivo_json, "w") as f:
        json.dump(infolder, f)
     
    Directory()

def Directory_Check():
    if os.path.exists(archivo_json):
        Directory()
    else:
        Empty_Directory()
