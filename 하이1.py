##from tkinter import *
##
##pen_color = "black"
##w = 6
##def paint(event):
##    x1,y1 = event.x, event.y
##    x2,y2 = x1 +5, y1+5
##    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)
##
##def change_color(color) :
##    global pen_color
##    pen_color = color
##
##def clear_canvas() :
##    canvas.delete("all")
##
##
##
##
##win = Tk()
##canvas = Canvas(win, bg = "white", width = 500, height = 200)
##btn_white = Button(win, text = "white", bg = "white",width = w, command = lambda : change_color("white"))
##btn_black= Button(win, text = "black", bg = "black",fg = "white", width = w, command = lambda : change_color("black"))
##btn_blue= Button(win, text = "blue", bg = "blue",width = w, fg = "white",command = lambda : change_color("blue"))
##btn_green= Button(win, text = "green", bg = "green",width = w, fg = "white", command = lambda : change_color("green"))
##btn_yellow= Button(win, text = "yellow", bg = "yellow",width = w, command = lambda : change_color("yellow"))
##btn_red= Button(win, text = "red", bg = "red",width = w, fg = "white", command = lambda :change_color("red"))
##btn_plus= Button(win, text = "plus", bg = "white" ,width = w, command = change_color)
##btn_minus= Button(win, text = "minus", bg = "white",width = w,  command = change_color)
##btn_clear= Button(win, text = "clear", bg = "white",width = w, command = clear_canvas)
##canvas.grid(row = 0, column = 0, columnspan = 9)
##btn_white.grid(row = 1, column = 0)
##btn_black.grid(row = 1, column = 1)
##btn_blue.grid(row = 1, column = 2)
##btn_green.grid(row = 1, column = 3)
##btn_yellow.grid(row = 1, column = 4)
##btn_red.grid(row = 1, column = 5)
##btn_plus.grid(row = 1, column = 6)
##btn_minus.grid(row = 1, column = 7)
##btn_clear.grid(row = 1, column = 8)
##win.bind("<B1-Motion>", paint)
##win.mainloop()
##from tkinter import *
##
##win = Tk()
##canvas = Canvas(win, width = 400, height = 400, bg = "white")
##canvas.pack()
##
##canvas.create_oval(10, 10, 60, 60, fill = "blue")
##canvas.create_rectangle(100, 10, 160, 60, fill = "yellow", outline = "red")
##canvas.create_polygon(100, 60, 30, 90, 160, 90, fill = "red")
##win.mainloop()
##from tkinter import *
##win = Tk()
##canvas = Canvas(win, width = 100, height = 100, bg = "white")
##canvas.pack()
##x1,y1,x2,y2 = 0, 0, 0, 100
##for i in range(10) :
##    canvas.create_line(x1, y1, x2, y2)
##    canvas.create_line(y1, x1, y2, x2)
##    x1+= 10
##    x2 = x1
##canvas.create_oval(20, 20, 80, 80)
##win.mainloop()
##from tkinter import *
##from random import *
##
##def draw_shape(event) :
##    color = ["black", "white", "blue", "red", "green", "yellow"]
##    x1, y1 = event.x, event.y
##    x2, y2 = x1 + randint(10, 70), y1 + randint(10, 70)
##    canvas.create_rectangle(x1, y1, x2, y2, fill = color[randint(0,5)])
##
##win = Tk()
##canvas = Canvas(win, width = 300, height = 300, bg = "white")
##canvas.pack()
##        
##canvas.bind("<B1-Motion>", draw_shape)
##
##win.mainloop()
a = 0
n = int(input("숫자를 입력해라"))
for i in range(1,n+1) :
    a = a+i
print(a)
