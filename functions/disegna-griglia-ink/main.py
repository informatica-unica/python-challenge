import turtle

def drawLine(n):
  global ink
  if (ink>=n): 
    pippo.forward(n)
    ink = ink - n
    print("Inchiostro disponibile: " + str(ink))
  else:
    print("Ho finito l'inchiostro!")

ink = 2800

pippo = turtle.Turtle(); # crea una tartaruga

# disegna la griglia 3x3 qui sotto, usando solo:
# drawLine() e left()

drawLine(300)

turtle.done()
