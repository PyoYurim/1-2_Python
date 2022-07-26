from tkinter import *

def calFtoC():
    f = etF.get().strip()
    if f :
        c = (float(f) - 32) * (5/9)
        etC.delete(0, END) #clear
        etC.insert(0, f"{c:0.2f}")

def calCtoF():
    c = etC.get().strip()
    if c :
        f = (float(c) *1.8) + 32
        etC.delete(0, END) #clear
        etC.insert(0, f"{f:0.2f}")



mw = Tk()

lbF = Label(mw, text="화씨")
lbC = Label(mw, text="섭씨")

etF = Entry(mw)
etC = Entry(mw)

frgroup = Frame(mw)
btFtoC = Button(frgroup, text="화씨->섭씨", command=calFtoC)
btCtoF = Button(frgroup, text="섭씨->화씨", command=calCtoF)

lbF.grid(row=0, column=0)
lbC.grid(row=1, column=0)

etF.grid(row=0, column=1)
etC.grid(row=1, column=1)

frgroup.grid(row=2, column=1)

btFtoC.grid(row=0, column=0)
btCtoF.grid(row=0, column=1)

mw.mainloop()

#pack쓰면 일렬로 쭈루룩 나옴