import turtle
import random

t = turtle.Turtle()

print("Inserisci un numero positivo:"),
n = int(input())
print("Adesso genero " + str(n) + " numeri casuali tra 1 e 100...")

for i in range(1,n+1):
  r = random.randint(1,100)
  print(r) # stampa il valore di i sulla console
