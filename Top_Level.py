from tkinter import *
win=Tk()

def top():
  tp=Toplevel(win)
  tp.title("java")
  tp.config(bg="grey")
  lb=Label(tp,text="lang")
  lb.place(x=10,y=10)
  tp.mainloop()


win.title("python")
btn=Button(win,text="ok",command=top)
btn.place(x=20,y=20,height=50,width=50)





win.mainloop()