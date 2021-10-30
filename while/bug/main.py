import turtle
import random

t = turtle.Turtle()

# inizializza la variabile ink
ink = 10000

while ink>0 :
    # genera in modo casuale il raggio del pallino
    r = random.randint(20,50)
    
    # disegna il pallino
    t.dot(r)
    
    # sottrae dalla variabile ink l'inchiostro che e' servito per disegnare il pallino
    # 3.14 * r* r è una buona approssimazione dell'area del pallino di raggio r (il bug non e' qui)
    ink = ink - (3.14*r*r)
    
    # solleva la testina
    t.up()
    # riposiziona la tartaruga in una posizione random 
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.setpos(x,y)
    # riabbassa la testina
    t.down()
