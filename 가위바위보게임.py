from tkinter import*
from random import*
win = Tk()
win.title("Rock scissors Paper Game")
def change_img(user):
    List = ["scissors.png", "rock.png", "paper.png"]

    com = randint(0,2)
    computer_img = PhotoImage(file = List[com])
    useruser_img = PhotoImage(file = List[user])
    
    com_img['image'] = computer_img
    com_img.image = computer_img

    user_img['image'] = useruser_img
    user_img.image = useruser_img

    game(com,user)

def game(com,user):
    if user == 0:
        if com == 0:
            result['text'] = "Draw -_-"
        elif com == 1:
            result['text'] = "defeat =_="
        else:
            result['text'] = "win ^_^"

    elif user == 1:
         if com == 1:
            result['text'] = "Draw -_-"
         elif com == 2:
            result['text'] = "defeat =_="
         else:
            result['text'] = "win ^_^"

    elif user == 2:
         if com == 2:
                result['text'] = "Draw -_-"
         elif com == 1:
                result['text'] = "win ^_^"
         else:
                result['text'] = "defeat =_="
basic_img = PhotoImage(file = "ready.png")

com_img = Label(win,image = basic_img, relief = "solid")
user_img = Label(win,image = basic_img, relief = "solid")
com_lbl = Label(win,text = "computer")
user_lbl = Label(win,text = "user")
result = Label(win, text = " ", width = 15, fg = "brown", bg = "lightyellow")

scissors_btn = Button(win, text = "scissors", bg = "purple", width = 15, command = lambda: change_img(0))
paper_btn = Button(win, text = "paper", bg = "red", width = 15, command = lambda: change_img(2))
rock_btn = Button(win, text = "rock", bg = "lightgreen", width = 15, command = lambda: change_img(1))

com_img.grid(row  = 0, column = 0)
user_img.grid(row  = 0, column =2 )
com_lbl.grid(row  = 1, column = 0)
user_lbl.grid(row  = 1, column = 2)
result.grid(row  = 0, column = 1)
scissors_btn.grid(row  = 2, column = 1)
paper_btn.grid(row  = 2, column = 2)
rock_btn.grid(row  = 2, column = 0)










































win.mainloop()
