from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block

from static_data import ddragon

class SummonerSpell(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "spellId" : Numeric("Spell id"),
            "spellName" : String("Spell name"),
            "spellImage" : Img("Spell image")
        }
    
    def setValue(self, data):
        dd = ddragon.ddragon()
        self.content["spellId"].setValue(data)
        self.content["spellName"].setValue(dd.getSummoner(data).name)
        self.content["spellImage"].setValue(dd.getSummoner(data).image)