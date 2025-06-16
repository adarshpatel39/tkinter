from tkinter import *

win = Tk()
win.title("PATEL")
win.config(bg="green")

lab = Label(win, text="patel", font=("Times New Roman", 30, "bold"), bg="blue")
lab.pack(padx=10,pady=20)
lab.pack(ipadx=10 ,ipady=20,fill="x" ,expand=True,side="left")    # decide position of label. ipadx,ipady=internal padding.  padx&pady=externly padding
# fill= complete fill along a axis.
# expand= place it at center.
lab1=Label(win,text="adarsh",font=("Times New Roman",20),bg="green")
lab1.pack(padx=10,pady=20,side="left",fill="x")

win.mainloop()
