import json

userjson = "src/saves/user.json"

def userWrite(user):
    user = None
    with open(userjson, "w") as f:
        json.dump(user, f)