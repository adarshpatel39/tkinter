from tkinter import *
win=Tk()
win.config(bg="beige")
lb=Label(win,text="hello adarsh",font=("Arial Black",40,"bold"),anchor=CENTER,relief="ridge",bg="grey")
lb.place(x=400,y=300)

btn=Button(win,bitmap="question")
btn.place(x=450,y=450)



win.mainloop()