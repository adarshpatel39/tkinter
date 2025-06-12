# from tkinter import *
# root = Tk()
# root.title("First Python GUI")
# mylabel=Label(root, text="Hello World")
# mylabel.pack()
# myform = Entry(root)
# myform.pack()
# mybutton =Button(root, text="Click Me", width="10", height="2")

# mybutton.pack()
# root.mainloop()


import tkinter as tk
win=tk.Tk()
win.title("ADARSH PATEL")
'''changing logo'''
# win.iconbitmap("C:\Users\adars\Downloads\\eren-yeager-3840x2743-10405")

'''setting transparency'''
# win.attributes('-alpha',1)

'''changing background'''
# win.config(bg="green")
# win['bg']="pink"

'''sizing window'''
# win.geometry("300x400+50+100")       #width x height +x+y
width=300
height=300
# sys_wdth=win.winfo_screenmmwidth()
# sys_hght=win.winfo_screenheight()
# c_x=int(sys_wdth/2-width/2)
# c_y=int(sys_hght/2-height/2)
# win.geometry(f"{width}x{height}+{c_x}+{c_y}")

# win.minsize=(100,100)
# win.maxsize=(100,100)
win.geometry("300x500")
win.resizable(False,False)

win.mainloop()
