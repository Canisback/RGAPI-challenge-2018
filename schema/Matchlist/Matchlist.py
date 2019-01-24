from .ListMatch import ListMatch
from ..Types.Block import Block

class Matchlist(Block):
    
    def __init__(self):
        Block.__init__(self, "Matchlist")
        self.t = "block"
        self.content = {
            "matchlist":ListMatch()
        }
    
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                
                
    def setPlayer(self, playerName):
        self.content["matchlist"].setPlayer(playerName)