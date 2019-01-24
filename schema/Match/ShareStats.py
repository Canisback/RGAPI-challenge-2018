from ..Types.Numeric import Numeric
from ..Types.Block import Block

class ShareStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "totalDamageDealt" : Numeric("Total damage dealt share"),
            "totalDamageDealtToChampions" : Numeric("Damage to champions share"),
            "physicalDamageDealtToChampions" : Numeric("Physical damage to champions share"),
            "magicDamageDealtToChampions" : Numeric("Magic damage to champions share"),
            "trueDamageDealtToChampions" : Numeric("True damage to champions share"),
            "damageDealtToTurrets" : Numeric("Damage to turrets share"),
            "damageDealtToObjectives" : Numeric("Damage to objectives share"),
            "visionScore" : Numeric("Vision score share"),
            "goldEarned" : Numeric("Gold earned share"),
            "kills" : Numeric("Kills share"),
            "deaths" : Numeric("Deaths share"),
            "assists" : Numeric("Assists share"),
            "kp" : Numeric("Kill participation"),
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data["stats"].keys():
                self.content[k].setValue(data["stats"][k] / data["teamStats"][k] if data["teamStats"][k] > 0 else 0)
        self.content["kp"].setValue((data["stats"]["kills"]+data["stats"]["assists"]) / data["teamStats"]["kills"] if data["teamStats"]["kills"]>0 else 0)
