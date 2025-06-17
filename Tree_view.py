from tkinter import *
from tkinter import ttk
win=Tk()

data=[("adarsh","anoop","ad2005verma @gmail.com")
      ,("aarush","amrendra","aarush123@gmail.com"),("shikhar","anoop","theshikhar42@gmail.com")]

col=("name_1","fname_1","email_1")
tree =ttk. Treeview(win,columns=col,show="headings")

tree.heading("name_1",text="Name")
tree.heading("fname_1",text="Father name")
tree.heading("email_1",text="Email")


for i in data:
  tree.insert("",END,values=i)

tree.place(x=30,y=30,height=400,width=600)








win.mainloop()