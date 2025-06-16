from tkinter import *
win=Tk()
win.title("****adarsh****")
#win.inconbitmap(r"eren-yeager-3840x2743-10405.jpg")
win.attributes('-alpha',1)
#win.config(bg="red")
win['bg']="red"

width=300
height=300
sys_width=win.winfo_screenwidth()
sys_height=win.winfo_screenheight()
c_x= int(sys_width/2-width/2)
c_y= int(sys_height/2-height/2)
win.geometry(f"{sys_width}x{height}+{c_x}+{c_y}")
win.minsize(100,100)
win.maxsize(500,500)
win.resizable(False,False)  #peermanently fixed window
win.mainloop()