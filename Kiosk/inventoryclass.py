from itemclass import Item

class Inventory():
    #constructor taking in initial values
    def __init__(self):
        self.itemlist=[] #initialize list
        
    #use this method to add items to list
    def addItem(self, Item):
        self.itemlist.append(Item)

    #return the list
    def getItems(self, Item):
        return self.itemlist

    def sortItems(self):
        return # return value?

    #to string method determines what to return
    #when the class is cast to string
    #str(item)

    def __str__(self):
        return self.itemlist
