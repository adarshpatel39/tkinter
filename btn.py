from tkinter import *
win=Tk()
win.config(bg="black")
# photo=PhotoImage(file="eren-yeager.jpg")
def python():
  lb.config(text="hello patel")


bt=Button(win,text="ON",font=30,fg="green",cursor="plus",relief="groove",compound="left",command=python)
bt.place(x=100,y=100)

lb=Label(win,text="hello",font=30)
lb.place(x=200,y=200)




win.mainloop()


#fg= font color