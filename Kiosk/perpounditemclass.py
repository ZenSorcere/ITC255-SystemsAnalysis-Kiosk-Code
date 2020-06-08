from itemclass import Item

class PerPoundItem(Item):
    #constructor taking in initial values
    def __init__(self, name, number, perpoundprice, weight):
        self.name=name
        self.number=number
        self.perpoundprice=perpoundprice
        self.weight=weight
        self.restricted=False  #boolean somehow? should it be in init?

    #get methods to return (see) the class variables
    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def getPerPoundPrice(self):
        return self.perpoundprice
    
    def getScaleWeight(self):
        return # what to enter here?

    def getEndPrice(self, scaleweight, PerPoundPrice):
        price = scaleweight * PerPoundPrice
        return price

    #to string method determines what to return
    #when the class is cast to string
    #str(item)
    def __str__(self):
        return self.name + ' ' + str(self.number) +  ' ' + str(self.perpoundprice) + '/lb.'