from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block

from static_data import ddragon

class Champion(Block):
    
    def __init__(self):
        Block.__init__(self, "Champion")
        self.content = {
            "championId" : Numeric("Champion id"),
            "championName" : String("Champion name"),
            "championImage" : Img("Champion image")
        }
    
    def setValue(self, data):
        dd = ddragon.ddragon()
        self.content["championId"].setValue(data)
        if data == -1:
            self.content["championName"].setValue("none")
            self.content["championImage"].setValue("http://raw.communitydragon.org/latest/plugins/rcp-fe-lol-champ-select/global/default/images/champion-grid/random-champion.png")
            
        else:
            self.content["championName"].setValue(dd.getChampion(data).name)
            self.content["championImage"].setValue(dd.getChampion(data).image)