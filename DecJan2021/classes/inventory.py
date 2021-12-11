# Creates items = def __init__
# updateItem = changing item name
# displayItems = Reading the item

class Inventory:
    allItems = []
    def __init__(self, itemName, itemDesc, itemType):
        self.itemName = itemName
        self.itemDesc = itemDesc
        self.itemType = itemType
        self.itemRating = None
        self.itemLocation = None # setting this = allows it to have a null entry and is not required on item creation
        Inventory.allItems.append(self)

    def displayItems(self):
        print(f"{self.itemName}")
        return f"{self.itemName}"

    def updateItem(self, itemName):
        self.itemName = itemName
        return self

    @classmethod
    def printAllItems(cls):
        for i in cls.allItems:
            i.displayItems()