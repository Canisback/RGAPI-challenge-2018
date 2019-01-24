from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Block import Block

maps = {
    1: "Summoner's Rift (Original Summer)", 
    2: "Summoner's Rift (Original Autumn)", 
    3: 'The Proving Grounds', 
    4: 'Twisted Treeline (Original)',
    8: 'The Crystal Scar', 
    10: 'Twisted Treeline', 
    11: "Summoner's Rift", 
    12: 'Howling Abyss', 
    14: "Butcher's Bridge", 
    16: "Cosmic Ruins", 
    18: "Valoran City Park", 
    19: "Substructure 43", 
    20: "Crash Site", 
    21: "Nexus Blitz"
}

class Map(Block):
    
    def __init__(self):
        Block.__init__(self, "Map")
        self.content = {
            "mapId" : Numeric("Map Id"),
            "mapName" : String("Map name")
        }
        
    def setValue(self, data):
        self.content["mapId"].setValue(data)
        self.content["mapName"].setValue(maps[data])