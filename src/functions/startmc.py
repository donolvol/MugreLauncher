# Lib

import subprocess
import json
import minecraft_launcher_lib as mc

# Modules

from src.variables.minecraft_directory_select import Directory_Check
from src.variables.options import options

# Start

versionid = "1.16.5"

def Install():
    Directory_Check()
    
    archivo_json = "src/saves/directory.json"
    with open(archivo_json, "r") as f:
        directory_json = json.load(f)
    minecraft_directory = directory_json
    versionforge = mc.forge.find_forge_version(versionid)
    mc.install.install_minecraft_version(versionid, minecraft_directory)
    mc.forge.install_forge_version(versionforge, minecraft_directory)

def Start():
    Directory_Check()
    archivo_json = "src/saves/directory.json"
    with open(archivo_json, "r") as f:
        directory_json = json.load(f)
    minecraft_directory = directory_json    
    minecraft_command = mc.command.get_minecraft_command("1.16.5", minecraft_directory, options)
    subprocess.run(minecraft_command)
