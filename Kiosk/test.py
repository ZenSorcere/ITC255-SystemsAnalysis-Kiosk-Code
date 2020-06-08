import unittest
from itemclass import Item
from kioskclass import Kiosk
from scaleabstract import Scale
from transactionclass import Transaction
from userclass import User
from staffclass import Staff
from perpounditemclass import PerPoundItem
from baggingscaleclass import BaggingScale
from kioskscaleclass import KioskScale
from inventoryclass import Inventory

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user=User('101', 'Mike', 'Gilson', 'mike@mike.com', '2065551212')

    def test_userstring(self):
        self.assertEqual(str(self.user),'Mike Gilson 101 mike@mike.com 2065551212')

class StaffTest(unittest.TestCase):
    def setUp(self):
        self.staff=Staff(10, 'Colin', 'Hanson', 'colin@hansonfan.net',2065551212, 'CH123', 'cheesewizard1234')
        self.Item= Item('Sky Kraken Beer, 6-pack', 1, 9.99, 2.00, True)

    def test_authitem(self):
        self.Item.restricted = False
        self.assertEquals(self.Item.restricted, False)
        self.assertEquals(str(self.Item.restricted), 'False' )
        
    def test_staffstring(self):
        self.assertEquals(str(self.staff), 'Colin Hanson CH123')

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item('Sky Kraken Beer, 6-pack', 1, 9.99, 2.00, True)

    def test_itemstring(self):
        self.assertEquals(str(self.item), 'Sky Kraken Beer, 6-pack 1 9.99')
    
class ItemPerPoundTest(unittest.TestCase):
    def setUp(self):
        self.perPoundItem=PerPoundItem('Bananas', 2, 0.59, 3)
        
    def test_perpoundstring(self):
        self.assertEquals(str(self.perPoundItem), 'Bananas 2 0.59/lb.')

    def test_setppweight(self):
        self.perPoundItem.weight=2.5
        self.assertEquals(self.perPoundItem.weight, 2.5)

class KioskScaleTest(unittest.TestCase):
        def setUp(self):
            self.kioskScale=KioskScale(0)
        
        def test_weighitem(self):
            self.kioskScale.scaleweight=1.34
            self.assertEquals(self.kioskScale.scaleweight, 1.34)

    # Was hoping this would catch the updated scaleweight but doesn't.
        def test_kioskscalestring(self):
            self.assertEquals(self.kioskScale.scaleweight, 0)

class InventoryTest(unittest.TestCase):
        def setUp(self):
            self.Inventory=Inventory()
            self.item1 = Item('Sky Kraken Beer, 6-pack', 1, 9.99, 2.00,True)
            self.item2 = Item('Pepperidge Farm Goldfish Crackers, 16oz', 2, 3.99, .5, False)
            self.item3 = Item('Signature 9 Grain Bread, Loaf', 3, 2.99, 1.2, False)
            self.item4 = Item('Ben & Jerrys Ice Cream, Pint', 4, 4.59, 1.3, False)
            self.Inventory.itemlist=[self.item1, self.item2, self.item3, self.item4]

        def test_inventorystring(self):
            self.assertEquals(self.Inventory.itemlist, [self.item1, self.item2, self.item3, self.item4])

class TransactionTest(unittest.TestCase):
        def setUp(self):
            self.Transaction=Transaction(1)
            self.transactionItem1 = Item('Sky Kraken Beer, 6-pack', 1, 9.99, 2.00,True)
            self.transactionItem2 = Item('Pepperidge Farm Goldfish Crackers, 16oz', 2, 3.99, .5, False)
            self.transactionItem3 = Item('Signature 9 Grain Bread, Loaf', 3, 2.99, 1.2, False)
            self.transactionItem4 = Item('Ben & Jerrys Ice Cream, Pint', 4, 4.59, 1.3, False)
            self.Transaction.transactionItemList=[self.transactionItem1, self.transactionItem2, self.transactionItem3, self.transactionItem4]
            self.user=User('101', 'Mike', 'Gilson', 'mike@mike.com', '2065551212')
            

        def test_identifyuser(self):
            self.assertEqual(self.Transaction.identifyUser(self.user), '101')

        def test_transactionstring(self):
            self.user.getMemberId()
            self.assertEquals(self.Transaction.transactionItemList, [self.transactionItem1, self.transactionItem2, self.transactionItem3, self.transactionItem4])
