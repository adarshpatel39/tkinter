from tkinter import *
win=Tk()

canvas_1=Canvas(win,bg="grey")
canvas_1.place(x=0,y=0,height=500,width=500)

coordinate=20,20,200,200

arc=canvas_1.create_arc(coordinate,start=0,extent=359,fill="black")






win.mainloop()
