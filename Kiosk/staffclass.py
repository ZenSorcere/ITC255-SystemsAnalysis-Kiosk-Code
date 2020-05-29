from userclass import User
from kioskclass import Kiosk

class Staff(User):
    def __init__(self, memberId, firstname, lastname, email, phone, staffId, password):
        self.memberId=memberId
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.phone=phone
        self.staffId=staffId
        self.password=password

    def authItem(self, Item):
        return #setRestricted() maybe?
    
    def generateReport(self): 
        return Kiosk.TransactionList

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + str(self.staffId)

    
