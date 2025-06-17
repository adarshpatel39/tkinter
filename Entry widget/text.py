from tkinter import*
win=Tk()
win.config(bg="black")
def press():
  var=text.get("1.0","end")
  lb.config(text=var)



text=Text(win,font=("ROBOTO",10),height=5,bg="white")
text.place(x=10,y=10,width=300)


lb=Label(win,text="",bg="beige")
lb.place(x=14,y=300,height=100,width=400)

btn=Button(win, text="select",command=press)
btn.place(x=10,y=250)











win.mainloop()