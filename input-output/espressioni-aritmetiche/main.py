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

# le parentesi tonde intorno a b + h serve per far si' che l'addizione
# venga eseguita prima della moltiplicazione. Se avessi scritto:
# p = b + h * 2
# allora il valore assegnato a p sarebbe stato 2 + 3 * 2 = 2 + 6 = 8, anziche' 10

# adesso scrivo l'area del rettangolo nella variabile a

a = b * h

# in questo caso non mi servono le parentesi, perche' ho solo una moltiplicazione

# infine, stampo il risultato
print("Il perimetro di un rettangolo con base " + str(b) + " e altezza " + str(h) + " e' " + str(p) + ", e la sua area e' " + str(a))
