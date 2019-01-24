class List():
    
    def __init__(self, name, item):
        self.name = name
        self.t = "list"
        self.contentType = item
        self.content = []
        
        
    def getSchema(self):
        return {
            "name":self.name,
            "type":self.t,
            "content": self.contentType().getSchema()
        }
        
    def getData(self):
        return {
            "name":self.name,
            "type":self.t,
            "content": [v.getData() for v in self.content]
        }
        
    def setValue(self, data):
        self.content = [self._loadData(d) for d in data]
        
    def _loadData(self, data):
        item = self.contentType()
        item.setValue(data)
        return item