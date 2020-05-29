class Item():
    #constructor taking in initial values
    def __init__(self, name, number, price, weight, restricted):
        self.name=name
        self.number=number
        self.price=price
        self.weight=weight
        self.restricted=False  #boolean somehow? should it be in init?

    #get methods to return (see) the class variables
    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def getPrice(self):
        return self.price
    
    def getWeight(self):
        return self.weight

    def getRestricted(self):
        return self.restricted
        """ def __bool__(self):
            # This returns true only if value is 1.
        if self.value == 1:
            return True
        else:
            return False """

    #to string method determines what to return
    #when the class is cast to string
    #str(item)

    def __str__(self):
        return self.name + ' ' + str(self.number) +  ' ' + str(self.price)

