# Numeri pseudocasuali

L'esecuzione del calcolatore è completamente deterministica: partendo dallo stesso stato iniziale ed eseguendo lo stesso programma, si otterrà sempre lo stesso risultato. 

Tuttavia, esistono alcuni comandi che *simulano* un comportamento non-deterministico. Uno di questi è il comando `randint`, che serve per generare un numero *pseudo*-casuale in un dato intervallo. Il numero si dice *pseudo*-casuale (anziché *casuale*) perché l'algoritmo usato per generarlo è comunque deterministico.

Nel programma nel file [main.py](main.py) ho usato il comando `randint` per generare un numero tra 1 e 100 (estremi inclusi), ed assegnarlo alla variabile `x`:
```
x = random.randint(1,100)
```

Più un generale, il programma genera tre numeri pseudocasuali, e li stampa sulla console. Prova ad eseguire più volte il programma, e osserva se i numeri stampati appaiono casuali.
