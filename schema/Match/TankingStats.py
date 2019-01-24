from ..Types.Numeric import Numeric
from ..Types.Block import Block

class TankingStats(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "totalDamageTaken" : Numeric("Total damage taken"),
            "physicalDamageTaken" : Numeric("Physical damage taken"),
            "magicalDamageTaken" : Numeric("Magic damage taken"),
            "trueDamageTaken" : Numeric("True damage taken"),
            "totalHeal" : Numeric("Damage healed"),
            "damageSelfMitigated" : Numeric("Self mitigated damage")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])