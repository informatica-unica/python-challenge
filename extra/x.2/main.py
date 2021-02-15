import turtle
import random

t = turtle.Turtle()

b = 0

for i in range(20):
  
  if b==0 :
    t.color("Red") 
    b = 1
  else :
    t.color("Blue")
    b = 0
    
  t.up()
  t.setpos(i*20,0)
  t.down()
  t.circle(10)
