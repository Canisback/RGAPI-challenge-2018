from ..Types.Numeric import Numeric
from ..Types.Block import Block

class PerminStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "goldEarned" : Numeric("Gold earned per minute"),
            "totalMinionsKilled" : Numeric("Minions per minute"),
            "neutralMinionsKilled" : Numeric("Jungle per minute"),
            "cs" : Numeric("CS"),
            "kills" : Numeric("Kills per minute"),
            "deaths" : Numeric("Deaths per minute"),
            "assists" : Numeric("Assists per minute"),
            "totalDamageDealt" : Numeric("Total damage dealt per minute"),
            "totalDamageDealtToChampions" : Numeric("Damage to champions per minute")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue((data[k]/data["gameDuration"])*60)
                
        self.content["cs"].setValue(((data["totalMinionsKilled"] + data["neutralMinionsKilled"]) /data["gameDuration"])*60)