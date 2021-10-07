# Il carattere cancelletto serve per scrivere dei commenti.
# Questi commenti non influenzano in alcun modo l'esecuzione del programma:
# servono solo come documentazione

# qui sto dicendo che voglio usare le funzioni della libreria turtle
import turtle                

wn = turtle.Screen()

# creo una tartaruga, chiamata pippo
# il nome della tartaruga non e' importante: scegliete il nome che preferite
# nello stesso programma posso usare anche piu' tartarughe, con nomi diversi

pippo = turtle.Turtle()

# il comando speed serve per impostare la velocita' della tartaruga
# qui la sto impostando a 1, che e' la velocita' piu' bassa
pippo.speed(1)

# il comando forward serve per far avanzare la tartaruga
# qui sto mandando avanti pippo di 100 unita'
# (notare che la tartaruga guarda verso destra)
pippo.forward(300)

# il comando left serve per far ruotare la tartaruga in senso antiorario
# qui la sto ruotando di 90 gradi
# (notare che adesso la tartaruga guarda verso l'alto)
pippo.left(90)

# anziche' un numero, posso usare una espressione aritmetica
# qui, sto usando l'espressione 2*(100+20), che vale 240
# (il simbolo asterisco denota la moltiplicazione)
pippo.forward(2*(100+20))

# il comando right fa l'opposto del comando left:
# ruota la tartaruga in senso orario 
# qui sto ruotando pippo di 180 gradi: quindi, sto invertendo la direzione
# (notare che adesso la tartaruga guarda verso destra)
pippo.right(90)

# per vedere l'effetto della rotazione, faccio avanzare pippo di 200 unita'
pippo.forward(200)

# il comando goto serve per spostare la tartaruga ad una posizione assoluta
# notare che la tartaruga continua a lasciare la scia
pippo.goto(0,0)
