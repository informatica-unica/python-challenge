# Inserisci la data

Scrivi un programma che chiede di inserire da tastiera una data, definita come due numeri interi: `mese` e `giorno`.

Una volta inseriti questi dati, il programma controlla se la data inserita è corretta. 
Una data è corretta se sono rispettati i seguenti vincoli:
* `mese` è un numero compreso tra 1 e 12;
* se il `mese` è febbraio, allora `giorno` è un numero compreso tra 1 e 28;
* se il `mese` è novembre, aprile, giugno o settembre, allora `giorno` è un numero compreso tra 1 e 30;
* altrimenti, `giorno` è compreso tra 1 e 31. 

Dopo aver eseguito il controllo, il programma stampa `Data corretta` oppure `Data errata` in base all'esito.

Ad esempio, alcune possibili esecuzioni del programma sono le seguenti:
```
Inserisci il mese: 5
Inserisci il giorno: 31
Data corretta
```

```
Inserisci il mese: 2
Inserisci il giorno: 30
Data errata
```

```
Inserisci il mese: 15
Inserisci il giorno: 5
Data errata
```
