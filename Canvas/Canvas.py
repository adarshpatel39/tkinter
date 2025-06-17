from tkinter import *
win=Tk()

canvas_1=Canvas(win,bg="grey")
canvas_1.place(x=0,y=0,height=500,width=500)
    #(x,y) (x1,y1)
coordinate1=0,0,500,500
coordinate2=500,0,0,500,
#create Line
line1=canvas_1.create_line(coordinate1,fill="white")

line2=canvas_1.create_line(coordinate2,fill="white")





win.mainloop()