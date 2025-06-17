from tkinter import *
win=Tk()

canvas_1=Canvas(win,bg="grey")
canvas_1.place(x=0,y=0,height=500,width=500)

canvas_1.create_text(200,400,font=(188),text="hi")
win.mainloop()