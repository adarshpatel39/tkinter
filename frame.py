from tkinter import *
from tkinter import ttk
win=Tk()

frame1=Frame(win,bd=5,bg="grey",relief="ridge")
frame1.place(x=0,y=0,height=400,width=400)

lb=Label(frame1,text="")
lb.place(x=100,y=100)

frame2=Frame(win,bd=5,bg="grey",relief="ridge")
frame2.place(x=500,y=0,height=400,width=400)


win.mainloop()
