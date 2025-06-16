from tkinter import *
win =Tk()
def new():
  print("hi!")

main_menu=Menu(win)
win.config(menu=main_menu)

#file

f_menu=Menu(main_menu,tearoff=0)
#f_menu.add_command(label="new file",command="new")
#f_menu.add_separator()
f_menu.add_command(label="open file")
f_menu.add_separator()
f_menu.add_command(label="save file")
f_menu.add_separator()

sub_menu=Menu(f_menu,tearoff=0)
sub_menu.add_command(label="file1")
sub_menu.add_separator()
sub_menu.add_command(label="file2")
f_menu.add_cascade(label='new file',menu=sub_menu)







f_menu.add_command(label="save as file")



main_menu.add_cascade(label='File',menu=f_menu)

# edit

f_menu1=Menu(main_menu,tearoff=0)
f_menu1.add_command(label="cut")
f_menu1.add_separator()
f_menu1.add_command(label="copy")
f_menu1.add_separator()
f_menu1.add_command(label="paste")
f_menu1.add_separator()
f_menu1.add_command(label="undo")



main_menu.add_cascade(label='Edit',menu=f_menu1)










win.mainloop()
