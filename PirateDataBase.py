from tkinter import *
import json
import random
import firebase

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

def addnew():
    p = Pirate()
    p.name = namentry.get()
    p.ship = shipentry.get()
    p.fictional = optionString.get()

    namentry.delete(0,"end")
    shipentry.delete(0,"end")

    d = p.getdict()
    fm = Filemanager()
    fm.writetofile("1010101",d)

root = Tk()
root.title("Pirate Database")
title = Label(root,text="Pirate Database",font = "Impact 25")
title.grid(row = 0,column = 0,columnspan = 3)

namelabel = Label(root,text="Name:",font = "Impact 15")
namelabel.grid(row = 1,column = 0)

shiplabel = Label(root,text="Ship:",font = "Impact 15")
shiplabel.grid(row = 2,column = 0)

fictionalabel = Label(root,text="Fictional:",font = "Impact 15")
fictionalabel.grid(row = 3,column = 0)

namentry = Entry(root,font = "Impact 15")
namentry.grid(row = 1,column = 1)

shipentry = Entry(root,font = "Impact 15")
shipentry.grid(row = 2,column = 1)

optionString = StringVar(root)
optionString.set("False")
dropdown = OptionMenu(root,optionString,"False","True")
dropdown.config(font = "Impact 15",width = "10")
dropdown.nametowidget(dropdown.menuname).config(font = "Impact 15")
dropdown.grid(row = 3,column = 1)

save = Button(root,text = "Save",font = "Impact 15",width = "20",command = addnew) 
save.grid(row = 4,column = 1)

root.mainloop()
    
