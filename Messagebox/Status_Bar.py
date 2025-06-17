from tkinter import *
win=Tk()

def change():
  status_bar.config(text="wow!")

status_bar=Label(win,text="ready",relief="sunken",anchor=W,bd=10)
status_bar.pack(side=TOP,fill=X)

btn=Button(win,text="ok",command=change)
btn.place(x=20,y=40,height=40,width=45)




win.mainloop()