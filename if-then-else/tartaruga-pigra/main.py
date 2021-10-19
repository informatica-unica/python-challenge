### non editare il programma fino alla linea 35
import turtle
import random

def controllaSoluzione(x,y,z,d):
  if d == min(x,y,z):
    print ("Soluzione corretta!")
  else:
    print ("Soluzione errata!!!")
    print ("La distanza calcolata e' " + str(distanza) + " anziche' " + str(min(x,y,z)))

pippo = turtle.Turtle()
x1 = random.randint(0,300) 
x2 = random.randint(0,300)
x3 = random.randint(0,300) 
print(x1,x2,x3)
pippo.color("red")
pippo.up()
pippo.goto(x1,0)
pippo.dot(5)
pippo.goto(x2,0)
pippo.dot(5)
pippo.goto(x3,0)
pippo.dot(5)
pippo.goto(0,0)
pippo.down()
pippo.color("black")
distanza = 0

### pippo deve raggiungere il pallino rosso piu' vicino 
### la variabile distanza deve contenere la distanza percorsa da pippo
### importante: non e' consentito usare la funzione min

### aggiungere il codice qui sotto ###




### non toccare le linee sotto: devono essere le ultime del programma
pippo.forward(distanza)
controllaSoluzione(x1,x2,x3,distanza)
