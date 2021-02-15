mport turtle, random
screen = turtle.Screen()

t = turtle.Turtle()

border_left = -250
border_right = 250
border_up = 200
border_down = -200

# inserire gli handler degli eventi sopra screen.listen()

screen.listen()

# disegna il riquadro esterno
t.speed(20)
t.up()
t.setpos(border_left,border_down)
t.down()
t.forward(border_right-border_left)
t.left(90)
t.forward(border_up-border_down)
t.left(90)
t.forward(border_right-border_left)
t.left(90)
t.forward(border_up-border_down)


# crea la tartaruga, e spostala alla posizione iniziale
ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("Red")
ball.setposition(0,0)
ball_radius = 10 # approximated!!

dx = 1
dy = 1

while True:
  (x,y) = ball.position()
  ball.setposition(x+dx,y+dy)
