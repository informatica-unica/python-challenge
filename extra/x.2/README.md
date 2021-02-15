# Disegna cerchi concentrici

Il programma qui a sinistra disegna 10 cerchi, di colori alternati blu e rossi. Per ottenere questo comportamento, ad ogni iterazione del ciclo `for` uso il costrutto `if ... else`.

```
if b==0 :
```

```
  t.color("Red") 
```

```
  b = 1
```

```
else :
```

```
  t.color("Blue")
```

```
  b = 0
```

Questo costrutto permette di eseguire un blocco di comandi oppure un altro, a seconda che la "guardia" dell'`if` sia vera o falsa. Nel codice a sinistra, la guardia è:

```
b == 0
```

che è vera se la variabile `b` vale 0, ed è falsa altrimenti.

Modifica il codice in modo da disegnare un "bersaglio" di 20 cerchi concentrici dai colori alternati blu, rossi e bianchi.