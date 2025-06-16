from tkinter import*
win=Tk()

def py():
  lb.config(text="file menu")

menubtn=Menubutton(win,text="File",bg="green",relief="sunken")
menubtn.menu=Menu(menubtn,tearoff=0)
menubtn["menu"]=menubtn.menu
menubtn.menu.add_checkbutton(label="new file",command=py)
menubtn.menu.add_checkbutton(label="open file")
menubtn.menu.add_checkbutton(label="save file")

menubtn.pack()

lb=Label(win,text="")
lb.pack()





win.mainloop()
