from tkinter import *
from tkinter import messagebox

def myMessage():
    messagebox.showinfo("클릭", etName.get())

root = Tk()
root.geometry("300x100")

etName = Entry(root)
btClick = Button(root, text="CLICK!!", fg='blue', command=myMessage)
etName.pack()
btClick.pack()

root.mainloop()



