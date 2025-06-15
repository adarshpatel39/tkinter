from tkinter import *
win=Tk()

def python(event):
  print("hi")

def fun(ev):
  print("hello")

btn=Button(win,text="OK")
btn.bind('<Leave>',python)
btn.bind('<Leave>',fun,add="+") # calls two fun in one time

# unbind(): stop the work
btn.place(x=20,y=20,height=50,width=50)










win.mainloop()