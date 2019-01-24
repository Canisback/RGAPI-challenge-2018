from ..Types.Numeric import Numeric 
from ..Types.String import String
from ..Types.Img import Img
from ..Types.Block import Block

from static_data import ddragon

class Item(Block):
    
    def __init__(self):
        Block.__init__(self, "Item")
        self.content = {
            "itemId" : Numeric("Item id"),
            "itemName" : String("Item name"),
            "itemImage" : Img("Item image"),
            "tooltips" : String("Item tooltip")
        }
    
    def setValue(self, data):
        dd = ddragon.ddragon()
        self.content["itemId"].setValue(data)
        if data > 0:
            self.content["itemName"].setValue(dd.getItem(data).name)
            self.content["itemImage"].setValue(dd.getItem(data).image)
            self.content["tooltips"].setValue("http://tooltips.canisback.com/{lang}/item/{id}".format(lang="en", id=data))