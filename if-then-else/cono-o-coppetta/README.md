# Cono o coppetta?

Scrivi un programma che calcola il prezzo di un gelato, secondo il seguente listino prezzi:
- 1 gusto: 2.5 EUR
- 2 gusti: 3 EUR
- 3 gusti: 3.5 EUR
- aggiunta di cioccolato: 0.50 EUR (disponibile solo sul cono)

Il programma deve segnalare errore nel caso di input scorretti (ad esempio, numero di gusti inferiore a 1 o superiore a 3).

Alcuni esemi di esecuzione del programma sono i seguenti:
```
Cono (0) o coppetta (1)? 1
Quanti gusti? (max 3) 3
Totale: 3.5 EUR
```
```
Cono (0) o coppetta (1)? 0
Aggiunta cioccolata? (s/n)? n
Quanti gusti? (max 3) 3
Totale: 3.5 EUR
```
```
Cono (0) o coppetta (1)? 0
Aggiunta cioccolata? (s/n)? s
Quanti gusti? (max 3) 3
Totale: 4.0 EUR
```
```
Cono (0) o coppetta (1)? 0
Aggiunta cioccolata? (s/n)? s
Quanti gusti? (max 3) 5
ERRORE
```
