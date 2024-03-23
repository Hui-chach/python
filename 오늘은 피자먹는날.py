from  tkinter import *

win = Tk()
img = PhotoImage(file = 'pizza.png')
lbl = Label(win, image = img)
label = Label(win, text = "pizza", font = ("Elephant", 20), bg = "yellow", fg = "red")





lbl.pack()
lbl.pack()
lbl.pack()
win.mainloop()
