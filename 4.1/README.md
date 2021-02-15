**Disegna 3 pallini**

Nel frammento di codice allegato ho introdotto una nuova procedura:

```
random.randint(start,end)
```

Ogni volta che chiamiamo `random.randint(start,end)`, otteniamo un numero intero (pseudo)casuale compreso tra gli estremi `start` ed `end`. Ad esempio, il comando:

```
x = random.randint(-100,100) 
```

assegna alla variabile `x` un intero compreso tra -100 e +100. 

Il programma allegato disegna un pallino celeste alle coordinate x, y generate con `randint()`.  Per disegnare il pallino, ho usato la procedura:

```
dot(n)
```

dove n è il raggio del pallino.

L'esercizio richiede di:
* definire una nuova procedura `pallino()`, che disegna un pallino la cui posizione, raggio e colore sono scelti in modo (pseudo)casuale.
* usare la nuova procedura per disegnare 3 pallini.
