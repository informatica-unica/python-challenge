import turtle
import random

t = turtle.Turtle()

# scegli x random compreso tra -100 e +100
x = random.randint(-100,100) 

# scegli y random compreso tra -100 e +100
y = random.randint(-100,100)

# stampa x ed y sulla console
print(x,y) 

# solleva la testina
t.up()
# posizionati alle coordinate x,y
t.setpos(x,y)
# abbassa la testina
t.down()

# imposta un colore RGB (R=red, G=green, B=blue)
t.color(100,200,300)

# disegna un pallino di raggio 50
t.dot(50)
