# Costrutto condizionale: if-else

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
* `n == 0`, che è vera quando il contenuto della variabile `n` è **uguale** a 0
* `n != 0`, che è vera quando il contenuto della variabile `n` è **diverso** da 0
* `n < 5`, che è vera quando il contenuto della variabile `n` è **minore** di 5 
* `n >= 7`, che è vera quando il contenuto della variabile `n` è **maggiore o uguale** a 7

In Python, le istruzioni che devono essere eseguite nel ramo `then` (ovvero, quando la guardia è vera) e quelle nel ramo `else` (quando la guardia è falsa) sono identificate attraverso dei caratteri di spaziatura. Nell'esempio sopra, ho inserito 2 spazi bianchi a sinistra delle istruzioni 1 e 2, e altrettanti per le istruzioni 3 e 4. Se non avessi inserito alcuno spazio, durante l'esecuzione del programma sarebbe stato segnalato un errore di sintassi.

Il programma nel file [main.py](main.py) illustra l'uso del costrutto condizionale su un esempio semplice. 

Dopo averlo studiato con attenzione, prova ad eseguire il programma e osservando cosa viene stampato sulla console.

Prova a fare piccole modifiche al programma, e studiane l'effetto eseguendolo.
