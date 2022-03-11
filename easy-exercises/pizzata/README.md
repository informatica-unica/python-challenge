# Pizzata

Scrivi un programma per calcolare il conto di un tavolo in pizzeria, secondo la seguente specifica.

Inizialmente, il programma chiede che venga inserito il numero di clienti al tavolo. Fatto questo, per ogni cliente, il programma chiede:

* il tipo di pizza scelta (M = Margherita, N = Napoli, D = Diavola)

* gli ingredienti della pizzeria permettono di preparare al massimo 3 Diavole. Se 3 clienti del tavolo ordinano la Diavola, ai clienti successivi verrà chiesto di ordinare solo tra Margherita e Napoli.

Una volta prese le ordinazioni di tutti i clienti, il programma calcola il totale dell'ordine, secondo la seguente logica:
* il prezzo della Margherita è 5 EUR, quello della Napoli 6 EUR, e quello della Diavola 7 EUR;
* se il tavolo ordina 3 diavole (eventualmente, in aggiunta alle altre pizze), allora una è in omaggio.

Il programma deve terminare stampando il totale complessivo dell'ordine.
