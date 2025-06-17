from tkinter import *
from tkinter .colorchooser import askcolor
win=Tk()

def color():
  ans=askcolor(title="colourfull")
  print(ans)
  win.config(bg=ans[1])

btn=Button(win,text="ok",command=color)
btn.place(x=20,y=20)

win.mainloop()