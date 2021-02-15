# La tartaruga pigra

Nel frammento di codice a sinistra ho introdotto una nuova funzione:


```
random.randint(start, end)
```

Ogni volta che chiamiamo questa funzione, si ottiene un numero intero pseudocasuale compreso tra gli estremi `start` e `end`. Ad esempio, il comando:


```
x1 = random.randint(0,300) 
```

assegna alla variabile x un intero compreso tra 0 e 300. 


Il programma a fianco genera due valori pseudocasuali `x1` ed `x2`, e fa spostare la tartaruga dalla posizione originaria 0 alla posizione più vicina (ovvero, il minimo tra `x1` e `x2`).

Estendere il programma in modo che la tartaruga si sposti alla posizione più vicina tra `x1`, `x2`, `x3`, dove anche `x3` è un  valore scelto in modo pseudocasuale.
