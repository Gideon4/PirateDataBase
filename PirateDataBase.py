import json
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

class Filemanager:
    path = "pdb.json"

    def writetofile(self,idNum,obj):
        try:
            f = open(self.path,"r")
            d = json.load(f)
            f.close()
        except:
            d = {}
        d[idNum] = obj
        f = open(self.path,"w")
        json.dump(d,f)
        f.close()
    
