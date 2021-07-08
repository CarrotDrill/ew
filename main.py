import turtle

turtle.bgcolor("black")
turtle.setup(800,800)
screen = turtle.Screen()

t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.forward(150)
t.pensize(5)

def circle():
  t.circle(100)

x = 0 
while x > 30:
  circle()
  x += 1