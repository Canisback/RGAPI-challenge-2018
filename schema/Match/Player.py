from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block

from ..LoLTypes.Champion import Champion
from ..LoLTypes.SummonerSpell import SummonerSpell
from .ItemList import ItemList
from ..LoLTypes.RunePage import RunePage

from .DamageStats import DamageStats
from .CombatStats import CombatStats
from .TankingStats import TankingStats
from .VisionStats import VisionStats
from .IncomeStats import IncomeStats
from .MiscStats import MiscStats
from .PerminStats import PerminStats
from .ShareStats import ShareStats


class Player(Block):
    
    def __init__(self):
        Block.__init__(self, "Player")
        self.content = {
            "name" : String("Summoner name"),
            "highestAchievedSeasonTier" : String("Rank", "Unranked"),
            "rankImage" : Img("Rank image", "http://canisback.com/img/lol/unranked.png"),
            "participantId" : Numeric("Participant id"),
            "championId" : Champion(),
            "championLevel" : Numeric("Champion level"),
            "win" : Numeric("Win"),
            "runes" : RunePage(),
            "spell1Id" : SummonerSpell("Summoner spell 1"),
            "spell2Id" : SummonerSpell("Summoner spell 2"),
            "items" : ItemList(),
            "damageStats" : DamageStats("Damage stats"),
            "combatStats" : CombatStats("Combat stats"),
            "tankingStats" : TankingStats("Tanking stats"),
            "visionStats" : VisionStats("Vision stats"),
            "incomeStats" : IncomeStats("Income stats"),
            "miscStats" : MiscStats("Misc stats"),
            "perminStats" : PerminStats("Stats per minute"),
            "shareStats" : ShareStats("Stats share")
        }
        
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
        
        self.content["items"].setValue([data["stats"]["item"+str(i)] for i in range(0,7)])
        self.content["win"].setValue(data["stats"]["win"])
        self.content["damageStats"].setValue(data["stats"])
        self.content["combatStats"].setValue(data["stats"])
        self.content["tankingStats"].setValue(data["stats"])
        self.content["visionStats"].setValue(data["stats"])
        self.content["incomeStats"].setValue(data["stats"])
        self.content["miscStats"].setValue(data["stats"])
        self.content["perminStats"].setValue(data["stats"])
        
        self.content["runes"].setValue(data["stats"])
        self.content["championLevel"].setValue(data["stats"]["champLevel"])
        
        if "teamStats" in data:
            self.content["shareStats"].setValue({"stats":data["stats"],"teamStats":data["teamStats"]})
            
        
        if "highestAchievedSeasonTier" in data:
            self.content["rankImage"].setValue("http://canisback.com/img/lol/" + data["highestAchievedSeasonTier"].lower() +".png")
        