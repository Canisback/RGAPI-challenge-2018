from ..Types.Numeric import Numeric
from ..Types.Block import Block

class IncomeStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "goldEarned" : Numeric("Gold earned"),
            "goldSpent" : Numeric("Gold spent"),
            "totalMinionsKilled" : Numeric("Minions"),
            "neutralMinionsKilled" : Numeric("Jungle"),
            "cs" : Numeric("CS")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                
        self.content["cs"].setValue(self.content["totalMinionsKilled"].getData()["value"] + self.content["neutralMinionsKilled"].getData()["value"])