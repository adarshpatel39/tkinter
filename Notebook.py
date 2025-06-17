from tkinter import *
from tkinter import ttk
win=Tk()

notebook=ttk.Notebook(win)
notebook.pack(pady=10,expand=True)

frame1= ttk.Frame(notebook,height=500,width=500)
frame1.pack(fill="both",expand=True)

label_frame1=Label(frame1,text="python")
label_frame1.place(x=10,y=10)

frame2= ttk.Frame(notebook,height=500,width=500)
frame2.pack(fill="both",expand=True)

label_frame2=Label(frame2,text="JS")
label_frame2.place(x=10,y=10)

notebook.add(frame1,text="NEW")
notebook.add(frame2,text="OPEN")














win.mainloop()