import random as rd
import turtle

t = turtle.Turtle()
t.shape('turtle')

x = rd.randint(0, 300)
y = rd.randint(0, 300)

t.goto(x, y)

x = rd.random() + rd.randint(0,300)
y = rd.random() + rd.randint(0,300)

t.goto(x, y)
 

x = rd.random() + rd.randint(0,300)
y = rd.random() + rd.randint(0,300)

t.goto(x, y)

turtle.done()
