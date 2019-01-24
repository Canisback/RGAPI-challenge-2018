from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block

class Summoner(Block):
    
    def __init__(self):
        Block.__init__(self, "Summoner")
        self.content = {
            "summonerLevel" : Numeric("Level"),
            "name" : String("Summoner name"),
            "icon" : Img("Profile icon")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
        
        self.content["icon"].setValue("http://ddragon.canisback.com/latest/img/profileicon/"+str(data["profileIconId"])+".png")