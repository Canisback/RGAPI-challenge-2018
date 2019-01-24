from ..Types.Numeric import Numeric 
from ..Types.Date import Date 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block
from .Queue import Queue
from .Map import Map
from .Team import Team
from .Player import Player

class Match(Block):
    
    def __init__(self):
        Block.__init__(self, "Match")
        self.content = {
            "queueId" : Queue(),
            "mapId" : Map(),
            "gameDuration" : Numeric("Duration"),
            "gameCreation" : Date("Creation"),
            "patch" : String("Patch"),
            "redTeam" : Team("Red team"),
            "blueTeam" : Team("Blue team"),
            "player" : Player()
        }
        
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                
        self.content["patch"].setValue(".".join(data["gameVersion"].split(".")[:2]))
        
        playerNames = {}
        for p in data["participantIdentities"]:
            playerNames[p["participantId"]] = p["player"]["summonerName"]
        for k,p in enumerate(data["participants"]):
            data["participants"][k]["name"] = playerNames[p["participantId"]]
            
        self.content["redTeam"].setValue(data)
        self.content["blueTeam"].setValue(data)
        
    def setPlayer(self, playerName):
        #print(self.content["redTeam"].content["players"].__dict__)
        for player in self.content["redTeam"].content["players"].content:
            if player.content["name"].getData()["value"] == playerName:
                self.content["player"] = player
        for player in self.content["blueTeam"].content["players"].content:
            if player.content["name"].getData()["value"] == playerName:
                self.content["player"] = player