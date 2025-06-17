from tkinter import *
from tkinter.messagebox import askokcancel
win=Tk()
win.title("School Mark Sheet")
win.config(bg="grey")
win.geometry("600x650")
win.resizable(False,False)

def enter():
  name=st_name1.get()
  math=math_mark.get()
  esc=esc_mark.get()
  phy=phy_mark.get()
  chm=chm_mark.get()

  total=math+esc+phy+chm
  per=(total/400)*100

  div=""

  if per>90:
    div="A+ Grade"
  elif per<=90 and per>80:
    div="A Grade"
  elif per<=80 and per>70:
    div="B Grade"
  elif per<=70 and per>60:
    div="C Grade"
  elif per<=50 and per>40:
    div="D Grade"
  elif per<40 :
    div="F Grade = Failed"

  print(total)
  print(per)
  print(div)
  messagebox(name,total,per,div)

def messagebox(*data):
  print_1=f"""
  Name:{data[0]}
  Total:{data[1]}
  Per:{data[2]}
  Div:{data[3]}
  """
  askokcancel(title="Patel Academy",message=print_1)



school_name=Label(win,text="Patel Academy",font=("Ariel Black",40,"bold"),bg="white")
school_name.place(x=5,y=20,height=50,width=600)

st_name1=StringVar()
st_name=Label(win,text="Student Name",font=("Roboto",30,"bold"))
st_name.place(x=10,y=80,height=30,width=260)
st_name_Entry=Entry(win,font=("Roboto",30,"bold"),textvariable=st_name1)
st_name_Entry.place(x=300,y=80,height=30,width=280)



subj=Label(win,text="Subject Number",font=("Roboto",30,"bold"))
subj.place(x=140,y=120,height=30,width=320)



math_mark=DoubleVar()
esc_mark=DoubleVar()
phy_mark=DoubleVar()
chm_mark=DoubleVar()

math=Label(win,text="Mathematics",font=("Roboto",30,"bold"))
math.place(x=10,y=160,height=30,width=260)
math_Entry=Entry(win,font=("Roboto",30,"bold"),textvariable=math_mark)
math_Entry.place(x=300,y=160,height=30,width=280)

esc=Label(win,text="Electronics",font=("Roboto",30,"bold"))
esc.place(x=10,y=200,height=30,width=260)
esc_Entry=Entry(win,font=("Roboto",30,"bold"),textvariable=esc_mark)
esc_Entry.place(x=300,y=200,height=30,width=280)

phy=Label(win,text="Physics",font=("Roboto",30,"bold"))
phy.place(x=10,y=240,height=40,width=260)
phy_Entry=Entry(win,font=("Roboto",30,"bold"),textvariable=phy_mark)
phy_Entry.place(x=300,y=245,height=30,width=280)

chm=Label(win,text="chemistry",font=("Roboto",30,"bold"))
chm.place(x=10,y=300,height=40,width=260)
chm_Entry=Entry(win,font=("Roboto",30,"bold"),textvariable=chm_mark)
chm_Entry.place(x=300,y=305,height=30,width=280)




btn=Button(win,text="Submit",bg="white",font=("Roboto",26,"bold"),relief="solid",command=enter)
btn.place(x=260,y=400,height=40,width=130)


win.mainloop()