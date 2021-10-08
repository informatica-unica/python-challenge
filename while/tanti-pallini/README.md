# Disegna tanti pallini

Il programma qui a fianco introduce due nuovi comandi.

Il comando `input()` permette di leggere un valore da tastiera. Ad esempio, il seguente frammento di codice:
```
n = int(input())
print(n+1)
```

Legge da tastiera un valore, lo memorizza nella variabile n, e poi stampa n+1 su schermo.

Il seguente frammento di codice:
```
for i in range(N) :
    # fai qualcosa, per N volte


    # ...
```
permette di eseguire il blocco di codice indentato sotto il `for` per un numero prefissato N di volte. 

Ad esempio, il programma allegato usa il ciclo `for` per stamapare 5 numeri casuali.

L'esercizio chiede di scrivere un programma che disegna sullo schermo tanti pallini (il loro numero deve essere letto da tastiera), scegliendo la loro posizione, dimensione e colore in modo (pseudo)casuale.