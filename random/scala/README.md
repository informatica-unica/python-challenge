# Scala

Scrivi un programma che genera 3 carte da un mazzo di 40 carte.

Ogni carta è rappresentata da due numeri: 
* il primo numero ne rappresenta il valore (compreso tra 1 e 10, dove 1 è l'asso);
* il secondo numero ne rappresenta il seme (0 = Cuori, 1 = Quadri, 2 = Fiori, 3 = Picche).

Dopodiché, il programma stampa:
* `Scala`, se le 3 carte hanno valori consecutivi, ma semi diversi;
* `Scala reale`, se le 3 carte hanno valori consecutivi, e lo stesso seme;
* `Hai perso`, altrimenti.

Ad esempio, possibili esecuzioni del programma sono le seguenti:
```
Carta 1: 7 di 0
Carta 2: 5 di 3
Carta 3: 6 di 3
Scala
```

```
Carta 1: 7 di 1
Carta 2: 9 di 1
Carta 3: 8 di 1
Scala reale
```

```
Carta 1: 7 di 1
Carta 2: 9 di 1
Carta 3: 6 di 1
Hai perso
```
