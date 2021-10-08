import random

# inizializza il voto a zero
voto = 0

# prima domanda
print ("Qual e' la capitale della Francia?")
# leggi la risposta da tastiera
a = input()

# controlla se la risposta è corretta
if a=="Parigi":
  # incrementa il voto
  voto = voto+1
  print ("risposta esatta!")
else: 
  print ("risposta sbagliata")

# seconda domanda

# genera un numero pseudocasuale
n = random.randint(20,100)
print ("Il numero " + str(n) + " e' divisibile per 3? (Y=yes, N=no) ")
a = input()

if (a=="Y" and n%3 == 0):
  voto = voto+1
  print ("risposta esatta!") 
elif (a=="N" and n%3 != 0):
  voto = voto+1
  print ("risposta esatta!") 
else:
  print ("risposta sbagliata")

# stampa il numero di risposte esatte
print ("Il numero di risposte esatte e': ")
print (voto)
