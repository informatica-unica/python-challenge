print("Inserisci un numero tra 1 e 10")
num = int(input())
print("Stampo la tabellina del " + str(num))

i=1

while i<=10:
  prodotto = num * i
  print(str(num) + " * " + str(i) + " = " + str(prodotto))
  i = i+1

print("Fine")

