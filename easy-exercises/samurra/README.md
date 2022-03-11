# Sa Murra

Scrivi un programma che implementa un gioco a due giocatori: un umano contro il computer. Prima di iniziare il gioco, il programma chiede il nome del giocatore umano, e inizializza il punteggio dei due giocatoria 0.

Il gioco è suddiviso in turni. Ad ogni turno: 

1. il programma genera due numeri pseudocasuali per il computer: la mano (un valore da 1 a 5) e la giocata (un valore da 2 a 10), in modo che il valore della giocata sia maggiore di quello della mano; questi valori vengono rivelati all'utenti soltanto dopo aver completato il passo 2;

2. il programma chiede all'utente di inserire la propria mano e la propria giocata;

3. il programma stampa la mano e la giocata del computer;

4. se la giocata di un giocatore è uguale alla somma delle due mani, allora il punteggio di quel giocatore (umano o computer) viene incrementato.

Il gioco termina quando uno dei due giocatori ha raggiunto 3 punti, oppure quando sono state giocate 16 mani.

Al termine del gioco, il programma deve stampare:

- il punteggio del giocatore umano e quello del computer;

- il nome del vincitore: quello del giocatore umano (inserito all'inizio del gioco), oppure "computer", oppure "parità" se entrambi i giocatori hanno lo stesso punteggio al termine del gioco.
