from tkinter import *
import FirebaseManager

window1 = Tk()

frame1 = Frame(window1,bg="salmon",padx=167)

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

frame2 = Frame(window1)

searchlabel = Label(frame2,text = "Search", font = "Arial 20", bg = "salmon")
searchlabel.grid(column=0,row=0)

searchbar = Entry(frame2,font="Arial 20",bg="orange")
searchbar.bind("<KeyRelease>", searchupdate)
searchbar.grid(row=0,column=1)

frame3 = Frame(window1,bg="salmon",padx=90,pady=85)

leftimg = PhotoImage(file="left.gif")
leftimg = leftimg.subsample(2)
leftbtn = Button(frame3,image=leftimg)
leftbtn.grid(row=1,column=0,rowspan=2)

rightimg = PhotoImage(file="right.gif")
rightimg = rightimg.subsample(2)
rightbtn = Button(frame3,image=rightimg)
rightbtn.grid(row=1,column=2,rowspan=2)

Piratelabel = Label(frame3,text="Pirate",font="Arial 30",bg="salmon")
Piratelabel.grid(row=0,column=1)

sponge = PhotoImage(file="spongepirate.gif")
Pirateimg = Label(frame3,image=sponge)
Pirateimg.grid(row=1,column=1)

ShipLabel = Label(frame3,text="Ship:",font="Arial 20",bg="salmon")
ShipLabel.grid(row=4,column=1)

FicLabel = Label(frame3,text="Fictional:",font="Arial 20",bg="salmon")
FicLabel.grid(row=5,column=1)

frame4 = Frame(window1,bg="salmon",padx=45,pady=27)

label4 = Label(frame4,text = "View Pirates", font = "Arial 20", bg = "salmon")
label4.pack()
listbox = Listbox(frame4,font="Arial 20",width=20,bg="gold")
fm = FirebaseManager.FirebaseManager()
dlist = fm.getall()
for item in dlist:
    pirate = dlist[item]
    listbox.insert(END,pirate["name"])
listbox.pack()

def listdelete():
    listbox.delete(ANCHOR)
deletebutton = Button(frame4,text="Delete",font="Arial 30",width=13,height=1,bg="orange",command=listdelete)
deletebutton.pack()


frame1.grid(row=0,column=0) 
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
