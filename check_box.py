from tkinter import *
win=Tk()

win.config(bg="black")
def test():
  lb.config(text=var.get(),bg="green",border=20)

var=StringVar()

cb=Checkbutton(win,text="patel",font=(60),variable=var,offvalue="python",command=test)
cb.pack()
cb.deselect()   # data will not be previousely checked

lb=Label(win,text="js",font=(20))
lb.pack()

#bt=Button(win,text="CLICK ME!",font=(60),command=test)
#bt.place(x=100,y=100)
#bt.pack()
#print(var.get())


win.mainloop()