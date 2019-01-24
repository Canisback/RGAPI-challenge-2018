from ..Types.List import List
from .Player import Player

class Players(List):
    
    def __init__(self):
        List.__init__(self, "Players", Player)