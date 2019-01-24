from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Block import Block
from ..Types.Img import Img

class League(Block):
    
    def __init__(self, name):
        Block.__init__(self, name)
        self.content = {
            "leagueName" : String("League name"),
            "tier" : String("Tier", "Unranked"),
            "rank" : String("Rank"),
            "leaguePoints" : Numeric("League points"),
            "wins" : Numeric("Wins"),
            "losses" : Numeric("Losses"),
            "games" : Numeric("Games"),
            "winrate" : Numeric("Winrate"),
            "image" : Img("Rank image", "http://canisback.com/img/lol/unranked.png")
        }
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])
                
        self.content["games"].setValue(data["wins"] + data["losses"])
        self.content["winrate"].setValue( ( data["wins"] / self.content["games"].getData()["value"] ) if self.content["games"].getData()["value"] > 0 else 0)
        self.content["image"].setValue("http://canisback.com/img/lol/" + data["tier"].lower() +".png")