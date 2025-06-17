from tkinter import *
from tkinter.messagebox import askokcancel
win=Tk()

def fun():
  ans=askokcancel(title="report",message="welcome!")
  print(ans)

btn=Button(win,text="ok",command=fun)
btn.place(x=20,y=20)

win.mainloop()