from firebase import firebase as fb

class FirebaseManager:
    app = fb.FirebaseApplication("https://fihreebahsay.firebaseio.com/")

    def writetofile(self, idNum, obj):
        result = self.app.put("", idNum, obj)

    def getall(self):
        d = self.app.get("",None)
        return d

    def deletepirate(self,id):
        self.app.delete(id,None)
