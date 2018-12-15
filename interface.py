from tkinter import *
import FirebaseManager
import PirateDataBase

window1 = Tk()

window1.config(bg="salmon")

window2 = ""

frame1 = Frame(window1,bg="salmon",padx=166)

label1 = Label(frame1,text = "Pirate Data-Base", font = "Arial 20", bg = "salmon")
label1.pack()

def dofilter():
    filt = searchbar.get()
    listbox.delete(0,"end")
    for pirate in dlist:
        if (filt.lower() in dlist[pirate]["name"].lower() or
        filt.lower() in dlist[pirate]["ship"].lower()):
            listbox.insert(END, dlist[pirate]["name"])

def searchupdate(e):
    dofilter()

frame2 = Frame(window1,padx=6,bg="salmon")

searchlabel = Label(frame2,text = "Search", font = "Arial 20", bg = "salmon")
searchlabel.grid(column=0,row=0)

searchbar = Entry(frame2,font="Arial 20",bg="orange")
searchbar.bind("<KeyRelease>", searchupdate)
searchbar.grid(row=0,column=1)

def scrollright():
    index = int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index == len(dlist) - 1:
        index = 0
    else:
        index += 1

    updatelistbox(index)

def scrollleft():
    index = int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index == 0:
        index = len(dlist) - 1
    else:
        index -= 1

    updatelistbox(index)

def updatelistbox(index):
    listbox.selection_set(index)
    piratename = listbox.get(index)
    for pirateid in dlist:
        if dlist[pirateid]["name"].lower() == piratename.lower():
            display(pirateid)

frame3 = Frame(window1,bg="salmon",padx=90,pady=102)

leftimg = PhotoImage(file="left.gif")
leftimg = leftimg.subsample(2)
leftbtn = Button(frame3,image=leftimg,command=scrollleft)
leftbtn.grid(row=1,column=0,rowspan=2)

rightimg = PhotoImage(file="right.gif")
rightimg = rightimg.subsample(2)
rightbtn = Button(frame3,image=rightimg,command=scrollright)
rightbtn.grid(row=1,column=2,rowspan=2)

Piratelabel = Label(frame3,text="Pirate",font="Arial 30",bg="salmon")
Piratelabel.grid(row=0,column=0,columnspan=3)

sponge = PhotoImage(file="spongepirate.gif")
Pirateimg = Label(frame3,image=sponge)
Pirateimg.grid(row=1,column=1)

ShipLabel = Label(frame3,text="Ship:",font="Arial 20",bg="salmon")
ShipLabel.grid(row=4,column=1)

FicLabel = Label(frame3,text="Fictional:",font="Arial 20",bg="salmon")
FicLabel.grid(row=5,column=1)

def onselect(e):
    w = e.widget
    index = int(w.curselection()[0])
    piratename = w.get(index)
    for pirate in dlist:
        if piratename.lower() == dlist[pirate]["name"].lower():
            display(pirate)   

def display(pirateId):
    Piratelabel.config(text = dlist[pirateId]["name"])
    ShipLabel.config(text = dlist[pirateId]["ship"])
    if dlist[pirateId]["fictional"] == "True":
        FicLabel.config(text="Fictional")
    else:
        FicLabel.config(text="Real")

def newpirate():
    global window2
    window2 = Toplevel()
    PirateDataBase.loadwindow(window2)
    
def refreshlistbox():
    listbox.delete(0,"end")
    for item in dlist:
        pirate = dlist[item]
        listbox.insert(END,pirate["name"])

def refreshme():
    global dlist
    dlist = fm.getall()
    refreshlistbox()

frame4 = Frame(window1,bg="salmon",padx=52,pady=29)

label4 = Label(frame4,text = "View Pirates", font = "Arial 20", bg = "salmon")
label4.pack()

listbox = Listbox(frame4,font="Arial 20",width=20,bg="gold")
listbox.bind("<<ListboxSelect>>",onselect)

fm = FirebaseManager.FirebaseManager()

dlist = fm.getall()
refreshlistbox()

listbox.pack()

def listdelete():
    index = int(listbox.curselection()[0])
    deletekey = ""
    piratename = listbox.get(index)
    for pirateid in dlist:
        if dlist[pirateid]["name"].lower() == piratename.lower():
            deletekey = pirateid
    fm.deletepirate(deletekey)
    dlist.pop(deletekey)
    dofilter()
    updatelistbox(0)

deletebutton = Button(frame4,text="Delete",font="Arial 20",width=18,height=1,bg="orange",command=listdelete)
deletebutton.pack()

addbutton = Button(frame4,text="Add",font="Arial 20",width=18,height=1,bg="orange",command=newpirate)
addbutton.pack()

refreshbutton = Button(frame4,text="Refresh",font="Arial 20",width=18,height=1,bg="orange",command=refreshme)
refreshbutton.pack()

frame1.grid(row=0,column=0) 
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
