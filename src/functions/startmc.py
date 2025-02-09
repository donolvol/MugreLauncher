# Lib

import subprocess

import minecraft_launcher_lib as mc

# Modules

from src.variables.minecraft_directory_select import Directory_Check, minecraft_directory
from src.variables.options import *

# Start

version = None

def Start():
    Directory_Check()
    
    minecraft_command = mc.command.get_minecraft_command(version, minecraft_directory, options)
    subprocess.run(minecraft_command, creationflags=subprocess.CREATE_NO_WINDOW)
