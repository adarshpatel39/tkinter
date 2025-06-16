from tkinter import *
from tkinter import ttk
win=Tk()

txt=Text(win,font=(30))
txt.place(x=10,y=10,height=400,width=400)

scbr=Scrollbar(win,orient="vertical",command=txt.yview)
scbr.place(x=410,y=10,height=400,width=20)

txt["yscrollcommand"]=scbr.set



win.mainloop()