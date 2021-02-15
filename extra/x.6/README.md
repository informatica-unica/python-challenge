# Sposta la tartaruga con il mouse

Il programma allegato introduce due nuovi comandi, che permettono alla tartaruga di reagire agli eventi generati dal mouse e dalla tastiera. Il comando:

```
screen.onclick(clickHandler)
```

stabilisce che, ad ogni click del mouse, la tartaruga deve eseguire la procedura `clickHandler`, definita in questo modo:

```
def clickHandler(x,y):
```

```
  print(x,y)
```

```
  t.setpos(x,y);
```

Questa procedura stampa sulla console le coordinate `x,y` in cui è stato cliccato il mouse, e poi sposta la tartaruga alla posizione `x,y`.

Il comando:

```
screen.onkey(clearTurtle,"c")
```

stabilisce che, ogni volta che viene premuto il tasto `c` sulla tastiera, viene eseguita la procedura `clearTurtle` così definita:

```
 def clearTurtle():
```

```
  t.clear()
```

Questa procedura cancella tutto quanto disegnato finora dalla tartaruga.

Estendere il programma, in modo che: 

1. ogni volta che viene premuto il tasto spazio (`"space"`) la linea disegnata dalla tartaruga cambi colore, in modo pseudo-casuale.
2. lo schermo venga cancellato solo se il tasto `c` viene premuto **due volte** (ad esempio, se viene premuto `c`, poi `z` e poi `c`, lo schermo viene cancellato a quest'ultima pressione).
3. (opzionale) lo schermo venga cancellato solo se il tasto `c` viene premuto **due volte** **consecutive** (ad esempio, se viene premuto `c`, poi `z` e poi `c`, lo schermo non viene cancellato).

