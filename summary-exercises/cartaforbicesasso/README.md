# Carta, forbice, sasso

Scrivi un programma che implementa un gioco a due giocatori: un umano contro il computer. 

Prima di iniziare il gioco, il programma chiede il nome del giocatore umano, e inizializza il punteggio dei due giocatoria 0.

Il gioco è suddiviso in 10 turni. Ad ogni turno: 

1. il programma genera la "giocata" per il computer, ovvero una scelta tra "carta", "forbice" o "sasso". La giocata può essere rappresentata come un numero, generato in modo pseudo-casuale.

2. il programma chiede all'utente di inserire la propria giocata (ovvero, una rappresentazione di "carta" o "forbice" o "sasso");

3. al vincitore della mano, determinato secondo le regole del gioco "carta, forbice, sasso", viene incrementato il punteggio.

Al termine del gioco (dopo 10 turni), il programma deve stampare:

- il punteggio del giocatore umano e quello del computer;

- il nome del vincitore: quello del giocatore umano (inserito all'inizio del gioco), oppure "computer", oppure "parità" se entrambi i giocatori hanno lo stesso punteggio al termine del gioco.
