import turtle

screen = turtle.Screen()
t = turtle.Turtle()

#disegna il quadrato esterno
t.speed(20)
t.up()
t.setpos(-200,-200)
t.down()
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)

# posiziona la tartaruga al centro del quadrato
t.up()
t.setpos(0,0)
t.down()
t.speed(1)

score = 0

# loop della tartaruga: la guardia andrà modificata per far terminare il gioco!
while True:
  t.forward(1)
  (x,y) = t.position() # (x,y) sono le coordinate correnti della tartaruga
  
  # aggiungere il codice del ciclo while qui sotto  
  # ricordarsi di aggiornare il punteggio
  # controllare che la tartaruga non esca dal quadrato


# stampa il punteggio
turtle.color("Red")
turtle.write("Game over", align="center", font=("Courier", 32))
turtle.setposition(0, -50)
turtle.write("Score =" + str(score), align="center", font=("Courier", 8))
print("Final score: " + str(score))

# turtle.mainloop()
