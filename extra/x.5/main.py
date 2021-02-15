import turtle
import random

achille = turtle.Turtle()
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

x_achille = 0
x_tartaruga = 5
x_end = 200

v_achille = 2   # velocità di achille
v_tartaruga = 1 # velocità della tartaruga

tartaruga.up()
tartaruga.setpos(100,50) # posizione iniziale della tartaruga

winner = "???"

while x_achille < x_end:    # la guardia andrà cambiata
  achille.forward(v_achille)
  x_achille = x_achille + v_achille
  # aggiungere codice qui
  
print ("The winner is: " + winner)
