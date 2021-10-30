import turtle
import random

t = turtle.Turtle()

ink = 10000

while ink>0 :
    r = random.randint(20,50)
    t.dot(r)
    ink = ink - (3.14*r*r)
    t.up()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.setpos(x,y)
    t.down()
    
