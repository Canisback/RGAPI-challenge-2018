from ..Types.FinalBlock import FinalBlock

class Img(FinalBlock):
    
    def __init__(self, name, value = None):
        FinalBlock.__init__(self, name, "img")
        self.value = value