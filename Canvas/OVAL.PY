from tkinter import *
win=Tk()

canvas_1=Canvas(win,bg="grey")
canvas_1.place(x=0,y=0,height=500,width=500)

oval=canvas_1.create_oval(20,20,200,300,fill="white")


win.mainloop()