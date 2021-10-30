# Biglietti al cinema

Scrivi un programma che calcola l'importo per l'acquisto di biglietti al cinema.

Come primo passo, il programma chiede che venga inserito il numero di spettatori. Fatto questo, per ogni spettatore, il programma chiede l'età e se lo spettatore desidera un posto "VIP".

Una volta inseriti i dati di tutti gli spettatori, il programma calcola il prezzo totale secondo la seguente logica:

1. il prezzo base del biglietto è 8 EUR. Il prezzo extra della poltrona VIP è 1 EUR.
2. gli spettatori con meno di 12 anni hanno il 50% di sconto sul prezzo base.
3. gli spettatori con più di 65 anni hanno il 50% di sconto sul prezzo base, e hanno gratis la poltrona VIP.
4. se il gruppo di spettatori è composta da due adulti (di età maggiore o uguale a 18 anni) e da almeno due bambini (di età minore o uguale a 12 anni), allora si applica un ulteriore "sconto famiglia" del 20% sul totale.
5. se tutti gli spettatori sono over-65, e il gruppo contiene almeno 4 spettatori, allora si applica un ulteriore sconto del 20% sul totale.

Il programma deve terminare stampando il prezzo complessivo dei biglietti.
