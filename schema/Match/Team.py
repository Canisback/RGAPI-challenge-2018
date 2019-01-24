from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Block import Block
from ..Types.Img import Img
from .Bans import Bans
from .Players import Players
from .DamageStats import DamageStats
from .CombatStats import CombatStats
from .TankingStats import TankingStats
from .VisionStats import VisionStats
from .IncomeStats import IncomeStats
from .MiscStats import MiscStats


class Team(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "towerKills" : Numeric("Tower kills"),
            "baronKills" : Numeric("Baron kills"),
            "dragonKills" : Numeric("Dragon kills"),
            "teamId" : Numeric("Team id"),
            "win" : Numeric("Win"),
            "bans" : Bans(),
            "players" : Players(),
            "damageStats" : DamageStats("Damage stats"),
            "combatStats" : CombatStats("Combat stats"),
            "tankingStats" : TankingStats("Tanking stats"),
            "visionStats" : VisionStats("Vision stats"),
            "incomeStats" : IncomeStats("Income stats"),
            "miscStats" : MiscStats("Misc stats"),
        }
    
    def setValue(self, data):
        i = 0 if self.name == "Blue team" else 1
        for k in self.content:
            if k in data["teams"][i].keys():
                self.content[k].setValue(data["teams"][i][k])
                
        self.content["win"].setValue(0 if data["teams"][i]["win"] == "Fail" else 1)
        
        playerData = [p for p in data["participants"] if p["teamId"] == self.content["teamId"].getData()["value"]]
        for k,p in enumerate(playerData):
            playerData[k]["stats"]["gameDuration"] = data["gameDuration"]
        self.content["players"].setValue(playerData)
        
        self.setTeamStats()
        
        teamStats = self.getNeededTeamStats()
        for k,p in enumerate(playerData):
            playerData[k]["teamStats"] = teamStats
        self.content["players"].setValue(playerData)
        
        
    def setTeamStats(self):
        playersData = self.content["players"].getData()
        teamStats = {}
        listStats = ["damageStats","combatStats","tankingStats","visionStats","incomeStats","miscStats"]
        exceptionsStats = ["largestMultiKill","largestKillingSpree"]
        
        for s in listStats:
            teamStats[s] = {}
        
        for p in playersData["content"]:
            for st in listStats:
                curStats = p["content"][st]["content"]
                for s in curStats:
                    if s in teamStats[st]:
                        if s in exceptionsStats:
                            teamStats[st][s] = curStats[s]["value"] if curStats[s]["value"] > teamStats[st][s] else teamStats[st][s]
                        else:
                            teamStats[st][s] += curStats[s]["value"]
                    else:
                        teamStats[st][s]= curStats[s]["value"]
                    
        for s in listStats:
            self.content[s].setValue(teamStats[s])
            
    
    def getNeededTeamStats(self):
        neededStats = ["damageStats","combatStats","tankingStats","visionStats","incomeStats"]
        stats = {}
        for ns in neededStats:
            currentStats = self.content[ns].getData()["content"]
            for s in currentStats:
                stats[s] = currentStats[s]["value"]
        return stats