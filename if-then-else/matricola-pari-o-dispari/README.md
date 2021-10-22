# Matricola pari o dispari

Scrivi un programma che chiede all'utente di inserire il suo numero di matricola. 
Dopodiché, se il numero inserito è pari, il programma deve stampare ``Matricola pari``, mentre se è dispari, deve stampare ``Matricola dispari``.

*Suggerimento.* Usare il costrutto condizionale, in cui (nell'ipotesi di aver memorizzato il numero di matricola nella variabile ``n``) la guardia è la seguente espressione booleana:
```
n % 2 == 0
```
Se ``n`` è pari, l'espressione valuta al booleano ``True``, mentre se è dispari valuta a ``False``.

*Suggerimento bis*. Assicurarsi che la variabile in cui si è memorizzato il numero di matricola sia di tipo intero:
```
n = int(input())
```
