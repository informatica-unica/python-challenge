# Costrutto di iterazione

Il costrutto di iterazione `while` permette di eseguire una sequenza di istruzioni una o più volte, in base al verificarsi o meno di una condizione logica.
Il formato generale del costrutto è il seguente:
```python
while cond:
    # se la guardia cond e' vera, vengono eseguite le istruzioni 1,2,...,N
    # nota che le istruzioni sono indentate, come per il costrutto condizionale
    istruzione 1
    istruzione 2    
    ...
    istruzione N
    # a questo punto torna sopra, alla riga del while
    # se la condizione cond è ancora vera, continua a eseguire il ciclo
    
# le istruzioni 3 e 3 vengono eseguite quando la guardia cond diventa falsa
# notare che ho rimosso l'indentazione!
istruzione 3;
istruzione 4;    
```

Il programma nel file [main.py](main.py) usa il costrutto di iterazione per stampare la tabellina del numero scelto dall'utente. 
A tal fine, il programma chiede all'utente di inserire un numero, e lo memorizza nella variabile `num`. 
Dopodiché, il programma usa un ciclo `while` per stampare la tabellina di `num`. La guardia del `while` è la condizione logica `i<=10`, 
che è vera finché la variabile `i` è minore o uguale a 10. La variabile `i` viene inizializzata ad 1, e incrementata ad ogni iterazione.
