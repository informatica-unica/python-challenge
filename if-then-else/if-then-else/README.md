# Costrutto condizionale

Il programma allegato introduce il costrutto condizionale, che permette di eseguire istruzioni diverse in base al verificarsi o meno di una condizione.

Dopo aver letto il nome dell'utente e la sua password da tastiera, il programma confronta la password inserita dall'utente con quella memorizzata nella variabile `pwd`. Se le due password sono uguali, allora il programma stampa un messaggio rassicurante, altrimenti stampa due messaggi di errore.

Il formato generale del costrutto condizionale e' il seguente:
```python
if condizione:
    # queste istruzioni vengono eseguite se condizione e' vera
    istruzione V1;
    istruzione V2;    
    ...
else:
    # queste istruzioni vengono eseguite se condizione e' false
    istruzione F1;
    istruzione F2;    
    ...
```

Notare che le istruzioni dentro il ramo `if` e dentro il ramo `else` possono a loro volta essere dei costrutti condizionali. Nell'esempio, questa caratterostica e' usata per permettere all'utente di reinserire la password, se la prima volta ha sbagliato ad inserirla. Inoltre, il programma memorizza nella variabile `tentativiErrati` il numero di tentativi errati.
