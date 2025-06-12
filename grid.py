from tkinter import *
win=Tk()
win.title("harsh")
win.config(bg="beige")

lab=Label(win,text="adarsh",bg="green")
#lab.grid(row=0,column=0,padx=30,pady=20)
#lab2= Label(win,text="hello",bg="green")
#lab2.grid(row=0,column=1,padx=10,pady=10)

lab.place(x=100,y=400,height=100,width=300) 
# relx,rely=relevant to other
win.mainloop()