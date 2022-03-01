# Questo programma illustra il comando di output su console (print)

# il comando print stampa la stringa racchiusa tra le parentesi tonde
# una stringa e' una sequenza di caratteri racchiusa tra virgolette
# Esempi di stringhe:
# "pippo"
# "ciao ciao"
# "123 stella"

print("pippo")

print("ciao ciao")

print("123")

# E' possibile concatenare due stringhe usando l'operatore +
# Ad esempio, "clara" + "bella" e' la stringa "clarabella"

print("clara" + "bella")

# Oltre alle stringhe, il comando print puo' stampare anche numeri:
print(42)

# Tuttavia, non e' possibile concatenare una stringa con un numero
# Il seguente comando darebbe un errore (togliere il commento e provare)

# print(123 + " stella")

# Per concatenare un numero ad una stringa, bisogna prima convertire il numero
# in una stringa, e poi usare l'operatore di concatenazione tra 2 stringe
# Il comando str(n) converte il numero n in una stringa

print(str(123) + " stella")


