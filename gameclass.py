import json
class player:
    def __init__(self, socket, name, email):
        self.sid = socket
        self.name = name
        self.word = ""
        self.found = "-----"
        self.guessed = ""
        self.notpresent = ""

class gamestate:
    def __init__(self, socket, name, email):
        self.players = [player(socket,name,email)]
    

    def dump(self):
        return json.dumps(self.players)
    
