from ..Types.List import List
from .Rune import Rune

class RuneList(List):
    
    def __init__(self, name):
        List.__init__(self, name, Rune)