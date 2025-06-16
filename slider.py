from tkinter import *
from tkinter import ttk

win=Tk()
var=DoubleVar()
win.config(bg="brown")

def call(a):
  a=str(var.get())
  lb.config(text=a)


slider=ttk.Scale(win,from_=0,to=100,variable=var,command=call,orient="vertical")
slider.pack()


lb=Label(win,text="",font=(50))
lb.place(x=100,y=100)









win.mainloop()