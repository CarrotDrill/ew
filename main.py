import turtle

turtle.bgcolor("black")
turtle.setup(600,600)
screen = turtle.Screen()

t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.pensize(5)

def circle():
  t.circle(100)

x = 0 
while x > 30:
  circle()
  x += 1