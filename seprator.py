from tkinter import*
from tkinter import ttk
win=Tk()

lb1=Label(win,text="adarsh",font=(30),bg="skyblue")
lb1.pack(side="left")

seperator=ttk.Separator(win,orient="horizontal")
seperator.pack(fill=X,side="left")

lb2=Label(win,text="shikhar",font=(30),bg="skyblue")
lb2.pack(side="right")









win.mainloop()