from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block

from static_data import ddragon

class Mastery(Block):
    
    def __init__(self):
        Block.__init__(self, "Mastery")
        self.content = {
            "championId" : Numeric("Champion Id"),
            "championName" : String("Champion name"),
            "championIcon" : Img("Champion icon"),
            "championLevel" : Numeric("Mastery level"),
            "championPoints" : Numeric("Mastery points"),
            "chestGranted" : Numeric("Chest granted"),
            "championPointsUntilNextLevel" : Numeric("Points to next level"),
            "image" : Img("Icon")
        }
        
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                
        dd = ddragon.ddragon()
        self.content["championName"].setValue(dd.getChampion(data["championId"]).name)
        self.content["championIcon"].setValue(dd.getChampion(data["championId"]).image)
        self.content["image"].setValue("http://forum.canisback.com/img/level_"+str(data["championLevel"])+".png")