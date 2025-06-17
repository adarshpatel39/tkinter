from tkinter import*
from tkinter import ttk
win=Tk()

lb=Label(win,text="Adarsh")
lb.place(x=10,y=20,height=50,width=100)

tree=ttk.Treeview(win,)

tree.insert("",END,text="python",iid=0)
tree.insert("",END,text="java",iid=1)
tree.insert("",END,text="JS",iid=2)

tree.insert("",END,text="c",iid=3)
tree.insert("",END,text="c++",iid=4)
tree.move(3,0,0)
        #(optin place,main place,place)
tree.move(4,1,0)


tree.place(x=10,y=100,height=200,width=100)

win.mainloop()