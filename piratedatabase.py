class Pirate:
    name = ""
    ship = ""
    fictional = False

    def loadfromdict(self,d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.fictional = d["fictional"]

    def getdict(self):
        d = {"name":self.name,
             "ship":self.ship,
             "fictional":self.fictional}
        return d
