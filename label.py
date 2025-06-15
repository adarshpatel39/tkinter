from tkinter import *
entry=input("ENTER YOUR WORDS:")
win=Tk()
win.config(bg="beige")
var=StringVar()
lab=Label(win,font=("Arial Black",40,"bold"),fg='green',cursor="Plus",relief="sunken",justify=CENTER,textvariable=var,underline=3)


lab.place(x=100,y=290)

var.set(entry)
print(var.get())
win.mainloop()
#relief= shows in 3D