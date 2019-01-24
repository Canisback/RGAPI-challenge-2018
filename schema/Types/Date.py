from ..Types.FinalBlock import FinalBlock

class Date(FinalBlock):
    
    def __init__(self, name, value = 0):
        FinalBlock.__init__(self, name, "date")
        self.value = value