# Albero di Natale custom

Scrivi un programma che stampa sulla console un albero di Natale di altezza scelta dall'utente (compresa tra 1 e 20).

Ad esempio, se l'utente sceglie come altezza 3, il programma stampa:
```
  *
 ***
***** 
```

mentre se l'utente sceglie come altezza 5, il programma stampa:
```
    *
   ***
  *****
 *******
*********
```

*Suggerimento*: usandolo come abbiamo fatto finora, il comando `print` va a capo ogni volta che viene eseguito. Ad esempio, eseguendo il programma:
```python
print("*")
print("*")
print("*")
```
otteniamo come output:
```
*
*
*
```

Per non andare a capo dopo la stampa, usare il comando nel modo seguente:
```python
print("*", end='')
print("*", end='')
print("*", end='')
```
In questo modo, l'output sarà:
```
***
```
