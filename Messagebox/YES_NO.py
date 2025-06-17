from tkinter import *
from tkinter.messagebox import askyesno,askquestion
win=Tk()
def ask_yesno():
  var=askyesno(title="python",message="hello!")
  print(var)


btn=Button(win,text="ohk",command=ask_yesno())
btn.place(x=20,y=20,height=40,width=70)






win.mainloop()