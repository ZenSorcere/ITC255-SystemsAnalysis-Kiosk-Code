from scaleabstract import Scale

class KioskScale(Scale):
    def __init__(self, scaleweight):
        self.scaleweight=scaleweight

    def resetWeight(self, scaleweight):
        scaleweight = 0.0
        return scaleweight

    def verifyItemWeight(self, scaleweight):
        #compare scaleweight to Item.weight
        #if ==, return true
        return

    def weightItem(self):
        # self.scaleweight = scaleweight again?
        return 

    def __str__(self):
        return self.scaleweight