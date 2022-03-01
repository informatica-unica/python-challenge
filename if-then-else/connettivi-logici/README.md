# Connettivi logici

Nell'esempio del costrutto if-else che abbiamo visto [qui](../if-then-else/main.py) abbiamo usato una condizione logica semplice, ovvero il confronto tra il contenuto di una variabile e un numero.

I connettivi logici: 
* `not` (negazione logica) 
* `and` (congiunzione logica)
* `or` (disgiunzione logica)

permettono di costruire condizioni logiche complesse a partire da condizioni semplici.

Ad esempio, partendo dalle espressioni booleane semplici `nome=="pippo"` e `anni<5`, è possibile ottenere le espressioni composte:
* `not (anni<5)`: questa espressione è vera quando `anni<5` è falsa (ovvero, quando `anni` è maggiore o uguale a 5)
* `nome=="pippo" and anni<5`: questa espressione è vera se entrambe le espressioni `nome=="pippo"` e `anni<5` sono vere
* `nome=="pippo" or anni<5`: questa espressione è vera se almeno una tra le espressioni `nome=="pippo"` e `anni<5` è vera.

Il programma nel file [main.py](main.py) raffina l'esempio visto in precedenza usando i connettivi logici.

Dopo averlo studiato con attenzione, prova ad eseguire il programma e osservando cosa viene stampato sulla console. 

Prova a fare piccole modifiche al programma, e studiane l'effetto eseguendolo.
