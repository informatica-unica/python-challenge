# Questo programma illustra l'uso di espressioni aritmetiche
# all'interno dei comandi di assegnamento.

# Voglio stampare il perimetro e l'area di un rettangolo con base e altezza date

# scrivo un numero nella variabile b (base)
b = 2

# scrivo un numero nella variabile h (altezza)
h = 3

# scrivo il perimetro del rettangolo nella variabile p
# il perimetro del rettangolo e' il doppio della somma tra base e altezza
# l'operatore di addizione si scrive con il simbolo +
# l'operatore di divisione si scrive con il simbolo *

p = (b + h) * 2

# scrivo l'area del rettangolo nella variabile a

a = b * h

# infine, stampo il risultato
print("Il perimetro di un rettangolo con base " + str(b) + " e altezza " + str(h) + " e' " + str(p) + ", e la sua area e' " + str(a))
