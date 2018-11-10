from tkinter import *

window1 = Tk()

frame1 = Frame(window1)

label1 = Label(frame1,text = "Frame 1", font = "Arial 20", bg = "#ff0000")
label1.pack()

frame2 = Frame(window1)

label2 = Label(frame2,text = "Frame 2", font = "Arial 20", bg = "#00ffff")
label2.pack()

frame3 = Frame(window1)

label3 = Label(frame3,text = "Frame 3", font = "Arial 20", bg = "#0000ff")
label3.pack()

frame4 = Frame(window1)

label4 = Label(frame4,text = "Frame 4", font = "Arial 20", bg = "#ff00ff")
label4.pack()

frame1.grid(row=0,column=0) 
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

window1.mainloop()
