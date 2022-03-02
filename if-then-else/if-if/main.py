# Questo programma illustra il costrutto if-elif

# chiedo all'utente di inserire da tastiera un numero compreso tra 60 di 100,
# e lo memorizzo nella variabile n

n = int(input("Inserisci un numero compreso tra 60 e 100 (estremi inclusi): "))

# se il numero inserito e' nell'intervallo richiesto, stampo "bravo", 
# altrimenti, stampo un messaggio di errore.

if n>=60:
  if n<=100:
    print("bravo!")
  else:
    print("asino! Il numero " + str(n) + " e' maggiore di 100")
else:
  print("asino! Il numero " + str(n) + " e' minore di 60")
