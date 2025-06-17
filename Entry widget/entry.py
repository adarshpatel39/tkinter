from tkinter import*
win=Tk()

def gmail():
  lb1.config(text=var.get())

lb=Label(win,text="email",font=(50))
lb.place(x=100,y=100,height=50,width=100)

var=StringVar()

entry=Entry(win,font=(60),cursor="xterm",show=".",justify="left",bd=5,textvariable=var)
entry.place(x=100,y=150,height=30,width=200)

btn=Button(win,text="submit",font=(30),command=gmail)
btn.place(x=100,y=240,width=100)

lb1=Label(win,text="",font=(50))
lb1.place(x=100,y=310,height=50,width=400)





win.mainloop()