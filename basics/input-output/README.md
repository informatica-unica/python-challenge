# Input-output da console

Il programma allegato mostra come leggere messaggi dalla tastiera, e come stampare messaggi sulla console. Prova ad eseguire il programma, inserendo da tastiera quanto richiesto, e osservando cosa viene stampato sulla console.

Fatto questo, studia il programma. La prima istruzione e' questa:
```
print ("come ti chiami? ");
```
L'effetto di questa istruzione e' di stampare sulla console la stringa racchiusa tra le virgolette.

L'istruzione successiva e' piu' complessa: 
```
nome = input();
```
L'effetto e' il seguente. Il programma legge da tastiera un messaggio di testo. Una volta che l'utente ha terminato l'inserimento (premendo il tasto invio), il messaggio inserito viene **assegnato** alla variabile `nome`. 

La terza istruzione del programma:
```
print ("ciao, " + nome);
```
stampa la stringa `ciao`, seguita dal contenuto della **variabile** `nome`, ovvero il messaggio inserito in precedenza dall'utente. L'operatore + serve per concatenare due stringhe.

Il resto del programma e' una variazione sul tema del frammento appena visto.

Per esercizio, scrivi un programma che chiede all'utente il suo nome, qual e' la sua pizza preferita, e qual e' il suo dolce preferito, e stampa sulla console un messaggio del tipo:

```
ciao, Pippo! La tua pizza preferita e' Margherita, mentre il tuo dolce preferito e' Castagnaccio
```
