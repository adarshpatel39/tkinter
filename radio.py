from tkinter import*
win=Tk()
def ok():
  lb.config(text=var.get())


var= StringVar()
list=(("python","p"),("java","j"),("c++","+"))
for i in list:

  Radio_btn=Radiobutton(win,text=i[0],value=i[1],variable=var)
  Radio_btn.pack()
  
  
lb=Label(win,text="",font=(30))
lb.pack()
btn=Button(win,text="ok",font=(30),command=ok,relief="groove")
btn.pack()

win.mainloop()

