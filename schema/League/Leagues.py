from .League import League
from ..Types.Block import Block

class Leagues(Block):
    
    def __init__(self):
        Block.__init__(self, "League")
        self.t = "block"
        self.content = {
            "RANKED_SOLO_5x5":League("Ranked Solo 5x5"),
            "RANKED_FLEX_SR":League("Ranked Flex 5x5"),
            "RANKED_FLEX_TT":League("Ranked Flex 3x3"),
        }
    
    
    def setValue(self, data):
        for dl in data:
            self.content[dl["queueType"]].setValue(dl)