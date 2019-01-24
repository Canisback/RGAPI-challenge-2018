class FinalBlock:
    
    def __init__(self, name, t):
        self.name = name
        self.t = t
        self.value = None
        
    def setValue(self, value):
        self.value = value
        
    def getSchema(self):
        return {
            "name":self.name,
            "type":self.t
        }
    
    def getData(self):
        return {
            "name":self.name,
            "type":self.t,
            "value":self.value
        }