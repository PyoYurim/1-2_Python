#Button, Entry(==Textbox) 글씨 입력

from tkinter import *
from tkinter import messagebox

def myname():
    messagebox.showinfo("너의 이름은", etname.get())

mw = Tk() #메인화면 만드시고

etname= Entry(mw)
btclick = Button(mw, text="클릭!!!", fg='blue', command=myname)

etname.pack()
btclick.pack()

mw.mainloop()
