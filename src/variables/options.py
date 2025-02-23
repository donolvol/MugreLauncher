# Lib

import json

# Modules

from src.variables.empty_variables import JVGArgs

# Variable Options

archivo_json = "./src/saves/user.json"

option_json = "./src/saves/options.json"

def createOptions():
    try:
        with open(archivo_json, "r") as f:
            user_json = json.load(f)
        user = user_json    
        options = {
            "username": user,
            "uuid": "",
            "token": "",
            "jvmArguments": [f"-Xmx{JVGArgs}G", f"-Xms{JVGArgs}G",
            '-Dminecraft.api.auth.host=https://nope.invalid',
            '-Dminecraft.api.account.host=https://nope.invalid',
            '-Dminecraft.api.session.host=https://nope.invalid',
            '-Dminecraft.api.services.host=https://nope.invalid'],
            }
    except FileNotFoundError:
        pass

    with open(option_json, "w") as g:
        json.dump(options, g)