from tkinter import *
import json
import random
from firebase import firebase as fb

class Pirate:

    name = ""
    ship = ""
    fictional = False
    image = ""

    def loadfromdict(self,d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.fictional = d["fictional"]
        self.image = d["image"]

    def getdict(self):
        d = {"name":self.name,
             "ship":self.ship,
             "fictional":self.fictional,
             "image":self.image}
        
        return d

class FirebaseManager:
    app = fb.FirebaseApplication("https://fihreebahsay.firebaseio.com/")

    def writetofile(self, idNum, obj):
        result = self.app.put("", idNum, obj)
        
def addnew():

    global win, namentry, shipentry, optionString
    p = Pirate()
    p.name = namentry.get()
    p.ship = shipentry.get()
    p.fictional = optionString.get()

    namentry.delete(0,"end")
    shipentry.delete(0,"end")

    d = p.getdict()
    fm = FirebaseManager()
    fm.writetofile(random.randint(10000,99999),d)

    win.destroy()

def cancelme():
    global win
    win.destroy()

def browseimage():
    x=0

def loadwindow(root):

    global win, namentry, shipentry, optionString, lbimage
    win = root
    root.config(bg="salmon")
    root.title("Pirate Database")
    title = Label(root,text="Pirate Database",font = "Impact 25",bg = "salmon")
    title.grid(row = 0,column = 0,columnspan = 3)

    namelabel = Label(root,text="Name:",font = "Impact 15",bg = "salmon")
    namelabel.grid(row = 1,column = 0)

    shiplabel = Label(root,text="Ship:",font = "Impact 15",bg = "salmon")
    shiplabel.grid(row = 2,column = 0)

    fictionalabel = Label(root,text="Fictional:",font = "Impact 15",bg = "salmon")
    fictionalabel.grid(row = 3,column = 0)

    namentry = Entry(root,font = "Impact 15",bg = "gold")
    namentry.grid(row = 1,column = 1)

    shipentry = Entry(root,font = "Impact 15",bg = "gold")
    shipentry.grid(row = 2,column = 1)

    imgbutton = Button(root,font = "Impact 15",text = "Select an Image",bg = "gold",command = browseimage)
    imgbutton.grid(row = 4,column = 0)

    lbimage = Label(root,font = "Impact 15",bg = "gold")
    lbimage.grid(row = 4,column = 1)

    optionString = StringVar(root)
    optionString.set("False")
    dropdown = OptionMenu(root,optionString,"False","True")
    dropdown.config(font = "Impact 15",width = "10",bg = "gold")
    dropdown.nametowidget(dropdown.menuname).config(font = "Impact 15")
    dropdown.grid(row = 3,column = 1)

    save = Button(root,text = "Save",font = "Impact 15",width = "20",bg = "orange",command = addnew) 
    save.grid(row = 5,column = 0,columnspan = 2)

    cancel = Button(root,text = "Cancel",font = "Impact 15",width = "20",bg = "orange",command = cancelme)
    cancel.grid(row = 6,column = 0,columnspan = 2)

    root.mainloop()
    
