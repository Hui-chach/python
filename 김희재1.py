##from tkinter import *
##win = Tk()
##canvas = Canvas(win, bg = "yellow", width = 100, height =100)
##canvas.pack()
##win.mainloop()
##    
##from tkinter import *
##
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 500)
##canvas.create_line(250, 100, 250, 400, fill = "red", width = 3)
##
##canvas.pack()
##win.mainloop()
##from tkinter import *
##
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 500)
##canvas.pack()
##
##x1, y1 = 10, 10
##x2, y2 = 460, 10
##
##for i in range(10) :
##    canvas.create_line(x1, y1, x2, y2, fill = "blue", width = 3)
##    y1 += 50
##    y2 = y1
##
##
##x1, y1 = 10, 10
##x2, y2 = 10, 460
##for i in range(10) :
##    canvas.create_line(x1, y1, x2, y2, fill = "red", width = 3)
##    x1 += 50
##    x2 = x1
##
##
##win.mainloop()
##from tkinter import *
##
##pen_color = "black"
##
##def paint(event):
##    x1,y1 = event.x, event.y
##    x2,y2 = x1 +5, y1+5
##    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)
##
##def change_color1() :
##    global pen_color
##    pen_color = "red"
##def change_color2() :
##    global pen_color
##    pen_color = "black"
##
##
##
##
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 200)
##btn1 = Button(win, text = "red", command = change_color1)
##btn2 = Button(win, text = "black", command = change_color2)
##canvas.pack()
##btn1.pack()
##btn2.pack()
##win.bind("<B1-Motion>", paint)
##win.mainloop()
##win.mainloop()
from tkinter import *

pen_color = "black"

def paint(event):
    x1,y1 = event.x, event.y
    x2,y2 = x1 +5, y1+5
    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)

def change_color() :
    global pen_color
    pen_color = "red"




win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 200)
btn_white = Button(win, text = "white", bg = "white",command = change_color)
btn_ black= Button(win, text = "black", bg = "black",command = change_color)
btn_ blue= Button(win, text = "blue", bg = "blue",command = change_color)
btn_ green= Button(win, text = "green", bg = "green",command = change_color)
btn_ yellow= Button(win, text = "yellow", bg = "yellow",command = change_color)
btn_ red= Button(win, text = "red", bg = "red",command = change_color)
btn_ plus= Button(win, text = "plus", bg = "white" ,command = change_color)
btn_ minus= Button(win, text = "minus", bg = "white",command = change_color)
btn_ clear= Button(win, text = "clear", bg = "white",command = change_color)

win.bind("<B1-Motion>", paint)
win.mainloop()
win.mainloop()



