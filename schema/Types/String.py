from ..Types.FinalBlock import FinalBlock

class String(FinalBlock):
    
    def __init__(self, name, value = ""):
        FinalBlock.__init__(self, name, "string")
        self.value = value