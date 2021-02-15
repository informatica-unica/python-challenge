import turtle
import random

t = turtle.Turtle()

# scegli x1 random compreso tra 0 e 300
x1 = random.randint(0,300) 
# scegli x2 random compreso tra 0 e 300
x2 = random.randint(0,300)

# stampa x1 ed x2 sulla console
print(x1,x2) 


if x1<x2:
  t.forward(x1)
else:
  t.forward(x2)

