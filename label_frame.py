'''Label Frame'''
from tkinter import *
win=Tk()
win.config(bg="black")

Label_Frame=LabelFrame(win,text="adarsh",font=(30),relief="groove", )

Label_Frame.place(x=100,y=100,height=200,width=600)

Label_1=Label(win,text="patel",font=(40),bg="green")
Label_1.place(x=150,y=150) 
 




win.mainloop()