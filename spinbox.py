from tkinter import*
from tkinter import ttk
win=Tk()

var=IntVar()

def show():
  lb.config(text=str(var.get()))

sp=ttk.Spinbox(win,from_=0,to=10,wrap=True,textvariable=var,command=show)
sp.pack()


lb=Label(win,text="",font=(30))
lb.place(x=10,y=60)





win.mainloop()