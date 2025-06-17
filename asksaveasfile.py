from tkinter import *
from tkinter import filedialog
win=Tk()

def save_file():
  var=filedialog.asksaveasfilename(title="python file",initialdir="/",filetypes=(("txt","*.txt"),("python","*.py"),("other file","*")))
  print(var)


btn=Button(win,text="save",command=save_file)
btn.place(x=30,y=40,height=50,width=70)















win.mainloop()