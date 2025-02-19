# Lib

import json

# Modules

from src.variables.empty_variables import JVGArgs

# Variable Options

archivo_json = "./src/saves/user.json"

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
