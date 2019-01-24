from ..Types.Numeric import Numeric
from ..Types.Block import Block

class DamageStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "totalDamageDealt" : Numeric("Total damage dealt"),
            "physicalDamageDealt" : Numeric("Physical damage dealt"),
            "magicDamageDealt" : Numeric("Magic damage dealt"),
            "trueDamageDealt" : Numeric("True damage dealt"),
            "totalDamageDealtToChampions" : Numeric("Damage to champions"),
            "physicalDamageDealtToChampions" : Numeric("Physical damage to champions"),
            "magicDamageDealtToChampions" : Numeric("Magic damage to champions"),
            "trueDamageDealtToChampions" : Numeric("True damage to champions"),
            "damageDealtToTurrets" : Numeric("Damage to turrets"),
            "damageDealtToObjectives" : Numeric("Damage to objectives")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])