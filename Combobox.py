from tkinter import *
from tkinter import ttk
win=Tk()


def click():
  a=var.get()
  lb.config(text=a)

var=StringVar()
list=["c","c++","python","JS"]
combobox=ttk.Combobox(win,values=list,textvariable=var)
combobox.set("choose option")
combobox.place(x=100,y=100)

lb=Label(win,text="")
lb.place(x=100,y=140)

btn=Button(win,text="select",command=click)
btn.place(x=100,y=120)




win.mainloop()

