nClienti = int(input("Numero clienti? "))
nDiavole = 0
nMargherite = 0
nNapoli = 0

i=1;

while i<=nClienti:
    # gli ingredienti permettono di preparare al massimo 3 Diavole
    if nDiavole<3:
        p = input("Cliente " + str(i) + ", che pizza scegli? (M=Margherita, N=Napoli, D=Diavola) ")
    else:
        p = input("Cliente " + str(i) + ", che pizza scegli? (M=Margherita, N=Napoli) ")

    if p=="M":
        nMargherite = nMargherite + 1
    elif p=="N":
        nNapoli = nNapoli + 1
    elif p=="D" and nDiavole<3:
        nDiavole = nDiavole+1
    else:
        print("Cliente " + str(i) + ", ordine errato")
        
    i = i+1

tot = nMargherite * 5 + nNapoli * 6 + nDiavole * 7

# se il tavolo ordina 3 diavole, allora una e' in omaggio.
if nDiavole>=3:
    tot = tot - 7

# stampa il totale
print("Totale: " + str(tot) + " EUR")


