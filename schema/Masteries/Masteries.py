from ..Types.Block import Block
from .ListMasteries import ListMasteries

class Masteries(Block):
    
    def __init__(self):
        Block.__init__(self, "Masteries")
        self.content = {
            "masteriesList" : ListMasteries()
        }
        
    
    def setValue(self, data):
        for k in self.content:
            if k in data.keys():
                self.content[k].setValue(data[k])