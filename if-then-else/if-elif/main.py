# Questo programma illustra l'uso dei connettivi logici nel costrutto if-else

# chiedo all'utente di inserire da tastiera un numero compreso tra 60 di 100,
# e lo memorizzo nella varabile n

n = int(input("Inserisci un numero compreso tra 60 e 100 (estremi inclusi): "))

print(n)
# se il numero inserito e' nell'intervallo richiesto, stampo "bravo", 
# altrimenti, stampo un messaggio di errore.

if n>=60 and n<=100:
  print("bravo!")
else:
  print("asino! Il numero " + str(n) + " non e' compreso tra 60 e 100")
