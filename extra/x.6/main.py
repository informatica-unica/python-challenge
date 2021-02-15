import turtle

t = turtle.Turtle()
t.setpos(0,0)
screen = turtle.Screen()

def clickHandler(x,y):
  print(x,y)
  t.setpos(x,y)

def clearTurtle():
  t.clear()

screen.onclick(clickHandler)
screen.onkey(clearTurtle,"c")

screen.listen()
# turtle.mainloop() # remove comment to execute from command line
