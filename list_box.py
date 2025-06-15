from tkinter import *
from tkinter import ttk
win=Tk()

def get_data(var):
  var=p.get()
  print(var)


list_1=["java","c","python","c++"]
p=StringVar(value=list_1)
list_box=Listbox(win,listvariable=p,font=40,selectmode="extended")
list_box.place(x=20,y=20,height=150,width=100)


list_box.bind('<<ListboxSelect>>',get_data)





win.mainloop()