from itemclass import Item
from inventoryclass import Inventory
from baggingscaleclass import BaggingScale
from kioskscaleclass import KioskScale
from perpounditemclass import PerPoundItem
from userclass import User
from staffclass import Staff
from kioskclass import Kiosk
from transactionclass import Transaction


def main():
    

#create items
    item1 = Item('Sky Kraken Beer, 6-pack', 1, 9.99, 2.00,True)
    item2 = Item('Pepperidge Farm Goldfish Crackers, 16oz', 2, 3.99, .5, False)
    item3 = Item('Signature 9 Grain Bread, Loaf', 3, 2.99, 1.2, False)
    item4 = Item('Ben & Jerrys Ice Cream, Pint', 4, 4.59, 1.3, False)


#add items to inventory
    inventory = Inventory()
    inventory.addItem(item1)
    inventory.addItem(item2)
    inventory.addItem(item3)
    inventory.addItem(item4)


# ?kiosk creates Transaction?
    Kiosk.startTransaction(1)

#add items to TransactionList
    Transaction.addTransactionItem(1, item1, 1)
        # Restricted=True-->?
    Transaction.addTransactionItem(1, item2, 1)
    Transaction.addTransactionItem(1, item3, 1)
    Transaction.addTransactionItem(1, item4, 3)

#do receipt/total calc
    saleTotal = Transaction.calcTotal()
    receipt = Transaction
    print(receipt)
    print(saleTotal)

main()



