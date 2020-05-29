from itemclass import Item
from userclass import User

class Transaction():
    #constructor taking in initial values
    def __init__(self, transactionId):
        self.transactionId=transactionId
        self.transactionItemList=[] #initialize list
        

    def identifyUser(self, User):
        return User.getMemberId()

    #use this method to add items to list
    def addTransactionItem(self, Item):
        transactionItemList.add(Item)
        """ count = self.count
        for i in count:
            self.transactionItemList.append(Item) """

        #parens for append item, THEN * count?

    def removeTransactionItem(self, Item):
        self.transactionItemList.remove(Item)
        #or .pop(index, Item)?

    

    
    def processPayment(self):
        return #return what? should I have a list of payment types?

    def calcTotal(self):
        total=0
        for i in self.transactionItemList:
            total += i.price
        return total

    #to string method determines what to return
    #when the class is cast to string
    #str(item)

    def __str__(self):
        return identifyUser(), self.transactionItemList