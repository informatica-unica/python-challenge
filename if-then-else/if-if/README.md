# Costrutto condizionale: if annidati

Nelle lezioni precedenti abbiamo visto come eseguire un comando `cmd1` oppure
un altro comando `cmd2` in base al verificarsi o meno di una condizione `cond1`:
```python
if cond1:
  cmd1
else:
  cmd2
```

Il costrutto if-else può essere annidato all'interno di un altro
per dar luogo a comportamenti più complessi.
Ad esempio, nel programma qui sopra, il comando `cmd1` può 
essere un altro comando `if-then` con condizione `cond2`: 
```python
if cond1:
  if cond2:
    cmd11
  else:
    cmd12
else:
  cmd2
```

È importante rispettare la spaziatura, 
inserendo un numero fisso di spazi bianchi (nell'esempio sopra, 2)
per ogni blocco di comandi da eseguire nel ramo `then` e nel ramo `else`.

Il programma nel file [main.py](main.py) illustra l'uso del costrutto `elif` su un esempio semplice. 

Dopo averlo studiato con attenzione, prova ad eseguire il programma e osservando cosa viene stampato sulla console.

Prova a fare piccole modifiche al programma, e studiane l'effetto eseguendolo.
