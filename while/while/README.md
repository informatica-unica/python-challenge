# Costrutto di iterazione

Il costrutto di iterazione `while` permette di eseguire una sequenza di istruzioni un numero indefinito volte, in base al verificarsi o meno di una condizione logica.
Il formato generale del costrutto è il seguente:
```python
while cond:
    # se la condizione cond e' vera, vengono eseguite le istruzioni 1,2,...,N
    # nota che le istruzioni sono indentate, come per il costrutto condizionale
    istruzione 1
    istruzione 2    
    ...
    istruzione N
    # a questo punto torna sopra, alla riga del while
    # se la condizione cond è ancora vera, continua a eseguire il ciclo
    
# le istruzioni 3 e 4 sono indentate al livello del while, 
# e vengono eseguite quando la condizione cond diventa falsa
istruzione 3
istruzione 4
```

Il programma nel file [main.py](main.py) usa il costrutto di iterazione per stampare la tabellina del numero scelto dall'utente. 
Il programma ha la seguente struttura: 
* chiede all'utente di inserire un numero, e lo memorizza nella variabile `num`;
* inizializza una variabile `i` ad 1;
* usa un ciclo `while` per stampare la tabellina di `num`: 
  * la guardia del `while` è la condizione logica `i<=10`, che è vera fintanto che la variabile `i` è minore o uguale a 10;
  * la variabile `i` viene incrementata ad ogni iterazione;
  * in questo modo, quando il valore di `i` diventa 10, la guardia del `while` diventa falsa, e il ciclo termina.
