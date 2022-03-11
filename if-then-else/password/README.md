# Password

Scrivere un programma per il controllo delle password, con la seguente specifica. 

* Dopo aver letto il nome dell'utente e la sua password da tastiera, il programma confronta la password inserita dall'utente con quella memorizzata nella variabile `pwd`. 

* Se la password inserita dall'utente coincide con quella nella variabile `pwd`, allora il programma stampa un messaggio di conferma. 

* Altrimenti, il programma stampa un messaggio di errore, e chiede all'utente di reinserire la password per un secondo tentativo. 

* Se l'utente sbaglia la password anche al secondo tentativo, il programma segnala un errore, e non permette più all'utente di inserire la password.

Ad esempio, supponendo che la password memorizzata in `pwd` sia `12345`, una possibile esecuzione del programma sarà la seguente:
```
Nome utente: pippo
Password: 11111
Hai sbagliato, riprova
Password: 12345
Password corretta!
```
