# Modules

from forms.form_firstInit import User
from forms.form_master_design import masterDesign
import os

# Main

firtsinitpath = "src/saves/user.json"

if os.path.exists(firtsinitpath):
    masterDesign()
else:
    User()
