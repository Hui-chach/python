from random import *
a = [1, 2, 3, 4, 5]
print(choices(a, [1, 1, 100, 1, 1],k = 3)) 
from random import *
a = [1,2,3,4,5]
print(choices(a, k = 3))
from random import *
t = [0,1,2,3,4,5]
a = choice(t)
if a == 0:
    print('Loss!')
else:
    print('No. %d spot!'%a)
from random import*
import turtle
house = turtle.Turtle()##집 그릴 터틀
house.penup()
house.goto(300,-100)
house.pendown()
house.fillcolor("skyblue")
house.begin_fill()
house.goto(330,-100)
house.goto(330,-70)
house.goto(300,-70)
house.goto(300,-100)
house.end_fill()
house.penup()
house.fillcolor("royalblue")
house.begin_fill()
house.goto(300,-70)
house.pendown()
house.goto(315,-40)
house.goto(330,-70)
house.goto(300,-70)
house.end_fill()

line= turtle.Turtle() #길그리기
line.penup()
line.goto(-380,-90)
line.pendown()
line.forward(370)
line.write(50)
line.forward(309.87)
line.write(100)


t = turtle.Turtle(shape = "turtle")
t.penup()
t.goto(-400,-90)
t.color("purple","pink")
t.penup()

g = turtle.Turtle()
g.write("재미없는 코딩님의 타자게임....",True, font = ("Arial",20,"bold"))


turtle.done()
