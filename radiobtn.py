from tkinter import *
win=Tk()
win.config(bg="black")

def fun():
  lb.config(text=var.get())

list_1=(("python","p"),("java","j"),("c++","+"))

var=StringVar()

for i in list_1:
  radio_btn=Radiobutton(win,text=i[0],value=i[1],variable=var,command=fun)
  radio_btn.pack()

lb=Label(win,text="",font=(30))
lb.pack()

bt=Button(win,text="ok",font=40,command=fun)
bt.pack()

radio_btn=Radiobutton(win,text="adarsh",value="sikhar",variable=var)
radio_btn.pack()
radio_btn.select()

win.mainloop()