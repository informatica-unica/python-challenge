# Il carattere cancelletto serve per scrivere dei commenti.
# Questi commenti non influenzano in alcun modo l'esecuzione del programma:
# servono solo come documentazione

# uso le funzioni della libreria turtle
import turtle                

wn = turtle.Screen()

# creo una tartaruga, chiamata pippo
# il nome della tartaruga non e' importante: scegliete il nome che preferite

pippo = turtle.Turtle()

# il comando speed serve per impostare la velocita' della tartaruga
# qui la sto impostando a 1, che e' la velocita' piu' bassa
pippo.speed(1)

# il comando forward serve per far avanzare la tartaruga
# qui sto mandando avanti pippo di 100 unita'
pippo.forward(300)

# il comando left serve per far ruotare la tartaruga in senso antiorario
# qui la sto ruotando di 90 gradi
pippo.left(90)

# anziche' un numero, posso usare una espressione aritmetica
# qui, sto usando l'espressione 2*(100+20), che vale 240
pippo.forward(2*(100+20))

# il comando right fa l'opposto del comando left:
# ruota la tartaruga in senso orario 
# qui sto ruotando pippo di 90 gradi
pippo.right(90)

# per vedere l'effetto della rotazione, faccio avanzare pippo di 200 unita'
pippo.forward(200)

# il comando color cambia il colore della tartaruga
# i nomi dei colori sono in inglese: black, red, green, pink, blue, ...
# qui sto facendo diventare pippo di colore rosso
pippo.color("red")

# il comando pensize serve per cambiare la larghezza della linea disegnata
# qui sto cambiando la dimensione di pippo a 5 
pippo.pensize(5)

# facendo andare avanti pippo, posso vedere il cambiamento
pippo.forward(200)

# il comando goto serve per spostare la tartaruga ad una posizione assoluta
pippo.goto(0,0)

# aggiungere il codice qui sotto (non modificare le righe sopra questo commento)

wn.exitonclick()
