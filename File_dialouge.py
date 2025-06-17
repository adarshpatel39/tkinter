# askopenfile()
# askopenfilename()

from tkinter import*
from tkinter import filedialog
win=Tk()
def click():
 # var=filedialog.askopenfilename(initialdir="/",filetypes=(("txtfile","*.txt"),("all file","*.*")),title="patel")
 # print (var)


  var=filedialog.askopenfilename(initialdir="/",filetypes=(("txtfile","*.txt"),("all file","*.*")),title="patel")

  read_file=var.read()

btn=Button(win,text="open",command=click)
btn.place(x=30,y=40)







win.mainloop()
