from transactionclass import Transaction
from itemclass import Item
#from staffclass import Staff

class Kiosk():
    def __init__(self, transactionList):
        self.transactionList=transactionList
        #self.alert=alert (boolean on/off?)

    def startTransaction(self):
        #call transaction init?
        Transaction(transactionId=1)
        


    def verifyStaff(self, staffId, password):
        # get StaffId
        # get password
        #verify mathces a database?
        return #boolean?

    def getItemInfo(self, Item):
        return Item.getName(self), Item.getNumber(self), Item.getPrice(self), Item.getWeight(self), Item.getRestricted(self)

    def callStaff(self):
        return # would the be a boolean flag for an alert property, setting it to true, perhaps? 
                #Staff could have an endAlert() which would set it to false.

    def __str__(self):
        return transactionList

        
        

