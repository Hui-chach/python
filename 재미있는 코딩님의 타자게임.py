
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

fruit = ["사과", "바나나", "딸기", "수박", "복숭아"]

score = 0

n = randint(3,5)

for i in range(n):
    s = choice(fruit)
    word = turtle.textinput("fruit", '%s(%d/%d)' % (s, i+1, n))
    if s == word :
        score += 1

rate = score/n*100
g.penup()
g.goto(0, -50)
g.pendown()
g.write("%d/%d번 성공 수고했습니다" %(score,n), True, font = ("Arial", 15, "bold"))
g.penup()
g.goto(0,-100)
g.pendown()
g.write("정확도 : %.1f%%" % rate, True, font = ("Arial", 15, "bold"))

distance = t.distance(line)/100 * rate

t.speed(1)
t.forward(distance)
if rate == 100 :
    t.write("집에 데려다줘서 고마워!!", False, "center", font = ("Arial", 15, "bold"))
    t.left(60)
    t.right(60)
    t.left(60)
    t.right(60)
if rate>=80 :
    t.write("집이 코앞인데!! 한 번만 더 시도해줘!!", False, "center", font = ("Arial", 15, "normal"))
if rate>=50 :
    t.write("집에 가고 싶어!! ㅠ0ㅠ", False, "center", font = ("Arial", 15, "normal"))
if rate<50 :
    t.color('pink')
    t.right(360)
    t.write("거북이가 쓰러졌어 ㅋㅋㅋ", False, "center", font = ("Arial", 15, "normal"))
