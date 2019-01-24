from ..Types.Numeric import Numeric
from ..Types.String import String
from ..Types.Block import Block

class CombatStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "kills" : Numeric("Kills"),
            "deaths" : Numeric("Deaths"),
            "assists" : Numeric("Assists"),
            "kda" : Numeric("KDA"),
            "kdaString" : String("K/D/A"),
            "largestKillingSpree" : Numeric("Largest killing spree"),
            "largestMultiKill" : Numeric("Largest multikills"),
            "firstBloodKill" : Numeric("First Blood")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                
        k = self.content["kills"].getData()["value"]
        d = self.content["deaths"].getData()["value"]
        a = self.content["assists"].getData()["value"]
        self.content["kda"].setValue((k+a) if d == 0 else (k+a)/d)
        self.content["kdaString"].setValue(str(k)+"/"+str(d)+"/"+str(a))