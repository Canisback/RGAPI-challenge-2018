from ..Types.FinalBlock import FinalBlock

class Numeric(FinalBlock):
    
    def __init__(self, name, value = 0.):
        FinalBlock.__init__(self, name, "numeric")
        self.value = value
        if type(value) == bool:
            self.value = int(value)
        