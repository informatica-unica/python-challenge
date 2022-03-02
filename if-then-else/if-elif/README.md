# Costrutto condizionale: if-elif

Negli esempi precedenti abbiamo usato il costrutto condizionale per eseguire un comando `cmd1` oppure un altro comando `cmd2` in base al fatto che una condizione `cond1` sia vera o falsa:
```python
if cond1:
  cmd1
else:
  cmd2
```

Più in generale, è possibile usare il costrutto condizionale per verificare una sequenza di condizioni, ed eseguire il comando corrispondente.
Ad esempio:
```python
if cond1:
  cmd1
elif cond2:
  cmd2
else:
  cmd3
```

Il comportamento del programma qui sopra è il seguente:
* se la condizione `cond1` è vera, allora esegui il comando `cmd1`;
* altrimenti, se la condizione `cond2` è vera, allora esegui il comando `cmd2`;
* altrimenti (ovvero, se sia `cond1` che `cond2` sono false), allora esegui il comando `cmd3`.

Il programma nel file [main.py](main.py) illustra l'uso del costrutto `elif` su un esempio semplice. 

Dopo averlo studiato con attenzione, prova ad eseguire il programma e osservando cosa viene stampato sulla console.

Prova a fare piccole modifiche al programma, e studiane l'effetto eseguendolo.
