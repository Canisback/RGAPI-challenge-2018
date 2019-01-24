from ..Types.List import List
from ..LoLTypes.Item import Item

class ItemList(List):
    
    def __init__(self):
        List.__init__(self, "Items", Item)