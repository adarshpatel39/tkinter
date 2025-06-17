from tkinter import*
from tkinter.messagebox import askretrycancel
win=Tk()


def fun():
  ans=askretrycancel(title="hello",message="hi!",)
  if ans:
    fun()
  else :
    lb.config(text="Thank You! Adarsh") 


btn=Button(win,text="ok",command=fun)
btn.place(x=20,y=20)

lb=Label(win,text="")
lb.place(x=20,y=80)


win.mainloop()