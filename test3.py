#Label 다시한번 확인..모르고 지움,,,
from tkinter import *


mw = Tk()

lb1 = Label(mw,text="인천광역시")
lb2 = Label(mw,text="미추홀구", font=("궁서체", 30), fg="red")
lb3 = Label(mw,text="용현동", bg="yellow", width=20, height=4, anchor=CENTER)

lb1.pack()
lb2.pack()
lb3.pack()

mw.mainloop()