from tkinter import *
from tkinter .messagebox import showinfo,showerror,showwarning
win=Tk()

def text():
  showwarning(title="adarsh patel",message="hello!")

btn=Button(win,text="ok",command=text)
btn.place(x=10,y=10,height=30,width=40)


win.mainloop()