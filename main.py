# Modules

from forms.form_firstInit import User
from forms.form_home import Home
import os

# Main

firtsinitpath = "src/saves/user.json"

if os.path.exists(firtsinitpath):
    Home()
else:
    User()