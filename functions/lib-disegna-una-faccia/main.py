import turtle;

def drawEye(x,y,r,ec) :
  # x,y : centro dell'occhio
  # r : raggio dell'occhio
  # ec : colore
  t.up()
  # aggiungi codice qui

def drawMouth(x,y,r,mc,bc) :
  # x,y : centro della bocca
  # r : raggio della bocca
  # mc : colore della bocca
  # bc : colore del background
  t.up()
  # aggiungi codice qui
  
def drawFace(x,y,ec,mc,bc) :
  # ec = colore degli occhi
  # mc = colore della bocca
  # bc = colore del background
  t.up()
  # aggiungi codice qui
  
t = turtle.Turtle()

drawFace(0,0,"Blue","Red","Pink")
drawFace(200,0,"Black","Red","Brown")

t.hideturtle()
