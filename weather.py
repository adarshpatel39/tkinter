from tkinter import *
from PIL import ImageTK,image
root=Tk()
root.inconbitmap()
root.geometry("400X400")
        
try:
  api_request=requests.get("cceee673685a4d1ca35172253251506");
api=json.loads(api_request.content)
except Exception as e
  api="Errorr....."

myLabel=Label(root,text="api")
myLabel.pack()








root.mainloop()