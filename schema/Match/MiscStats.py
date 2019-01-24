from ..Types.Numeric import Numeric
from ..Types.Block import Block

class MiscStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "turretKills" : Numeric("Towers destroyed"),
            "inhibitorKills" : Numeric("Inhibitor destroyed")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                