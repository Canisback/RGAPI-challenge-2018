from ..Types.List import List
from ..Match.Match import Match

from static_data import ddragon

class ListMatch(List):
    
    def __init__(self):
        List.__init__(self, "Matches list", Match)
        
    def setPlayer(self, playerName):
        self.content = [self._loadPlayer(m,playerName) for m in self.content]
        
        
    def _loadPlayer(self, m, playerName):
        m.setPlayer(playerName)
        return m