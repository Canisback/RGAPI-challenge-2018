class Block:
    
    def __init__(self, name):
        self.name = name
        self.t = "block"
        self.content = {}
        
        
    def getSchema(self):
        return {
            "name":self.name,
            "type":self.t,
            "content": {k:v.getSchema() for k,v in self.content.items()}
        }
        
    def getData(self):
        return {
            "name":self.name,
            "type":self.t,
            "content": {k:v.getData() for k,v in self.content.items()}
        }
        