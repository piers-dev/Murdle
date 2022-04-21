import json
class player:
    def __init__(self, socket, name, email):
        self.sid = socket
        self.name = name
        self.email = email
        self.word = ""
        self.found = "-----"
        self.guessed = ""
        self.notpresent = ""

class gamestate:
    def __init__(self):
        self.players = {}
    
    def addPlayer(self,socket,name,email,session):
        if socket not in self.players.keys():
            self.players[session] = {'name':name,'email':email,'word':'-----','sid':socket}
        else:
            print("trying to add duplicate player")

    def getPlayers(self):
        return list(self.players.values())

    def dump(self):
        return json.dumps(self.players)
    
