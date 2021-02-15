import turtle
import random
import math

redInk = 10000

def drawBox(x,y):
  global redInk # dichiarando la variabile redInk come global,
                # la procedura drawBox può aggiornarla 
  
  print(redInk)
  b = random.randint(10,100) # base del rettangolo
  h = random.randint(10,100) # altezza del rettangolo
  
  # se l'inchiostro non è sufficiente, 
  # usa tutto quello che c'è per disegnare un quadrato
  if b*h >= redInk:
    h = redInk // b     # integer division
    redInk = 0
  else:
    redInk = redInk-b*h # aggiorna la quantità disponibile di inchiostro

  # disegna un rettangolo, riempiendolo di rosso
  t.begin_fill()
  t.fillcolor("Red")
  t.forward(b)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.forward(b)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.end_fill()



t = turtle.Turtle()

while redInk>0 :
    r = random.randint(20,50)
       
    t.up()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.setpos(x,y)
    t.down()
    drawBox(x,y)

t.hideturtle() 
