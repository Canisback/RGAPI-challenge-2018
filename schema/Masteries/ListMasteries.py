from ..Types.List import List
from .Mastery import Mastery

class ListMasteries(List):
    
    def __init__(self):
        List.__init__(self, "Masteries list", Mastery)