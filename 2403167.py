from tkinter import *
win = Tk()

def click() :
    if lbl['text'] == "hello" :
        lbl['text'] = "python"
        lbl['bg'] = "green"
    else:
        lbl['text'] = 'hello'
        lbl['bg'] = 'orange'
lbl = Label(win, text = "hello", bg = "orange", fg = "white")
btn = Button(win, text = "button",
             command = click)
lbl.pack()
btn.pack()
win.mainloop()

