from inventoryclass import Inventory
class User():
    #constructor taking in initial values
    def __init__(self, memberId, firstname, lastname, email, phone):
        self.memberId=memberId
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.phone=phone

    #get methods to return (see) the class variables
    def getMemberId(self):
        return self.memberId

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname
    
    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone
        

    #to string method determines what to return
    #when the class is cast to string
    #str(item)

    def __str__(self):
        return str((self.firstname) + ' ' + self.lastname +  ' ' + str(self.memberId) + ' ' + self.email + ' ' + str(self.phone))

    def browseInventory(self, Inventory):
        return #what to return here?