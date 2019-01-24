from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block

from static_data import ddragon

statsShards = {
    5001:{"name":"Health","image":"http://canisback.com/img/lol/perks/statmodshealthscalingicon.png"},
    5002:{"name":"Armor","image":"http://canisback.com/img/lol/perks/statmodsarmoricon.png"},
    5003:{"name":"Magic resist","image":"http://canisback.com/img/lol/perks/statmodsmagicresicon.png"},
    5005:{"name":"Attack speed","image":"http://canisback.com/img/lol/perks/statmodsattackspeedicon.png"},
    5007:{"name":"CDR","image":"http://canisback.com/img/lol/perks/statmodscdrscalingicon.png"},
    5008:{"name":"Adaptative force","image":"http://canisback.com/img/lol/perks/statmodsadaptativeforceicon.png"},
    
}

class RuneSA(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "runeId" : Numeric("Rune id"),
            "runeName" : String("Rune name"),
            "runeImage" : Img("Rune image")
            #"tooltips" : String("Rune tooltip")
        }
    
    def setValue(self, data):
        dd = ddragon.ddragon()
        self.content["runeId"].setValue(data)
        if data > 6000:
            self.content["runeName"].setValue(dd.getRune(data).name)
            self.content["runeImage"].setValue(dd.getRune(data).image)
        else:
            self.content["runeName"].setValue(statsShards[data]["name"])
            self.content["runeImage"].setValue(statsShards[data]["image"])
            

class Rune(RuneSA):
    
    def __init__(self):
        RuneSA.__init__(self, "Rune")
            