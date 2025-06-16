from tkinter import *
win =Tk()
def value_change(var):
  var=value.get()
  lb.config(text=var)

value=StringVar()
value.set("code")
opt_list=["c#","python","c++","java"]
opt=OptionMenu(win,value,command=value_change,*opt_list)
opt.place(x=100,y=100,height=30,width=100)
               
lb=Label(win,text="")
lb.place(x=300,y=100,height=30,width=100)











win .mainloop()