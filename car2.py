from tkinter import *
from tkinter import messagebox
from procar import Car

def getnumber():...

def searchnumber(number):...

def doin():...

def doout():...

def gettime():...

def getprice():...

carlist=[]

w = Tk()

lbTitle = Label(w, text="차량번호")
lbResult = Label(w, height=10)

etOpr = Entry(w, width=30)


btin= Button(w, text="차량입고", width=10, command=None)
btout= Button(w, text="차량출고", width=10, command=None)
bttime= Button(w, text="보관시간", width=10, command=None)
btprice= Button(w, text="요금조회", width=10, command=None)


btin.grid(row=1, column=0)
btout.grid(row=1, column=1)
bttime.grid(row=1, column=2)
btprice.grid(row=1, column=3)

lbTitle.grid(row=0, column=0)
lbResult.grid(row=2, column=0)
etOpr.grid(row=0, column=1)




w.mainloop()