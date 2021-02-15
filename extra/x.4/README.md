# Esercizio

Definisci due procedure con la seguente specifica:

```
drawBox(s)
```

disegna un quadrato di lato `s`, il cui vertice in basso a sinistra è nella posizione corrente della tartaruga;

```
move(x,y)
```

sposta la tartaruga dalla posizione corrente alle coordinate `x,y`. Definisci `move` senza usare la procedura di libreria `setpos`. _Suggerimento_: usare la funzione `position()`, che restituisce le coordinate della tartaruga.

Dopo aver testato le due procedure, usale per definire la procedura:

```
drawSquares(s)
```

che disegna una serie di quadrati concentrici, in cui il quadrato più esterno ha lato `s`, e la distanza tra un quadrato e l'altro è di 20 pixel. 