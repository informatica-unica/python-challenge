# Boom

Il gioco del Boom è un semplice gioco numerico con queste regole:
* i giocatori contano a turno, dicendo 1, 2, 3, ...
* se il numero da dire è multiplo di 7 (ad es. 7, 14, 21, ...) oppure contiene 7 (ad es. 17, 27, 170, ...) , allora il giocatore di turno deve dire "Boom".

Implementare il gioco del Boom, con la semplificazione che anziché dire "Boom", il giocatore deve dire 0.

Ad esempio, alcune esecuzioni del programma sono le seguenti:
```
Prossimo numero: 1
Prossimo numero: 2
Prossimo numero: 3
Prossimo numero: 4
Prossimo numero: 5
Prossimo numero: 6
Prossimo numero: 7
Hai perso!
```

```
Prossimo numero: 1
Prossimo numero: 2
Prossimo numero: 3
Prossimo numero: 4
Prossimo numero: 5
Prossimo numero: 6
Prossimo numero: 0
Prossimo numero: 9
Hai perso!
```

```
Prossimo numero: 1
Prossimo numero: 2
Prossimo numero: 3
Prossimo numero: 4
Prossimo numero: 5
Prossimo numero: 6
Prossimo numero: 0
Prossimo numero: 8
Prossimo numero: 9
Prossimo numero: 10
Prossimo numero: 11
Prossimo numero: 12
Prossimo numero: 13
Prossimo numero: 0
Prossimo numero: 15
Prossimo numero: 16
Prossimo numero: 17
Hai perso!
```

*Suggerimento*: per controllare se il numero `num` corrente contiene il carattere 7, usare l'espressione booleana:
```
"7" in str(num)
```
