from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block
from .Rune import Rune
from .Rune import RuneSA
from .RuneList import RuneList

class RunePage(Block):
    
    def __init__(self):
        Block.__init__(self, "Summoner spell")
        self.content = {
            "perkPrimaryStyle" : RuneSA("Primary style"),
            "perkSubStyle" : RuneSA("Sub style"),
            "perk0" : RuneSA("Keystone"),
            "primaryTree" : RuneList("Primary runes"),
            "subTree" : RuneList("Sub runes"),
            "stats" : RuneList("Stats")
        }
    
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                
        self.content["primaryTree"].setValue([data["perk0"],data["perk1"],data["perk2"],data["perk3"]])
        self.content["subTree"].setValue([data["perk4"],data["perk5"]])
        self.content["stats"].setValue([data["statPerk0"],data["statPerk1"],data["statPerk2"]])