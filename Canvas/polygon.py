from tkinter import *
win=Tk()

canvas_1=Canvas(win,bg="grey")
canvas_1.place(x=0,y=0,height=500,width=500)

coor=[20,20,50,50,40,100]
canvas_1.create_polygon(coor,fill="beige")

win.mainloop()