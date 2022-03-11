# Tris

Scrivi un programma che genera 4 carte da un mazzo di 40 carte.

Ogni carta è rappresentata da due numeri: 
* il primo numero ne rappresenta il valore (compreso tra 1 e 10, dove 1 è l'asso);
* il secondo numero ne rappresenta il seme (0 = Cuori, 1 = Quadri, 2 = Fiori, 3 = Picche).

Dopodiché, il programma stampa:
* `Tris`, se *almeno* 3 carte hanno lo stesso valore (indipendentemente dal seme);
* `Hai perso`, altrimenti.

Ad esempio, possibili esecuzioni del programma sono le seguenti:
```
Carta 1: 2 di 0
Carta 2: 7 di 3
Carta 3: 2 di 1
Carta 4: 2 di 2
Tris
```

```
Carta 1: 7 di 0
Carta 2: 7 di 3
Carta 3: 7 di 2
Carta 4: 7 di 2
Tris
```

```
Carta 1: 7 di 0
Carta 2: 7 di 3
Carta 3: 8 di 2
Carta 4: 8 di 1
Hai perso
```
