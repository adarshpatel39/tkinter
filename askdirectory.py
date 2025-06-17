from tkinter import *
from tkinter import filedialog

win=Tk()
def fun():
  var=filedialog.askdirectory(title="python",initialdir="/")
  print(var)


btn=Button(win,text="ok",command=fun)
btn.place(x=20,y=30,height=40,width=70)









win.mainloop()