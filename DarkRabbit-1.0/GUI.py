from tkinter import *
import ttkbootstrap  as ttkb

root = Tk()
root.geometry("800x800")
ttkb.Style(theme="superhero")
Label(root,text = "Enter the Site : ",font=25).pack()
String = StringVar()
Entry(root,textvariable=String,font=22).pack()

Label(root,text = "Enter the Username: ",font=25).pack()
String = StringVar()
Entry(root,textvariable=String,font=22).pack()

Label(root,text = "Enter pattern: ",font=25).pack()
String = StringVar()
Entry(root,textvariable=String,font=22).pack()

root.mainloop()



