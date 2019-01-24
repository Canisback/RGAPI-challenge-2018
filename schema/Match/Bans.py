from ..Types.List import List
from ..LoLTypes.Champion import Champion

class Bans(List):
    
    def __init__(self):
        List.__init__(self, "Bans", Champion)
        
        
    def setValue(self, data):
        self.content = [self._loadData(db["championId"]) for db in data]
        
    def _loadData(self, data):
        item = self.contentType()
        item.setValue(data)
        return item