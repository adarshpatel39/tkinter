from tkinter import *
from tkinter import ttk
win=Tk()


#progress_bar=ttk.Progressbar(win,orient="horizontal",length=100,mode="determinate")
#progress_bar.place(x=30,y=30,height=30,width=200)


progress_bar=ttk.Progressbar(win,orient="horizontal",length=100,mode="indeterminate")
progress_bar.place(x=30,y=30,height=30,width=200)

btn=Button(win,text="start",command=progress_bar.start(300))
btn.place(x=30,y=140,height=40,width=70)


btn1=Button(win,text="stop",command=progress_bar.stop)
btn1.place(x=160,y=140,height=40,width=70)


win.mainloop()