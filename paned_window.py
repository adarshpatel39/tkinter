from tkinter import *
from tkinter import ttk
win=Tk()


paned_window=PanedWindow(orient=HORIZONTAL,sashwidth=4,showhandle=True)
paned_window.pack(fill=BOTH,expand=True)

left_side= Listbox(win)
left_side.pack(side=LEFT)
paned_window.add(left_side)

right_side=Listbox(win)
right_side.pack(side=LEFT)
paned_window.add(right_side)






win.mainloop()