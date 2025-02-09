# Modules

from src.variables.empty_variables import user, JVGArgs

# Inicio

options = {
    "username": user,
    "uuid": "",
    "token": "",
    "jvmArguments": [f"-Xmx{JVGArgs}G", f"-Xms{JVGArgs}G"],
    "server": "example.com",
    "port": "123",
    "gameDirectory": "minecraft_launcher_lib/server"
    }