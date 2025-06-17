from tkinter import *
win=Tk()

data=""

def get_data(value):
  global data

  data=data+str(value)
  var.set(data)

  
def equal():
  global data
  try:
    total=str(eval(data))
    var.set(total)
    data=""
  except :
    var.set("Error")
  

def clear():
  global data
  data="" 
  var.set("")


win.title("Calculator")
win.config(bg="black")
win.geometry("500x500")
win.resizable(False,False)

lb_title=Label(win,text="Calculator",font=("Ariel Black",35,"bold"),bg="lightgrey")
lb_title.place(x=110,y=20,height=50,width=290)

var=StringVar()

entry=Entry(win,font=("Ariel Black",15),relief="solid",textvariable=var,bg="snow")
entry.place(x=50,y=90,height=50,width=410)


btn_7=Button(win,text="7",command=lambda:get_data(7),bg="grey",font=("roboto",20))
btn_7.place(x=75,y=160,height=60,width=90)

btn_8=Button(win,text="8",command=lambda:get_data(8),bg="grey",font=("roboto",20))
btn_8.place(x=165,y=160,height=60,width=90)

btn_9=Button(win,text="9",command=lambda:get_data(9),bg="grey",font=("roboto",20))
btn_9.place(x=255,y=160,height=60,width=90)

btn_x=Button(win,text="*",command=lambda:get_data("*"),bg="grey",font=("roboto",20))
btn_x.place(x=345,y=160,height=60,width=90)



btn_4=Button(win,text="4",command=lambda:get_data(4),bg="grey",font=("roboto",20))
btn_4.place(x=75,y=220,height=60,width=90)

btn_5=Button(win,text="5",command=lambda:get_data(5),bg="grey",font=("roboto",20))
btn_5.place(x=165,y=220,height=60,width=90)

btn_6=Button(win,text="6",command=lambda:get_data(6),bg="grey",font=("roboto",20))
btn_6.place(x=255,y=220,height=60,width=90)

btn_minus=Button(win,text="-",command=lambda:get_data("-"),bg="grey",font=("roboto",20))
btn_minus.place(x=345,y=220,height=60,width=90)



btn_1=Button(win,text="1",command=lambda:get_data(1),bg="grey",font=("roboto",20))
btn_1.place(x=75,y=280,height=60,width=90)

btn_2=Button(win,text="2",command=lambda:get_data(2),bg="grey",font=("roboto",20))
btn_2.place(x=165,y=280,height=60,width=90)

btn_3=Button(win,text="3",command=lambda:get_data(3),bg="grey",font=("roboto",20))
btn_3.place(x=255,y=280,height=60,width=90)

btn_plus=Button(win,text="+",command=lambda:get_data("+"),bg="grey",font=("roboto",20))
btn_plus.place(x=345,y=280,height=60,width=90)



btn_devide=Button(win,text="/",command=lambda:get_data("/"),bg="grey",font=("roboto",20))
btn_devide.place(x=75,y=340,height=60,width=90)

btn_0=Button(win,text="0",command=lambda:get_data(0),bg="grey",font=("roboto",20))
btn_0.place(x=165,y=340,height=60,width=90)

btn_point=Button(win,text=".",command=lambda:get_data("."),bg="grey",font=("roboto",20))
btn_point.place(x=255,y=340,height=60,width=90)

btn_equal=Button(win,text="=",command=equal,bg="orange",font=("roboto",20))
btn_equal.place(x=345,y=340,height=60,width=90)

btn_clear=Button(win,text="C",command=clear,bg="grey",font=("roboto",20),)
btn_clear.place(x=210,y=400,height=60,width=90)

win,mainloop()