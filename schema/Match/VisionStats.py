from ..Types.Numeric import Numeric
from ..Types.Block import Block

class VisionStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "visionScore" : Numeric("Vision score"),
            "wardsPlaced" : Numeric("Wards placed"),
            "wardsKilled" : Numeric("Wards killed"),
            "visionWardsBoughtInGame" : Numeric("Control Wards purchased")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])