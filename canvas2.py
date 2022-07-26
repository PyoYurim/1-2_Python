from tkinter import *
from tkinter import colorchooser

penWidth = 1
color = 'black'

def doselcolor():
    global color
    colors = colorchooser.askcolor()
    color = colors[1]

def dothick():
    global penWidth
    if penWidth < 10:
        penWidth += 1

def dothin():
    global penWidth
    if penWidth > 2:
        penWidth -= 1

def doclear():
    cv.delete("all")  # delete("all" | "항목명")

def doexit():
    root.destroy()

def dodraw(event):
    x = event.x
    y = event.y
    cv.create_oval(x-penWidth, y, x+penWidth, y+penWidth, fill=color, outline=color)


root = Tk()
root.title("그림판")
cv = Canvas(root, width=800, height=600, background="lightblue")
cv.pack()

cv.bind("<B1-Motion>", dodraw)
frButtonGroup = Frame(root)
frButtonGroup.pack()

btColor = Button(frButtonGroup, text="색상", font="굴림", command=doselcolor)
btThick = Button(frButtonGroup, text="두껍게", font="굴림", command=dothick)
btThin = Button(frButtonGroup, text="가늘게", font="굴림", command=dothin)
btClear = Button(frButtonGroup, text="지우기", font="굴림", command=doclear)
btExit = Button(frButtonGroup, text="나가기", font="굴림", command=doexit)

btColor.grid(row=0, column=0)
btThick.grid(row=0, column=1)
btThin.grid(row=0, column=2)
btClear.grid(row=0, column=3)
btExit.grid(row=0, column=4)

root.mainloop()

