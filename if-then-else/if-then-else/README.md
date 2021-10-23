# Costrutto condizionale

Il costrutto condizionale permette di eseguire istruzioni diverse in base al verificarsi o meno di una condizione.
Il formato generale del costrutto è il seguente:
```python
if cond:
    # le istruzioni 1 e 2 vengono eseguite se la guardia cond e' vera
    istruzione 1;
    istruzione 2;    
    ...
else:
    # le istruzioni 3 e 3 vengono eseguite se la guardia cond e' falsa
    istruzione 3;
    istruzione 4;    
    ...
```
La guardia usata nel costrutto condizionale è un *espressione booleana*. Ad esempio, sono espressioni booleane:
* `True`, che è sempre vera
* `False`, che è sempre falsa
* `n == 0`, che è vera quando il contenuto della variabile `n` è uguale 0
* `n < 5`, che è vera quando il contenuto della variabile `n` è minore di 5
* `not exp`, la negazione logica dell'espressione booleana `exp` (ad esempio: `not (n < 5)`)
* `exp1 and exp2`, la congiunzione logica delle espressioni booleane `exp1` ed `exp2` (esempio: `n < 5 and m < 7`)
* `exp1 or exp2`, la disgiunzione logica delle espressioni booleane `exp1` ed `exp2` (esempio: `n < 5 or m < 7`)

In Python, le istruzioni che devono essere eseguite nel ramo `then` (ovvero, quando la guardia è vera) e quelle nel ramo `else` (quando la guardia è falsa) sono identificate attraverso dei caratteri di spaziatura. Nell'esempio sopra, ho inserito 4 spazi bianchi a sinistra delle istruzioni 1 e 2, e altrettanti per le istruzioni 3 e 4. Se non avessi inserito alcuno spazio, durante l'esecuzione del programma sarebbe stato segnalato un errore di sintassi.

Il programma nel file [main.py](main.py) illustra l'uso del costrutto condizionale per il controllo delle password. Dopo aver letto il nome dell'utente e la sua password da tastiera, il programma confronta la password inserita dall'utente con quella memorizzata nella variabile `pwd`. Se le due password sono uguali, allora il programma stampa un messaggio rassicurante, altrimenti stampa due messaggi di errore.

Notare che le istruzioni dentro il ramo `if` e dentro il ramo `else` possono a loro volta essere dei costrutti condizionali. 
Nell'esempio, questa caratteristica è usata per permettere all'utente di reinserire la password, se la prima volta ha sbagliato ad inserirla. 
Inoltre, il programma memorizza nella variabile `tentativiErrati` il numero di tentativi errati.
