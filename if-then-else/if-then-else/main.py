# Questo programma illustra l'uso del costrutto if-else

# chiedo all'utente di inserire da tastiera un numero minore di 100,
# e lo memorizzo nella varabile n

n = input("Inserisci un numero minore di 100: ")

# se il numero inserito e' veramente minore di 100, stampo "bravo", 
# altrimenti, stampo un messaggio di errore.

if n<100:
  print("bravo!")
else:
  print("asino! Il numero " + str(n) + " non e' minore di 100")
