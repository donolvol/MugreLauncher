# Modules

from src.variables.empty_variables import user, JVGArgs

# Variable Options

options = {
    "username": user,
    "uuid": "",
    "token": "",
    "jvmArguments": [f"-Xmx{JVGArgs}G", f"-Xms{JVGArgs}G"]
    }

