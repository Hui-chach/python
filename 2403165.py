from tkinter import*
win = Tk()
img = PhotoImage(file = 'pizza.png')
lbl1 = Label(win, image = img)
lbl2 = Label(win, text = "pizza", bg = "yellow", fg = "red")
lbl1.pack()
lbl2.pack()
win.mainloop()
