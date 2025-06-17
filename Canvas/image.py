from tkinter import *
win=Tk()

canvas_1=Canvas(win,bg="grey")
canvas_1.place(x=0,y=0,height=500,width=500)
file_1=PhotoImage(file="C:\Users\adars\OneDrive\tkinter\eren-yeager-3840x2743-10405.jpg")
canvas_1.create_image(150,150,image=file_1)

win.mainloop()
