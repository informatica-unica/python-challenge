# Questo programma illustra il costrutti di assegnamento, 
# che serve per memorizzare un valore in una variabile.

# Il seguente comando assegna alla variabile colore, il valore "fuxia"
# (come abbiamo visto nella lezione sul comando di output, "fuxia" e' una stringa)

colore = "fuxia"

# Dopo aver eseguito il comando, il contenuto della variabile colore
# sara' la stringa "fuxia".
# Per verificarlo, proviamo a stampare il contenuto della variabile
# usando il comando di output

print(colore)

# Attenzione: sto usando il comando print in modo diverso rispetto a quanto
# visto nella lezione corrispondente. Prima stavamo usando print per stampare
# direttamente una stringa. 
# Per capire la differenza, si confronti il comando precedente con:

print("colore")

# Notare che il risultato dei due comandi e' diverso:
# print(colore) stampa il contenuto della variabile colore
# print("colore") stampa la string "colore"

# Usando nuovamente il comando di assegnamento, possiamo sovrascrivere il
# valore contenuto di una variabile

colore = "rosa"

# Usiamo il comando print per vedere il nuovo contenuto della variabile:

print(colore)

# Siccome la variabile colore contiene una stringa, possiamo usare 
# la concatenazione di stringhe per stampare messaggi composti. Ad esempio:

print ("Il mio preferito e' il " + colore)
