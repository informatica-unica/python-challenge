# Il carattere cancelletto serve per scrivere dei commenti.
# Questi commenti non influenzano in alcun modo l'esecuzione del programma:
# servono solo come documentazione

# Un programma e' formato da una sequenza di comandi,
# che vengono eseguiti uno dopo l'altro.
# Esistono modi per cambiare questo flusso di esecuzione,
# ma li vedremo piu' avanti.

# qui sto dicendo che voglio usare le funzioni della libreria turtle
import turtle                

# Creo una tartaruga, chiamata pippo
# Il nome della tartaruga non e' importante: scegliete il nome che preferite
# nello stesso programma posso usare anche piu' tartarughe, con nomi diversi

pippo = turtle.Turtle()

# Il comando speed serve per impostare la velocita' della tartaruga
# Qui la sto impostando a 1, che e' la velocita' piu' bassa

pippo.speed(1)

# Il comando forward serve per far avanzare la tartaruga
# Qui sto mandando avanti pippo di 300 unita'
# (notare che la tartaruga guarda verso destra)

pippo.forward(300)

# Il comando left serve per far ruotare la tartaruga in senso antiorario
# Qui la sto ruotando di 90 gradi
# (notare che adesso la tartaruga guarda verso l'alto)

pippo.left(90)

# Anziche' un numero, posso usare una espressione aritmetica
# Aui, sto usando l'espressione (2*(100+20)/3)-5, che vale 75
# (il simbolo asterisco denota la moltiplicazione, / la divisione)

pippo.forward(2*(100+20)/3 - 5)

# Il comando right fa l'opposto del comando left:
# ruota la tartaruga in senso orario 
# Qui sto ruotando pippo di 180 gradi: quindi, sto invertendo la direzione
# (notare che adesso la tartaruga guarda verso destra)

pippo.right(90)

# Per vedere l'effetto della rotazione, faccio avanzare pippo di 150 unita'

pippo.forward(150)
